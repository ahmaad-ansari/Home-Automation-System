# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# models.py in your lightcontrol app

from django.db import models

class Setting(models.Model):
    auto_mode = models.BooleanField(default=False)
    led_state = models.BooleanField(default=False)