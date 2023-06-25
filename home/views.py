from django.shortcuts import render
from django.http import HttpResponse
from datetime import timedelta
import hashlib
import random


def generate_salt():
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    salt_length = 16
    salt = ''.join(random.choice(characters) for _ in range(salt_length))
    return salt

def home(request):
    context = {}
    cookies = request.COOKIES.get('view')
    if not cookies:
        context['show_alert'] = True

    response = render(request, 'home.html', context)
    expiration = timedelta(hours=24)
    salt = generate_salt()
    response.set_signed_cookie('view', True,  
                               max_age=expiration.total_seconds(),
                               salt=salt)
    return response

# key
# value
# max_age -> inteiro em segundos
# domain -> example.com
# secure -> True apenas HttpResponse
# httponly -> True para JS não ter acesso