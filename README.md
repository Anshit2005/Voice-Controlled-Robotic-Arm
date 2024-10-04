# Voice Controlled Robotic Arm

## Overview
This project is a self learning project developed under the guidance of **Robotics Society IIT Jodhpur** and is designed to control a robotic arm using voice commands. The system uses the pyFirmata library to communicate with an Arduino, which controls MG90 servo motors attached to various joints of the robotic arm. Voice input is handled using the SpeechRecognition library, and text-to-speech is facilitated through pyttsx3.

## Requirements
- Python 3.x
- Arduino with servos connected to the appropriate pins
- MG90 Servo Motors
- pyFirmata
- pyttsx3
- SpeechRecognition
- word2number
- Arduino StandardFirmata firmware uploaded to the Arduino board

## Installation
1. Install the required packages using pip: pyfirmata, pyttsx3, SpeechRecognition, and word2number.
2. Upload the StandardFirmata firmware to Arduino using the Arduino IDE by selecting File -> Examples -> Firmata -> StandardFirmata, and then uploading the sketch to your Arduino board.

## Hardware Setup
1. Connect your Arduino to the computer.
2. Connect the MG90 servo motors to the appropriate pins on the Arduino:
   - Base servo: Pin 9
   - Shoulder servo: Pin 10
   - Elbow servo: Pin 11
   - Wrist servo: Pin 12
   - Grip servo: Pin 13

## Running the Application
1. Connect your Arduino to the computer.
2. Run the Python script (app.py) to start controlling the robotic arm via voice commands.

## Application Usage

### Voice Commands
- The application will prompt you to specify which servo pin to operate (e.g., say "nine" for pin 9).
- Then, the application will prompt you for the angle (e.g., say "forty-five" to set the angle to 45 degrees).

### Code Explanation
- word_to_number(word): Converts spoken number words to integers.
- speak(audio): Uses pyttsx3 to convert text to speech.
- takeCmd(): Listens for a voice command and returns the recognized string.
- rotateServo(pin, angle): Rotates the specified servo to the given angle.

### Main Application Flow
1. Initialize the Arduino and set up servo pins using pyFirmata.
2. Initialize pyttsx3 for text-to-speech.
3. Prompt the user for the servo pin and angle using voice commands, converting them into numbers.
4. Control the servos based on voice inputs.

## Example Usage
- For pin selection: User says "nine" (base servo pin 9).
- For angle selection: User says "forty-five" (servo will rotate to 45 degrees).

## Notes
- Ensure your Arduino is connected to the correct COM port and the baud rate is set correctly.
- For accurate voice recognition, use the application in a quiet environment.

## Troubleshooting
- If there are serial connection issues, verify the correct COM port is being used and that no other applications are using it.
- For voice recognition issues, ensure your microphone is functioning and test with another one if necessary. Make sure you have an active internet connection for the Google Speech Recognition API.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
