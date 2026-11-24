Install VScode and Extension and 

install python and python extension also and check phthon --version //cmd for Python 3.15.2

install env first python -m venv myenv

after activate env like this D:\Python_Learn>myenv\Scripts\activate

after successfully install show this now what you install all stuff there in this myenv there


D:\Python_Learn>myenv\Scripts\activate

(myenv) D:\Python_Learn>

after install Django (myenv) D:\Python_Learn>python -m pip install Django


[notice] A new release of pip is available: 26.2.2 -> 26.3
[notice] To update, run: python.exe -m pip install --upgrade pip

(myenv) D:\Python_Learn>

 check django version cmd :(myenv) D:\Python_Learn>django-admin --version
6.1.3

after create project for use this cmd : (myenv) D:\Python_Learn>django-admin startproject Python_Project

convert to your project folder (myenv) D:\Python_Learn>cd Python_Project

run your project for use this cmd: (myenv) D:\Python_Learn\Python_Project>python manage.py runserver

Starting WSGI development server at http://127.0.0.1:8000/


in vscode run this cmd : for create app new terminal kudukanum (myenv) PS D:\Python_Learn\Python_Project> python .\manage.py startapp TestProject   


after your main Python_project seetings.py regiester you above app like this 

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'TestProject',
]


after this your project testproject view.py create this one 

from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("hello world ")

after this testproject create file like urls.py

from django.urls import path
from . import views   // important . this after one space need rule 


urlpatterns =[
    path("", views.index, name="index")
]

that urls.py this one call after your main project like Python_Project urls.py call this file 

from django.urls import path, include

urlpatterns = [
    path("", include("TestProject.urls")),
    path('admin/', admin.site.urls),
]


after one more creat Url check this one 



def details(request):
    return HttpResponse(" See yoyr second /Page ")

path("details", views.details, name="details"),


if you need Dyanamic URL this code use like (post_id) ex: http://127.0.0.1:8000/home/1

view.py:

def details(request , details_id):
    return HttpResponse(f" See your second /Page ID is {details_id} ")

urls.py:

 path("details/<int:details_id>", views.details, name="details") #Dynamic URL values 


URl Navigate :

view.py:

def old_url_redirect(request):
    return redirect("new_url")

def new_url_view(request):
    return HttpResponse("this is the new URL")



url.py:
 path("new_url", views.new_url_view, name="new_url"),
    path("old_url", views.old_url_redirect, name="old_url"),

