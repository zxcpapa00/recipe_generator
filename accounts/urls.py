from django.urls import path
from .views import CustomLoginView, SignUpView

app_name = 'accounts'

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name="login"),
    path('registration/', SignUpView.as_view(), name="register")
]
