from django.urls import path
from .views import some_view

urlpatterns = [
    path('', some_view, name="index"),
    path('url/<url>/', some_view, name='some_view'),
]

