from django.shortcuts import render
import reverse
from django.http import HttpResponse
import requests
# Create your views here.

bookk = [
    {"id": 1, "name": "test1"},
    {"id": 2, "name": "test2"}
]

def library(request):
    data = ""
    for item in bookk:
        url = reverse('book_list', args={item['id']})
        data = data + f"<a href='{url}' target='_blank'>{item['name']}</a>" + "<br>"
    return HttpResponse(data)

def book_list(request):
    context={"books":bookk}
    return render(request,'book.html', context=context)
 
def detail(request, id):
    return HttpResponse(f"book list: {id}")

def detail2(request):
    id=request.GET.get("id",0)
    return HttpResponse(id)

def random(request, number):
    response = requests.get(f'http://numberapi.com/{number}')
    a = response.text
    return HttpResponse(a)

     