from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests

import json

from django.contrib import messages

# Home
def home(request):
    return render(request, "homeView.html", {})

# Login
def login_view(request):
    
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        # print("Data: " + username + ", " + password)

        if (username != None and password != None):
            params = {'username': username, 'password': password}
            response = requests.post('http://127.0.0.1:3000/login', json = params)
            
            res = response.json()
            #print("respuesta: " + res['message'] + ", " + str(res['state']))

            if (res['state'] == 1):
                request.session['session_id'] = str(res['id'])
                request.session['session_username'] = str(username)
                return redirect('users')
            elif (res['state'] == 2):
                messages.info(request, 'Contraseña incorrecta')
                return render(request, "auth/loginView.html", {})
                #return HttpResponse("""your form is wrong, reload on <a href = "">reload</a>""")
            elif (res['state'] == 3):
                messages.info(request, 'Nombre de usuario incorrecto')
                return render(request, "auth/loginView.html", {})
            elif (res['state'] == 4):
                messages.info(request, 'Nombre de usuario y contraseña incorrectos')
                return render(request, "auth/loginView.html", {})

    return render(request, "auth/loginView.html", {})

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