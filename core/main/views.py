from django.shortcuts import render

# Create your views here.

def email_verification_needed_view(request):
    return render(request, "email_verification_needed.html")