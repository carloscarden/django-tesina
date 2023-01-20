from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from snippets.models.Lel import Lel

from snippets.models.constructorMD import ConstructorMD
from snippets.models.termino import Termino
# Create your views here

@csrf_exempt
def caca(request):


    a = ConstructorMD()



    if request.method == 'GET':
        thisdict = {
            "brand": "Ford",
            "model": "Mustang",
            "year": 1964
        }
        return JsonResponse(thisdict)



