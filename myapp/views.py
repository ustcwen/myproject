# -*- coding: utf-8 -*-
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core import serializers
import requests
import json

from .models import Book

# Create your views here.
@require_http_methods(["GET"])
def add_book(request):
    response = {}
    try:
        book = Book(book_name=request.GET.get('book_name'))
        book.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

@require_http_methods(["GET"])
def show_books(request):
    response = {}
    try:
        books = Book.objects.filter()
        response['list']  = json.loads(serializers.serialize("json", books))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


def login(request):
        form_in_line = json.loads(request.body)
        print(form_in_line)
        user = form_in_line['user']
        pwd = form_in_line['pwd']
        if user == 'root' and pwd == "root":
            # 生成随机字符串
            # 写到用户浏览器cookie
            # 保存在服务端session中
            # 在随机字符串对应的字典中设置相关内容
            request.session['username'] = user
            request.session['islogin'] = True
            if request.POST.get('rmb', None) == '1':
                # 认为设置超时时间
                request.session.set_expiry(10)
            return render(request,'index.html')
        else:
            return render(request,'index.html')


def gettable(request):
    data = {
        'code': 'ok',
        'cols_list': [
            {'prop': 'name', 'label': '名字'},
            {'prop': 'sex', 'label': '性别'}
        ],
        'each_row': [
            {'name': '小李', 'sex': '男'},
            {'name': '小红', 'sex': '女'}
        ]
    }
    return JsonResponse({'code': 200, 'data': data})
