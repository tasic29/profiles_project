from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('thank-you/', views.thank_you, name='thank-you'),
]
