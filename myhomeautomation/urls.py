# Import required modules and views
from django.conf.urls import url, include
from django.contrib import admin
from lightcontrol import views as lightcontrol_views

# Define URL patterns for your project
urlpatterns = [
    # URL for the Django admin site
    url(r'^admin/', admin.site.urls),
    
    # Include the URL patterns from the 'lightcontrol' app
    url(r'^lightcontrol/', include('lightcontrol.urls')),
    
    # Map the root URL to the 'dashboard' view from the 'lightcontrol' app
    url(r'^$', lightcontrol_views.dashboard, name='home'),
]
