import cv2
import numpy as np
import time

def create_white_cloak_effect_improved():
    """
    Simulates a 'white cloak' by replacing white/light areas with a pre-recorded background,
    with improved mask refinement to reduce visible parts of the paper.
    """
    print("Preparing to capture background. Please ensure the area is clear.")
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not access webcam.")
        return

    print("Capturing background in 3 seconds...")
    time.sleep(3)

    ret, background = cap.read()
    if not ret:
        print("Error: Failed to capture background frame.")
        return
    
    background = np.flip(background, axis=1)

    print("Background captured. You can now use a white object to become 'invisible'.")
    print("Press 'q' to exit the program.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = np.flip(frame, axis=1)
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # A wider range to better capture various shades of white under different lighting
        lower_white = np.array([0, 0, 150], dtype=np.uint8)
        upper_white = np.array([255, 30, 255], dtype=np.uint8)
        
        mask = cv2.inRange(hsv_frame, lower_white, upper_white)

        # Refine the mask using more aggressive morphological operations
        # This helps to fill small holes and smooth out the edges of the mask
        kernel = np.ones((7, 7), np.uint8)  # Using a larger kernel size
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=3) 
        mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel, iterations=2) 
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=1)

        # Create a reverse mask
        inverse_mask = cv2.bitwise_not(mask)

        # Combine the frames
        frame_without_white = cv2.bitwise_and(frame, frame, mask=inverse_mask)
        background_for_white = cv2.bitwise_and(background, background, mask=mask)
        
        final_output = cv2.addWeighted(frame_without_white, 1, background_for_white, 1, 0)
        
        cv2.imshow("White Cloak Effect", final_output)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    create_white_cloak_effect_improved()