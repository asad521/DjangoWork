from http.client import HTTPResponse
from django.shortcuts import HttpResponse


class UnderConstructionMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        
        
    def __call__(self, request):
        print("Call from middlware")
        # response = self.get_response(request)
        response = HttpResponse("<h1>Site Under Construction</h1>")
    
        print("Call from middlware after view")
        return response