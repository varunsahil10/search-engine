from django.http import HttpResponse

class BrotherMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print("Brother middleware initialised")

    def __call__(self, request):
        print("Brother before view")
        response = self.get_response(request)
        print("Brother after view")

        return response
    
class FatherMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print("Father middleware initialised")

    def __call__(self, request):
        print("Father before view")
        # response = HttpResponse("Get lost")
        response = self.get_response(request)
        print("Father after view")

        return response
    
class MotherMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print("Mother middleware initialised")

    def __call__(self, request):
        print("Mother before view")
        response = self.get_response(request)
        print("Mother after view")

        return response
    
