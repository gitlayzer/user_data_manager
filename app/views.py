from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from app.models import User
from django.http import QueryDict


# Create your views here.

def user(request):
    if request.method == 'GET':
        return HttpResponse('这是一个获取用户的请求！')
    elif request.method == 'POST':
        try:
            name = request.POST.get('name')
            city = request.POST.get('city')
            sex = request.POST.get('sex')
            age = request.POST.get('age')
            User.objects.create(
                name=name,
                city=city,
                sex=sex,
                age=age
            )
            result = {'code': 200, 'msg': '创建成功！'}
            return JsonResponse(result)
        except Exception as e:
            result = {'code': 500, 'msg': '创建失败！'}
            return JsonResponse(result)
    elif request.method == 'PUT':
        try:
            data = QueryDict(request.body)
            id = data.get('id')
            # 用户更新
            user_obj = User.objects.get(id=id)
            user_obj.name = data.get('name')
            user_obj.city = data.get('city')
            user_obj.sex = data.get('sex')
            user_obj.age = data.get('age')
            user_obj.save()
            result = {'code': 200, 'msg': '更新成功！'}
            return JsonResponse(result)
        except Exception as e:
            result = {'code': 500, 'msg': '更新失败！'}
            return JsonResponse(result)
    elif request.method == 'DELETE':
        try:
            data = QueryDict(request.body)
            id = data.get('id')
            User.objects.get(id=id).delete()
            result = {'code': 200, 'msg': '删除成功！'}
            return JsonResponse(result)
        except Exception as e:
            result = {'code': 500, 'msg': '删除失败！'}
            return JsonResponse(result)
    else:
        return HttpResponse('这是一个未知的请求！')


def user_list(request):
    userlist = User.objects.all()
    return render(request, 'userlist.html', {'userlist': userlist})


def user_add(request):
    return render(request, 'useradd.html')


def user_edit(request):
    # 拿到ID
    id = request.GET.get('id')
    user_obj = User.objects.get(id=id)
    return render(request, 'useredit.html', {'user_obj': user_obj})
