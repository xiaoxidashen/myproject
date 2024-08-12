from django.urls import path
from .views import SignUpView, UserView, SignInView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('me/', UserView.as_view(), name='me'),
]