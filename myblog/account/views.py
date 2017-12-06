from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login
from .forms import login_form,RegistrationForm,UserProfileForm, UserInfoForm,UserForm
from .models import UserProfile, UserInfo
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

# Create your views here.

def user_login(request):
    if request.method == "POST":
        # loginForm = login_form(request.POST)
        username = request.POST['Username']
        password = request.POST['Password']
        print(username,password)
        # if loginForm.is_valid():
        if username and password:
            # print(loginForm.cleaned_data)
            # cd = loginForm.cleaned_data
            # user = authenticate(username=cd['username'], password=cd['password'])
            user = authenticate(username=username,password=password)
            if user:
                login(request,user)
                return redirect(to="/")
            else:
                return HttpResponse("Authenticated failed")
        else:
            return HttpResponse("Invalid login")

    if request.method == "GET":
        loginForm = login_form()
        # print(loginForm)
        return render(request, "account/login.html", {'form': loginForm})

def register(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)
        if user_form.is_valid():
            new_user =user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            new_profile = userprofile_form.save(commit=False)
            new_profile.user = new_user
            UserInfo.objects.create(user=new_user)
            new_profile.save()
            return HttpResponseRedirect(reverse("account:user_login"))
        else:
            return HttpResponse('Sorry, Registered failed!')
    else:
        user_form = RegistrationForm()
        userprofile_form = UserProfileForm()
        return render(request,"account/register.html", {"form": user_form, "profile":userprofile_form})

@login_required(login_url='/account/login/')
def myself(request):
    user = User.objects.get(username=request.user.username)
    # print(user)
    userprofile = UserProfile.objects.get(user=user)
    userinfo = UserInfo.objects.get(user=user)
    return render(request, "account/myself.html", {"user":user, "userinfo":userinfo, "userprofile":userprofile})


# 用户信息修改
@login_required(login_url='/account/login/')
def myself_edit(request):
    user = User.objects.get(username=request.user.username)
    userprofile = UserProfile.objects.get(user=request.user)
    userinfo = UserInfo.objects.get(user=request.user)

    if request.method == "POST":
        user_form = UserForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)
        userinfo_form = UserInfoForm(request.POST)
        if user_form.is_valid() and userprofile_form.is_valid() and userinfo_form.is_valid():
            user_data = user_form.cleaned_data
            userprofile_data = userprofile_form.cleaned_data
            userinfo_data = userinfo_form.cleaned_data
            user.email = user_data['email']
            userprofile.birth = userprofile_data['birth']
            userprofile.phone = userprofile_data['phone']
            userinfo.school = userinfo_data['school']
            userinfo.company = userinfo_data['company']
            userinfo.profession = userinfo_data['profession']
            userinfo.address = userinfo_data['address']
            userinfo.aboutme = userinfo_data['aboutme']
            user.save()
            userprofile.save()
            userinfo.save()
            return HttpResponseRedirect('/account/my-information')
    else:
        user_form = UserForm(instance=request.user)
        userprofile_form = UserProfileForm(initial={'birth':userprofile.birth, 'phone':userprofile.phone})
        userinfo_form = UserInfoForm(initial={'school':userinfo.school, 'company':userinfo.company,
                                              'profession':userinfo.profession, 'address':userinfo.address,
                                              'aboutme':userinfo.aboutme})
        # print(user_form)
        # print(userprofile_form)
        # print(userinfo_form)
        return render(request, 'account/myself_edit.html', {'user_form':user_form, 'userprofile_form':userprofile_form,
                                                            'userinfo_form':userinfo_form})

def my_image(request):
    return render(request,'account/imagecrop.html',)

@login_required(login_url='/account/login/')
def my_image(request):
    if request.method == "POST":
        img = request.POST['img']
        # print(img)
        userinfo = UserInfo.objects.get(user=request.user.id)
        userinfo.photo = img
        userinfo.save()
        return HttpResponse('1')
    else:
        return render(request, 'account/imagecrop.html')