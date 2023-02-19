from django.http import HttpRequest
import datetime


def set_useragent_on_request_middleware(get_response):
    print('initial call')

    def middleware(request: HttpRequest):
        print('before get response')
        # request.user_agent = request.META['HTTP_USER_AGENT']
        response = get_response(request)
        print('after get response')
        return response

    return middleware


class CountRequestsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.requests_count = 0
        self.responses_count = 0
        self.exceptions_count = 0

    def __call__(self, request: HttpRequest):
        self.requests_count += 1
        print('requests count', self.requests_count)
        response = self.get_response(request)
        self.responses_count += 1
        print('responses count', self.responses_count)
        return response

    def process_exception(self, request: HttpRequest, exception: Exception):
        self.exceptions_count += 1
        print('got', self.exceptions_count, 'exceptions so far')


class ThrottlingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.time = datetime.datetime(1900, 1, 1, 0, 0, 0, 0)

    def __call__(self, request: HttpRequest):
        user_ip = request.META['REMOTE_ADDR']
        now = datetime.datetime.now()
        result = now - self.time
        if result.seconds > -1:
            self.time = datetime.datetime.now()
        else:
            raise Exception('Frequently Asked Questions')
        response = self.get_response(request)
        return response

