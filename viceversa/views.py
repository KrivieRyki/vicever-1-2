from django.shortcuts import render

def home(request):
    return render(request,"home.html")

def reverse(request):
    text=request.GET["usertext"]
    rever_text=text[::-1]
    return render(request,"reverse.html",{'usertext':rever_text})