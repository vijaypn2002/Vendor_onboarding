from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration/', include('registration.urls')),
    path('', RedirectView.as_view(url='registration/register/', permanent=False)),  # Redirect root to the registration form
]