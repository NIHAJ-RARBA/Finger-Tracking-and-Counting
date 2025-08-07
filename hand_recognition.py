import cv2
import mediapipe as mp
import math

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5
)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def is_finger_extended(tip, pip, mcp, wrist):
    """Check if finger is extended using multiple criteria"""
    # Distance-based check: tip should be farther from wrist than PIP
    tip_wrist_dist = calculate_distance(tip, wrist)
    pip_wrist_dist = calculate_distance(pip, wrist)
    
    # Angle-based check: tip should be roughly in line with MCP-PIP direction
    mcp_pip_dist = calculate_distance(mcp, pip)
    tip_pip_dist = calculate_distance(tip, pip)
    
    # Finger is extended if:
    # 1. Tip is farther from wrist than PIP
    # 2. The finger segments are reasonably straight
    distance_check = tip_wrist_dist > pip_wrist_dist * 1.1
    straightness_check = tip_pip_dist > mcp_pip_dist * 0.8
    
    return distance_check and straightness_check

def is_thumb_extended(thumb_tip, thumb_ip, thumb_mcp, wrist):
    """Check if thumb is extended using distance and angle"""
    # Distance check: tip should be farther from wrist than IP
    tip_wrist_dist = calculate_distance(thumb_tip, wrist)
    ip_wrist_dist = calculate_distance(thumb_ip, wrist)
    mcp_wrist_dist = calculate_distance(thumb_mcp, wrist)
    
    # Distance-based extension check
    distance_extended = tip_wrist_dist > ip_wrist_dist * 1.1
    
    # Additional check: thumb tip should be farther from wrist than MCP
    mcp_distance_check = tip_wrist_dist > mcp_wrist_dist * 1.05
    
    # Straightness check: thumb should be reasonably straight
    ip_mcp_dist = calculate_distance(thumb_ip, thumb_mcp)
    tip_ip_dist = calculate_distance(thumb_tip, thumb_ip)
    straightness_check = tip_ip_dist > ip_mcp_dist * 0.7
    
    return distance_extended and mcp_distance_check and straightness_check

while True:
    success, img = cap.read()
    if not success:
        break

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    finger_count = 0

    if results.multi_hand_landmarks and results.multi_handedness:
        for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
            lm_list = []
            for id, lm in enumerate(hand_landmarks.landmark):
                h, w, _ = img.shape
                lm_list.append((int(lm.x * w), int(lm.y * h)))

            # Get hand type
            hand_label = handedness.classification[0].label
            
            # Get key landmark points
            wrist = lm_list[0]
            
            # Thumb landmarks
            thumb_tip = lm_list[4]
            thumb_ip = lm_list[3]
            thumb_mcp = lm_list[2]
            
            # Finger landmarks - these indices are consistent across hands
            finger_landmarks = [
                (lm_list[8], lm_list[6], lm_list[5]),   # Index: tip, pip, mcp
                (lm_list[12], lm_list[10], lm_list[9]), # Middle: tip, pip, mcp
                (lm_list[16], lm_list[14], lm_list[13]), # Ring: tip, pip, mcp
                (lm_list[20], lm_list[18], lm_list[17])  # Pinky: tip, pip, mcp
            ]
            
            # Count extended fingers
            finger_count = 0
            fingers_status = []
            
            # Check thumb with hand-specific logic
            thumb_extended = is_thumb_extended(thumb_tip, thumb_ip, thumb_mcp, wrist)
            if thumb_extended:
                finger_count += 1
            fingers_status.append(f"T:{thumb_extended}")
            
            # Check other four fingers with curl detection
            finger_names = ["I", "M", "R", "P"]
            for i, (tip, pip, mcp) in enumerate(finger_landmarks):
                extended = is_finger_extended(tip, pip, mcp, wrist)
                if extended:
                    finger_count += 1
                fingers_status.append(f"{finger_names[i]}:{extended}")

            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # Display finger status for debugging
            status_text = " ".join(fingers_status)
            cv2.putText(img, f'{hand_label}: {status_text}', (10, 80 + len(results.multi_hand_landmarks) * 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    cv2.putText(img, f'Fingers: {finger_count}', (10, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)

    cv2.imshow("Hand Tracking", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
