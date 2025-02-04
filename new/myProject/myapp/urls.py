from . import views 
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),       # Home page route
    path('bank/', views.bank, name='bank'),  # Materialbank page route
    path('prop/', views.prop, name='prop'),  # Properties page route
    path('diagnostic/', views.diagnostic, name='diagnostic'),  # Diagnostics page route
    path('wizard/', views.wizard, name='wizard'),  # wizard page route
]