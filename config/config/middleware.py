from django.conf import settings

def tokenRequired(get_response):
    print("On initialixze")
    def func(request):
        print("before view")
        response = get_response(request)
        print("after view")
        return response
    return func


class TokenRequired:
    def __init__(self, get_response):
        self.get_response = get_response
        print("On initialixze")
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print(request.get_full_path())
        print(request.META.get('HTTP_AUTHORIZATION'))

        print(request.user)
        
        

        response = self.get_response(request)
        print("after view")

        # Code to be executed for each request/response after
        # the view is called.

        return response     


