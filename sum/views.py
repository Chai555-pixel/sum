from django.shortcuts import render
from django.http import HttpResponse
def sum(request):
    a = 10
    b = 20
    result=a+b
    return HttpResponse(f"The sum of {a} and {b} is {result}.")

    