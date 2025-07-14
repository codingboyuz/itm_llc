import logging

class RequestLoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.home_logger = logging.getLogger('home')
        self.product_logger = logging.getLogger('product')

    def __call__(self, request):
        path = request.path

        if path.startswith('/home') or path == '/':
            self.home_logger.info(f"SO‘ROV: {request.method} {request.path}")
        elif path.startswith('/product'):
            self.product_logger.info(f"SO‘ROV: {request.method} {request.path}")

        response = self.get_response(request)
        return response
