# views.py

from django.shortcuts import render, redirect
from django.http import JsonResponse
from .gpio_control import toggle_led, get_led_state, control_led_with_ldr
from .models import Setting

def dashboard(request):
    # Pass the initial state of the LED and Auto mode to the template
    setting = Setting.objects.first() or Setting.objects.create()
    context = {
        'led_state': setting.led_state,
        'auto_mode': setting.auto_mode,
    }
    return render(request, 'lightcontrol/dashboard.html', context)

def toggle_auto_mode(request):
    # Toggle Auto mode
    setting = Setting.objects.first()
    if setting:
        setting.auto_mode = not setting.auto_mode
        setting.save()
        # When Auto mode is turned on, the LED should be controlled by the LDR logic
        # This should probably be handled by a separate function or a management command as described previously
    return JsonResponse({'auto_mode': setting.auto_mode})

def toggle_led_view(request):
    # If Auto Mode is on, control the LED with the LDR
    control_led_with_ldr()
    # Toggle the LED only if Auto mode is off
    setting = Setting.objects.first()
    if not setting.auto_mode:
        new_state = toggle_led()
        setting.led_state = new_state
        setting.save()
        return JsonResponse({'led_state': new_state})
    else:
        # If Auto mode is on, return the current state without changing it
        return JsonResponse({'led_state': setting.led_state})

def led_state_view(request):
    # If Auto Mode is on, control the LED with the LDR
    control_led_with_ldr()
    # Return the LED state as JSON
    setting = Setting.objects.first()
    if setting is None:
        # If the setting does not exist, create it and assume LED is off
        setting = Setting.objects.create(led_state=get_led_state())
    else:
        # Update the setting with the current state
        setting.led_state = get_led_state()
        setting.save()
    return JsonResponse({'led_state': setting.led_state})

def control_led_with_ldr_view(request):
    # If Auto Mode is on, control the LED with the LDR
    control_led_with_ldr()
    # Return the LED state as JSON
    setting = Setting.objects.first()
    if setting:
        return JsonResponse({'led_state': setting.led_state})
    else:
        return JsonResponse({'error': 'Setting not found'}, status=404)
def auto_mode_state_view(request):
    # Return the Auto Mode state as JSON
    setting = Setting.objects.first()
    if setting is None:
        # If the setting does not exist, create it and assume Auto Mode is off
        setting = Setting.objects.create(auto_mode=False)
    return JsonResponse({'auto_mode': setting.auto_mode})