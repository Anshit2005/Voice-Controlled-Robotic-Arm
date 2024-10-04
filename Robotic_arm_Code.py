import pyfirmata
from pyfirmata import Arduino, SERVO
from time import sleep
import pyttsx3
import speech_recognition as sr
from word2number import w2n

# Set up the Arduino port and servo pins
port = 'COM3'  
base = 9
shoulder = 10
elbow = 11
wrist = 12
grip = 13
board = Arduino(port)

# Initialize servos on specified pins
board.digital[base].mode = SERVO
board.digital[shoulder].mode = SERVO
board.digital[elbow].mode = SERVO
board.digital[wrist].mode = SERVO
board.digital[grip].mode = SERVO

# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Change voice as needed

def word_to_number(word):
    """Converts spoken words (like 'one', 'two') into numbers."""
    try:
        return w2n.word_to_num(word)
    except ValueError:
        speak("Sorry, I couldn't convert that to a number.")
        return None

def speak(audio):
    """Converts text to speech."""
    engine.say(audio)
    engine.runAndWait()

def takeCmd():
    """Listens to voice input and returns the recognized string."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Understanding...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Could not understand audio, please say it again.")
        return "None"
    return query

def rotateServo(pin, angle):
    """Rotates the servo connected to the specified pin to a given angle."""
    try:
        board.digital[pin].write(angle)
        sleep(0.015)
    except Exception as e:
        print(f"Failed to rotate servo on pin {pin}. Error: {e}")

if __name__ == "__main__":
    while True:
        # Ask for the servo pin to operate
        speak("Tell me the pin you want to operate.")
        pin_input = takeCmd().lower()

        # Map voice command to actual pin number
        pin_map = {
            'base': base,
            'shoulder': shoulder,
            'elbow': elbow,
            'wrist': wrist,
            'grip': grip,
            'nine': base,
            'ten': shoulder,
            'eleven': elbow,
            'twelve': wrist,
            'thirteen': grip
        }
        
        pin = pin_map.get(pin_input, None)
        if pin is None:
            speak("Invalid pin, please try again.")
            continue
        
        # Ask for the angle
        speak("Please tell me the angle.")
        angle_input = takeCmd().lower()
        angle = word_to_number(angle_input)
        
        if angle is None or not (0 <= angle <= 180):
            speak("Invalid angle, please specify an angle between 0 and 180.")
            continue
        
        # Rotate the servo
        rotateServo(pin, angle)
        speak(f"Rotating {pin_input} servo to {angle} degrees.")
        
        # Ask if the user wants to continue
        speak("Do you want to control another servo? Yes or No.")
        response = takeCmd().lower()
        if 'no' in response:
            speak("Goodbye!")
            break
