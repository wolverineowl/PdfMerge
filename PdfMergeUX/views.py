from django.http import HttpResponse

def home(request):
    return HttpResponse("This free and easy to use online tool allows combining multiple PDF or images files into a single PDF document without having to install any software.")