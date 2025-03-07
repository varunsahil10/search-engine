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

    def process_view(self, *args, **kwargs):
        print('Just before view: Brother')
        # return HttpResponse('Brother')
    
    def process_exception(self,request,exception):
        print(f"{exception} in Btother")
        return HttpResponse(exception)

    def process_template_response(self,request, response):
        print(f'process_template_response of brother')
        response.context_data['inMiddleware'] = 'brother'
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
    
    def process_view(self, *args, **kwargs):
        print('Just before view: Father')
        # return HttpResponse('father')

    def process_exception(self,request,exception):
        print(f"{exception} in FATHERMW")
        return HttpResponse(exception)

    def process_template_response(self,request, response):
        print(f'process_template_response of father')
        response.context_data['inMiddleware'] = 'Father'
        return response

class MotherMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print("Mother middleware initialised")
        print(self.get_response)

    def __call__(self, request):
        print("Mother before view")
        response = self.get_response(request)
        print("Mother after view")

        return response
    
    def process_view(self, *args, **kwargs):
        print('Just before view: Mother')
        # return HttpResponse('Mother')

    def process_exception(self,request,exception):
        print(f"{exception} in Mother")
        # return HttpResponse(exception)

    def process_template_response(self,request, response):
        print(f'process_template_response of mother')
        response.context_data['inMiddleware'] = 'Mother'
        return response
