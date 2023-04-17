from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login

# Create your views here.

def index(request):
    return render(request, 'index.html')

def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('adminpage')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form, 'msg': msg})

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('adminpage')
            elif user is not None and user.is_student:
                login(request, user)
                return redirect('student')
            elif user is not None and user.is_teacher:
                login(request, user)
                return redirect('teacher')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})

def admin(request):
    return render(request,'admin.html')


def student(request):
    return render(request,'student.html')


def teacher(request):
    return render(request,'teacher.html')

def logout_view(request):
    return render(request, 'logout.html')
def snotification(request):
    return render(request, 'snotification.html')
def bookrenewal(request):
    return render(request, 'bookrenewal.html')
def tablebook(request):
    return render(request, 'tablebook.html')
def s_about(request):
    return render(request, 's_about.html')
def s_fine(request):
    return render(request, 's_fine.html')
def s_reserve(request):
    return render(request, 's_reserve.html')
def s_borrowbook(request):
    return render(request, 's_borrowbook.html')
def s_borrowhistory(request):
    return render(request, 's_borrowhistory.html')
def s_profile(request):
    return render(request, 's_profile.html')
def contact(request):
    return render(request, 'contact.html')
def bookstats(request):
    return render(request, 'bookstats.html')
def bookupdate(request):
    return render(request, 'bookupdate.html')
def fineimpo(request):
    return render(request, 'fineimpo.html')
def datamanip(request):
    return render(request, 'datamanipulation.html')