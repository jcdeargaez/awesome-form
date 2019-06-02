from django.urls import path

from .views import Form

urlpatterns = [
    path('', Form.as_view()),
]
