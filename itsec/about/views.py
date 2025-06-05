from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. Learning Django can take between one to four weeks for the average learner. Thorough understanding of Python fundamentals is a prerequisite to learning Django.")