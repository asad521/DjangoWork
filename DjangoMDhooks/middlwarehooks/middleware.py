from django.shortcuts import HttpResponse 

# class My_proces_middleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request): 
#         response =  self.get_response(request)
#         return response
            
#     def process_view(request, *args, **kwargs):
#         print("This is process view. Before View")
#         # return HttpResponse("This is before view")
#         # for showing actual view 
#         return None

# This will occure when there is exception in main view
# class My_exception_middleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request): 
#         response =  self.get_response(request)
#         return response
            
#     def process_exception(self, request,exception):
#         msg = exception
#         return HttpResponse(msg)


class My_template_response_middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request): 
        response =  self.get_response(request)
        return response
            
    def process_template_response(self, request,response):
       print("I am template response middlware")
       response.context_data['name'] = 'muhammad asad ali'
       return response