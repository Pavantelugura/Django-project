from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpRequest
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.utils.datastructures import MultiValueDictKeyError
import json
from bs4 import BeautifulSoup as bs

# Create your views here.

def home(request):
    return render(request, 'index.html')

# for UI
def math_operation(request):
    operation = request.POST['operation']
    num1 = int(request.POST['num1'])
    num2 = int(request.POST['num2'])
    if operation == 'add':
        r = num1 + num2
        result = 'the sum of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
    if operation == 'subtract':
        r = num1 - num2
        result = 'the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
    if operation == 'multiply':
        r = num1 * num2
        result = 'the product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
    if operation == 'divide':
        r = num1 / num2
        result = 'the quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
    return render(request, 'results.html', {"result": result})


# for standalone REST API
@api_view(["POST"])
def via_postman(request):
    request_str=(request.body).decode("utf-8")
    request_json=json.loads(request_str)
    print(request_json)
    operation = request_json["operation"]
    print("Operation : ", operation)
    num1 = int(request_json["num1"])
    num2 = int(request_json["num2"])
    #operation = "add"
    #num1 = 2
    #num2 = 3
    if operation == 'add':
        r = num1 + num2
        result = 'the sum of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
    if operation == 'subtract':
        r = num1 - num2
        result = 'the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
    if operation == 'multiply':
        r = num1 * num2
        result = 'the product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
    if operation == 'divide':
        r = num1 / num2
        result = 'the quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
    return HttpResponse(result)
