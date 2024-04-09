from django.shortcuts import render
from .models import MenuItem  # Import your MenuItem model

def some_view(request):
    template_name = "index.html"
    # Your view logic goes here
    return render(request, template_name)










