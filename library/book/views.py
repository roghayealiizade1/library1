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

def standard_book_list(request, name):
    filter_list = []
    for item in bookk:
        if name in item["name"]:
            filter_list.append(item)

    context = {"books": filter_list}
    return render(request,'templates/list.html', context=context)

def detail(request, id):
    selected_book = {}
    for item in bookk:
        if item["id"] == id:
            selected_book = item
            break

    return render(request,'templates/detail.html', context=selected_book)

def detail2(request):
    id = request.GET.get("id", 0)
    return HttpResponse(id)




