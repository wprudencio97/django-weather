from django.shortcuts import render
import json
import requests 


def home(request):

    api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=28227&distance=30&API_KEY=5EB6EA4F-056E-43D3-BEC9-A7EC3FA5C04F")

    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api_request = "Error....."


    return render(request, 'home.html', {'api': api})

def about(request):
    return render(request, 'about.html', {})