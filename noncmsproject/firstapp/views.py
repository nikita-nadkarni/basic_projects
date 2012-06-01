# Create your views here.
from django.template import Context, loader
from firstapp.models import Book
from django.http import HttpResponse

def book_view(request):
    book_list = Book.objects.all()
    t = loader.get_template('book_display.html')
    c = Context({'book_list': book_list})
    return HttpResponse(t.render(c))

def index(request):
    return HttpResponse("Hi this is the index")