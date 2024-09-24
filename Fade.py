# Import necessary modules for the program
import sys  # Provides access to system-specific parameters and functions
from PyQt5.QtWidgets import QApplication, QMainWindow, QSlider, QVBoxLayout, QWidget, QLabel  # Import PyQt5 classes for creating GUI
from PyQt5.QtCore import Qt  # Core PyQt functionality, used for alignment and slider orientation
import RPi.GPIO as GPIO  # Import the RPi.GPIO library to control Raspberry Pi GPIO pins

# Set GPIO mode to BCM, which refers to the Broadcom chip pin numbering on the Raspberry Pi
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin numbers for the LEDs: Red, Green, and White
RED_PIN = 19
GREEN_PIN = 22
WHITE_PIN = 24

# Set each pin as an output pin to control the corresponding LEDs
GPIO.setup(RED_PIN, GPIO.OUT)  # Set the RED_PIN (18) as an output pin
GPIO.setup(GREEN_PIN, GPIO.OUT)  # Set the GREEN_PIN (23) as an output pin
GPIO.setup(WHITE_PIN, GPIO.OUT)  # Set the WHITE_PIN (24) as an output pin

# Initialize PWM (Pulse Width Modulation) on each LED pin to control brightness
pwm_red = GPIO.PWM(RED_PIN, 200)  # Set PWM on the red LED with a frequency of 200Hz
pwm_green = GPIO.PWM(GREEN_PIN, 100)  # Set PWM on the green LED with a frequency of 100Hz
pwm_white = GPIO.PWM(WHITE_PIN, 100)  # Set PWM on the white LED with a frequency of 100Hz

# Start PWM with a duty cycle of 0%, meaning the LEDs are initially off
pwm_red.start(0)  # Start the red LED PWM with brightness 0 (off)
pwm_green.start(0)  # Start the green LED PWM with brightness 0 (off)
pwm_white.start(0)  # Start the white LED PWM with brightness 0 (off)

# Function to change the brightness of the red LED
def change_red_brightness(value):
    pwm_red.ChangeDutyCycle(value)  # Change the duty cycle to the value passed by the slider (0-100%)

# Function to change the brightness of the green LED
def change_green_brightness(value):
    pwm_green.ChangeDutyCycle(value)  # Change the duty cycle for the green LED

# Function to change the brightness of the white LED
def change_white_brightness(value):
    pwm_white.ChangeDutyCycle(value)  # Change the duty cycle for the white LED

# Create the main window class for the GUI
class LEDControlGUI(QMainWindow):
    def __init__(self):
        super().__init__()  # Call the constructor of the parent class (QMainWindow)

        self.setWindowTitle("LED Brightness Control")  # Set the window title

        layout = QVBoxLayout()  # Create a vertical layout to arrange sliders and labels

        # Create a label and slider for red LED brightness
        self.red_label = QLabel("Red Brightness", self)  # Label to indicate control for red LED
        self.red_slider = QSlider(Qt.Horizontal)  # Slider to control red LED brightness
        self.red_slider.setRange(0, 100)  # Set the slider range from 0 (off) to 100 (full brightness)
        self.red_slider.setValue(0)  # Start the slider at 0% (off)
        self.red_slider.valueChanged.connect(change_red_brightness)  # When slider value changes, call the change_red_brightness function

        # Create a label and slider for green LED brightness
        self.green_label = QLabel("Green Brightness", self)  # Label to indicate control for green LED
        self.green_slider = QSlider(Qt.Horizontal)  # Slider to control green LED brightness
        self.green_slider.setRange(0, 100)  # Set the slider range from 0 (off) to 100 (full brightness)
        self.green_slider.setValue(0)  # Start the slider at 0% (off)
        self.green_slider.valueChanged.connect(change_green_brightness)  # Connect slider to the change_green_brightness function

        # Create a label and slider for white LED brightness
        self.white_label = QLabel("White Brightness", self)  # Label to indicate control for white LED
        self.white_slider = QSlider(Qt.Horizontal)  # Slider to control white LED brightness
        self.white_slider.setRange(0, 100)  # Set the slider range from 0 (off) to 100 (full brightness)
        self.white_slider.setValue(0)  # Start the slider at 0% (off)
        self.white_slider.valueChanged.connect(change_white_brightness)  # Connect slider to the change_white_brightness function

        # Add all the labels and sliders to the layout, so they appear in the window
        layout.addWidget(self.red_label)  # Add red brightness label to the layout
        layout.addWidget(self.red_slider)  # Add red brightness slider to the layout
        layout.addWidget(self.green_label)  # Add green brightness label to the layout
        layout.addWidget(self.green_slider)  # Add green brightness slider to the layout
        layout.addWidget(self.white_label)  # Add white brightness label to the layout
        layout.addWidget(self.white_slider)  # Add white brightness slider to the layout

        # Create a central widget to hold the layout and set it as the main widget of the window
        central_widget = QWidget()  # Create a central widget
        central_widget.setLayout(layout)  # Set the layout to the central widget
        self.setCentralWidget(central_widget)  # Set the central widget as the main widget of the window

# Main program execution starts here
if __name__ == '__main__':
    app = QApplication(sys.argv)  # Initialize the PyQt5 application with command-line arguments
    window = LEDControlGUI()  # Create an instance of the LEDControlGUI class
    window.show()  # Show the window on the screen
    sys.exit(app.exec_())  # Start the application's event loop, waiting for user interaction

# Clean-up code after closing the GUI
pwm_red.stop()  # Stop the PWM signal for the red LED
pwm_green.stop()  # Stop the PWM signal for the green LED
pwm_white.stop()  # Stop the PWM signal for the white LED (note: corrected from pwm_blue to pwm_white)
GPIO.cleanup()  # Reset all GPIO pins to their default state to prevent interference
