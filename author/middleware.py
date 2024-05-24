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
class AdvancedMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to execute for each request before the view (and later middleware) are called.
        response = self.get_response(request)
        # Code to execute for each response after the view is called.
        return response

    def process_request(self, request):
        # Called on each request, before Django decides which view to execute.
        print("Processing request")

    def process_view(self, request, view_func, view_args, view_kwargs):
        # Called just before Django calls the view.
        print(f"Processing view: {view_func.__name__}")

    def process_exception(self, request, exception):
        # Called for the response if the view raises an exception.
        print(f"Processing exception: {exception}")

    def process_template_response(self, request, response):
        # Called just after the view has finished executing if the response contains a `render` method (typically template responses).
        print("Processing template response")
        return response
