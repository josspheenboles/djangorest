# your_app/middleware.py

class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to execute for each request before the view (and later middleware) are called.
        print("Before the view is called")

        response = self.get_response(request)

        # Code to execute for each response after the view is called.
        print("After the view is called")

        return response
