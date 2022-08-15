# FUNCTION BASED MIDDLWARE
# def my_middleware(get_response):
#     print("one time initialization")
    
#     def my_function(request):
#         print("print before view ")
#         response = get_response(request)
#         print("this is after view")
#         return response
#     return my_function

# CLASS BASED MIDDLEWARE


class brother_middleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print("One Time  brother initialization")
        
    def __call__(self, request):
        response = self.get_response(request)
        print("This is brother middleware after view")
        return response

class father_middleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print("One Time  father initialization")
        
    def __call__(self, request):
        response = self.get_response(request)
        print("This is father middleware after view")
        return response
    
    
class mother_middleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print("One Time mother initialization")
        
    def __call__(self, request):
        response = self.get_response(request)
        print("This is mother middleware after view")
        return response