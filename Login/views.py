from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import ThemForm


# Create your views here.
def login(request):
    a = LoginModel.objects.all()
    # context = {
    #     'f': a,
    # }
    # for i in a:
    #     print(i.user)
    #     print(i.pas)
    if request.method == 'POST':
        form = request.POST
        user_html = form['user']
        pas_html = form['pas']
        for i in a:
            if (user_html == i.user and pas_html == i.pas):
                # print("Đăng nhập")
                return HttpResponse("Đăng nhập")
            else:
                # print("Sai pass")
                return HttpResponse("Sai mật khẩu")
    return render(request, 'Login/login.html')


def them(request):
    form = ThemForm()
    list = ThemSuaXoa.objects.all()
    if request.method == 'POST':
        form = ThemForm(request.POST)
        if form.is_valid():
            fix = [';', ':', '-- -', '1=1', 'SELECT * FROM', 'ORDER', 'UNION', 'admin', '--', '""-"', '"*"', '"^"',
                   '"&"', '" "', '"-"', 'or', ]
            a = (form.data.get('title'))
            b = form.data.get('body')
            s = 0
            for i in fix:
                if (a.find(i) >= 0 or b.find(i) >= 0):
                    s = s + 1
            if s == 0:
                form.save()
                return HttpResponse("Lưu thành công")
            else:
                return HttpResponse("Xin vui lòng không nhập những từ nhạy cảm gây ra lỗi sql injection xin cảm ơn")
            return redirect("/them/")
    context = {'form': form,
               'list': list}
    return render(request, 'Login/create_update_delete.html', context)


def sua(request, pk):
    sua = ThemSuaXoa.objects.get(id=pk)
    form = ThemForm(instance=sua)
    if request.method == 'POST':
        form = ThemForm(request.POST, instance=sua)
        if form.is_valid():
            fix = [';', ':', '-- -', '1=1', 'SELECT * FROM', 'ORDER', 'UNION', 'admin', '--', '""-"', '"*"', '"^"',
                   '"&"', '" "', '"-"', 'or', ]
            a = (form.data.get('title'))
            b = form.data.get('body')
            s = 0
            for i in fix:
                if (a.find(i) >= 0 or b.find(i) >= 0):
                    s = s + 1
            if s == 0:
                form.save()
                return HttpResponse("Lưu thành công")
            else:
                return HttpResponse("Xin vui lòng không nhập những từ nhạy cảm gây ra lỗi sql injection xin cảm ơn")
        return redirect("/them/")
    context = {'form': form}
    return render(request, 'Login/create_update_delete.html', context)


def xoa(request, pk):
    xoa = ThemSuaXoa.objects.get(id=pk)
    if request.method == 'POST':
        xoa.delete()
        return redirect("/them/")
    context = {'item': xoa}
    return render(request, 'Login/xoa.html', context)
