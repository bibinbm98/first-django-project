from django.shortcuts import render

def create_book(request):
    return render(request,"bookapp/create_book.html")

def list_all_book(request):
    return render(request,"bookapp/listallbook.html")

def update_book(request):
    return render(request,"bookapp/editbook.html")

def delete_book(request):
    return render(request,"bookapp/deletebook.html")

def index(request):
    return render(request,"bookapp/index.html")


def message(request):
    return render(request,"bookapp/message.html")

def fetch_data(request):
    bookname=request.POST.get("bookname")
    author=request.POST.get("author")
    price=request.POST.get("price")
    pages=request.POST.get("pages")
    print(bookname,author,price,pages)
    return render(request,"bookapp/create_book.html")

