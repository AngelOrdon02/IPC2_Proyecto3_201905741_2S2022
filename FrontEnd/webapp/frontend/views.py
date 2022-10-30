from django.shortcuts import render
from django.http import HttpResponse
import requests

import json

# Home
def home(request):
    return render(request, "homeView.html", {})

# Create your views here.
def users(request):

    #pull data from third party rest api
    # response = requests.get('https://jsonplaceholder.typicode.com/users')
    response = requests.get('http://127.0.0.1:3000/users')

    #convert reponse data into json
    users = response.json()
    #print(users)
    
    # return HttpResponse("Users")
    # return render(request, "users.html")
    # return render(request, "users.html", {'users': users})
    # return render(request, "users.html", {'users': users['users']})
    return render(request, "administration/usersView.html", {'users': users['users']})
    pass