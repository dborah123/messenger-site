from django.contrib.auth import authenticate, login, logout
from rest_framework import status


def login_view(request):
    username = request.get("username", None)
    password = request.get("password", None)
    
    user = authenticate(username=username, password=password)

    if (user is not None):
        login(request, user)
        return HTTP_202_ACCEPTED
    
    return HTTP_404_NOT_FOUND
