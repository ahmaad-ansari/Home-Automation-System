import RPi.GPIO as GPIO
from .models import Setting

# Set up the GPIO channels
LED_PIN = 17
LDR_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(LDR_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)

def toggle_led():
    # Get the first Setting instance from the database
    setting = Setting.objects.first()
    
    # Check if a Setting instance exists and auto_mode is off
    if setting and not setting.auto_mode:
        current_state = GPIO.input(LED_PIN)
        new_state = not current_state
        GPIO.output(LED_PIN, new_state)
        setting.led_state = new_state  # Update the model with the new LED state
        setting.save()
        return new_state
    # If in auto mode, return the current state without toggling
    return setting.led_state if setting else None

def get_led_state():
    # Get the first Setting instance from the database
    setting = Setting.objects.first()
    
    if setting:
        current_state = GPIO.input(LED_PIN)
        
        # Check if the hardware state differs from the database state
        if current_state != setting.led_state:
            setting.led_state = current_state
            setting.save()
        return current_state
    return None  # If no setting is found

def read_ldr():
    # Read the digital value (0 or 1) from the LDR's D0 pin
    return GPIO.input(LDR_PIN)

# Add this function to your gpio_control.py
def control_led_with_ldr():
    # Get the first Setting instance from the database
    setting = Setting.objects.first()
    
    if setting and setting.auto_mode:
        # If the LDR output is LOW (0), it means it's dark, and the LED should be ON
        led_on = read_ldr()  # This will be True when it's dark, and False when it's light
        GPIO.output(LED_PIN, led_on)
        setting.led_state = led_on
        setting.save()
