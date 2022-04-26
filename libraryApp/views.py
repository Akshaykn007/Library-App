from django.http import JsonResponse
from django.shortcuts import render,HttpResponseRedirect,get_object_or_404,redirect
from .models import *
from .forms import *
import hashlib
from rest_framework.views import APIView

def home(request):
    return render(request,"home.html")

def create(request):
    context ={}
    bookform = booksForm(request.POST)
    if bookform.is_valid():
        bookform.save()
        return redirect("/list")
    context['bookform']= bookform
    return render(request, "create.html", context)

def retrieve(request):
    context ={}
    context["booksset"] = books.objects.all()
    return render(request, "listuser.html", context)

def retrieveAdminList(request):
    context ={}
    context["booksset"] = books.objects.all()
    return render(request, "list.html", context)

def update(request,bookName):
    context ={}
    obj = get_object_or_404(books, title = bookName)
    form = booksForm(request.POST,instance = obj)
    if form.is_valid():
        form.save()
        return redirect("/list")
    context["form"] = form
    return render(request, "update.html", context)

def delete(request,bookName):
    context ={}
    obj = get_object_or_404(books,title = bookName)
    form = booksForm(request.POST,instance = obj)
    if request.method =="POST":
        obj.delete()
        return HttpResponseRedirect("/list")
    return render(request, "delete.html", context)

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        result = hashlib.sha256(password.encode('utf-8'))
        password=result.hexdigest()
        try:
            user = admin_users.objects.get(user_name=username)
        except:
            return redirect('/listuser')
        try:
            password=admin_users.objects.get(password=password)
            return redirect('/list')
        except:
            return render(request, 'login.html', {'error_message': 'Incorrect username and / or password.'})
    else:
        return render(request,'login.html')

class admin_sign_up(APIView):
    def post(self,request):
        username = request.data['username'].lower()
        try:
            admin_users.objects.get(user_name=username)
            return JsonResponse(status=200,data={"data":"Already exists"})
        except:
            pass
        password = request.data['password']
        result = hashlib.sha256(password.encode('utf-8'))
        password=result.hexdigest()
        data = admin_users(user_name=username,password=password)
        data.save()
        return JsonResponse(status=200,data={"data":"Admin created successfully"})