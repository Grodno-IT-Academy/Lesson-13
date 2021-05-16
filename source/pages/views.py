from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request):
    my_context = {
        'title': "This is a home page",
        'number': 123,
        'my_list': [i for i in range(5)],
    }
    return render(request,'home.html',context=my_context)