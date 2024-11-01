

from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import Profile, QuestionModel
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
# Create your views here.
def index(request):
    return render(request,'index.html')

def logout(request):
    auth.logout(request)
    return redirect("/")
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    else:
        return render(request,'login.html')


def register(request):

    if request.method=='POST':
      
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if len(username)<6:
            messages.info(request,'username must be atleast 6 characters')
            return redirect('register')
        if len(password1)<8:
            messages.info(request,'password must be atleast 8 characters')
            return redirect('register')
        if(password1==password2):
               if User.objects.filter(username=username).exists():
                messages.info(request,'Username exists')
                return redirect('register')
               elif User.objects.filter(email=email).exists():
                messages.info(request,'email exists')
                return redirect('register')
               else:
                  user=User.objects.create_user(username=username,email=email,password=password1)
                  user.save()

                  user_login=auth.authenticate(username=username,password=password)
                #   auth.login(request,user_login)

                #   user_model =User.objects.get(username=username)
                #   new_profile=Profile.objects.create(user=user_model)
                #   new_profile.save()
                  return redirect('/') 

        else:
            messages.info(request,'password not matching')
            return redirect('register')

        return redirect('/')

    return render(request,"register.html")

def logout(request):
        auth.logout(request)
        return redirect("/")

def front(request):
    return render(request,"front.html")

def ds(request):
    return render(request,"ds.html")

@login_required(login_url='login')
def profile(request):
    # profile = Profile.objects.get(user=request.user)
    return render(request, 'profile.html')#, {'profile': profile})

@login_required(login_url='login')
def editProfile(request):
#    profile = Profile.objects.get(user=request.user)
#    if request.method == 'POST':
#         form = ProfileForm(request.POST, request.FILES, instance=profile)
#         if form.is_valid():
#             form.save()
#             return redirect('profile')
#         else:
#             form = ProfileForm(instance=profile)
   return render(request, 'profile-edit.html')#, {'form': form})

@login_required(login_url='login')
def deleteProfile(requeest):
    context={}
    return render(request,'confirm.html',context)#,context

def os(request):
    return render(request,"os.html")

def oop(request):
    return render(request,"oop.html")

def cns(request):
    return render(request,"cns.html")

def dbms(request):
    return render(request,"dbms.html")

def co(request):
    return render(request,"co.html")

def about(request):
    return render(request,"about.html")

def quiz_view(request):
    questions = Question.objects.prefetch_related('options').all()
    return render(request, 'quiz.html', {'questions': questions})