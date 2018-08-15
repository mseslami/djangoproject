from django.shortcuts import render


# Create your views here.

def index0(request):
    my_dict = {"insert_content": "hello i'm in the first with index 0"}
    return render(request, "first_app/index0.html", context=my_dict)


def index(request):
    my_dict = {"insert_content": "hello i'm in the first appxxxxxxxxxxxxxxxxxxx"}
    return render(request, "first_app/index.html", context=my_dict)


def index2(request):
    my_dict2 = {"insert_content": "hello i'm in the first app2222222222222222"}
    return render(request, "first_app/index2.html", context=my_dict2)
