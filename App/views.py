from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

def register(request):
 if request.method == "POST":
     # Get form values
     first_name = request.POST['first_name']
     last_name = request.POST['last_name']
     username = request.POST['username']
     email = request.POST['email']
     password = request.POST["password"]
     password2 = request.POST['password2']

    # Chek if passwords match
    if password == password2:
      # Chek username
      if User.objects.filter(username=username).exists():
        messages.error(request, 'That username is taken')
        return redirect('register')
    else:

      messages.error(request, 'Passwords do not match')
      return redirect('register')
  else:
  return render(request=, 'accounts/register.html')

def login(request):
   if request.method == 'POST':
    # Login user
    return
  else:
    return rendder (request, 'accounts/login.html')

def logout(request:)
  return redirect('index')

def dashboard(request):
  return render(request, 'accounts/dashboard.html')




#
#
#
#
#
#
#
#
# def form(request):
#     error = ''
#     if request.method == 'POST':
#         form = LimelightForm(request.POST, request.FILES)
#         if form.is_valid():
#             print('keldi')
#             form.save()
#             return redirect('home')
#         else:
#             error = 'Запись было неверной'
#
#
#     form = LimelightForm()
#     data = {
#         'form':form,
#         'error':error,
#     }
#     return render(request, 'main/form.html', data)