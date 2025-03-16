import cv2
import pytesseract
import pyttsx3

# Set Tesseract-OCR executable path if needed
# Uncomment and set this to your Tesseract installation path
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def text_to_speech(text):
    """Converts text to speech using pyttsx3."""
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)
    engine.say(text)
    engine.runAndWait()

def process_camera():
    """Captures video from webcam, extracts text, and speaks it."""
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture video. Exiting...")
            break

        # Preprocess the frame for better OCR accuracy
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
        text = pytesseract.image_to_string(gray)  # Extract text using Tesseract OCR

        if text.strip():  # If text is detected
            print("Extracted Text:", text.strip())
            text_to_speech(text.strip())  # Convert text to speech

        # Display the video feed
        cv2.imshow("Webcam Feed - Press 'q' to exit", frame)

        # Exit on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    print("Starting the webcam feed. Press 'q' to exit.")
    process_camera()

