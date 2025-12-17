class FixHostMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host()

        if 'падел74.рф' in host:
            normalized = host.replace('падел74.рф', 'xn--74-6kcqf0bya.xn--p1ai')
            request.META['HTTP_HOST'] = normalized

        return self.get_response(request)