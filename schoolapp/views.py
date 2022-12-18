from django.shortcuts import render

def front(request):
    return render(request,'base.html')
def loginpage(request):
    return render(request,'login.html')