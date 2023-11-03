from django.urls import path
from . import views

# Define URL patterns for your views
urlpatterns = [
    # Map the root URL to the 'dashboard' view
    path('', views.dashboard, name='dashboard'),
    
    # URL for toggling the LED state
    path('toggle/', views.toggle_led_view, name='toggle_led'),
    
    # URL for getting the LED state
    path('state/', views.led_state_view, name='led_state'),
    
    # URL for toggling the auto_mode setting
    path('toggle_auto_mode/', views.toggle_auto_mode, name='toggle_auto_mode'),
    
    # URL for getting the auto_mode state
    path('auto_mode_state/', views.auto_mode_state_view, name='auto_mode_state'),
    
    # URL for controlling the LED with the LDR
    path('control_led_with_ldr/', views.control_led_with_ldr_view, name='control_led_with_ldr'),
]
