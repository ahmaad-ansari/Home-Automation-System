# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Import Django's models module
from django.db import models

# Define a Django model called 'Setting' that represents settings for light control
class Setting(models.Model):
    # Boolean field to store the auto_mode setting, defaulting to False
    auto_mode = models.BooleanField(default=False)
    
    # Boolean field to store the LED state, defaulting to False
    led_state = models.BooleanField(default=False)
