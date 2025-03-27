from django.shortcuts import render, redirect

from .forms import createuserform
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def loginpage(request):
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username , password=password)
        
        if user is not None:
            login(request , user)
            return redirect('main')
        else:
            messages.info(request , 'username or password or both is incorrect')
    
    context = {}
    return render(request , 'auth_page/login.html', context)

def signuppage(request):
    # username = request.POST.get('username')
    # email = request.POST.get('email')
    # password = request.POST.get('password')
    # if request.method == "POST":
    #     data = SignupForm(username=username , email=email , password=password)
    #     data.save() 
    form = createuserform()
    context = {'form' : form}
    
    if request.method == 'POST':
        form = createuserform(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('username')
            messages.success(request , f'the account has been created {name}!')
            return redirect("login")
        elif not form.is_valid():
            messages.info(request , 'there is an error in your data!')
      
    
    return render(request , 'auth_page/signup.html' , context)
@login_required
def logoutUser(request):
    logout(request)
    return redirect('login')
    

