from django.http.response import HttpResponse

def home_page_view(Request,*args):
    return HttpResponse("<h1> HELLO EVERYONE</h1>")