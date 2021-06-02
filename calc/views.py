from django.shortcuts import render

# Create your views here.
def addition_page(request):
    if request.method=="POST":
        num1 = request.POST.get("num1")
        num2 = request.POST.get("num2")
        res = int(num1) + int(num2)
        print(res)
        context={}
        context["total"]=res
        return render(request,"calc/addition.html",context)

    return render(request,"calc/addition.html")



def subtraction_page(request):
    if request.method=="POST":
        num1 = request.POST.get("num1")
        num2 = request.POST.get("num2")
        res = int(num1) - int(num2)
        print(res)
    return render(request,"calc/subtraction.html")



def multiplication_page(request):
    if request.method=="POST":
        num1 = request.POST.get("num1")
        num2 = request.POST.get("num2")
        res = int(num1) * int(num2)
        print(res)
    return render(request,"calc/multiplication.html")



def division_page(request):
    if request.method=="POST":
        num1 = request.POST.get("num1")
        num2 = request.POST.get("num2")
        res = int(num1) / int(num2)
        print(res)
    return render(request,"calc/division.html")



def index(request):
    return render(request,"calc/index.html")

