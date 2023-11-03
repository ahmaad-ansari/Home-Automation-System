from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('toggle/', views.toggle_led_view, name='toggle_led'),
    path('state/', views.led_state_view, name='led_state'),
    path('toggle_auto_mode/', views.toggle_auto_mode, name='toggle_auto_mode'),
    path('auto_mode_state/', views.auto_mode_state_view, name='auto_mode_state'),
    path('control_led_with_ldr/', views.control_led_with_ldr_view, name='control_led_with_ldr'),

]