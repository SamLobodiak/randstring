from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    print("***********going through INDEX views***********")
    longstring = unique_id = get_random_string(length=16)
    print("The long string is: ", longstring)
    context = {
        'big_string': longstring
    }
    return render(request, 'first_app/index.html', context)

def test(request):
    longstring = unique_id = get_random_string(length=16)
    context = {
        "big_string": longstring,
        "email" : "blog@gmail.com",
        "name" : "mike"
     }
    return render(request, "first_app/index.html", context)

def create(request):
    longstring = unique_id = get_random_string(length=16)
    context = {
        "big_string": longstring,
        "email" : "blog@gmail.com",
        "name" : "mike"
     }
    return render(request, "first_app/index.html", context)
#     response = "Hello, I am a TEST."
#     return HttpResponse(response)

# def show(request, blog_id):
#     print(blog_id)
#     return HttpResponse("placeholder to display blog {}".format(blog_id))
