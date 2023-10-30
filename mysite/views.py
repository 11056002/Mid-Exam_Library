from django.shortcuts import render, redirect
from mysite.models import Book1, Publisher, Author

def homepage(request):
    selected_menu = request.GET.get('menu', 'book')  # 默認顯示書本
    if selected_menu == 'book':
        articles = Book1.objects.all()
    elif selected_menu == 'author':
        articles = Author.objects.all()
    elif selected_menu == 'publisher':
        articles = Publisher.objects.all()
    else:
        return redirect("/")  # 處理無效的MENU選項，直接重定向到首頁
    return render(request, 'index.html', {'selected_menu': selected_menu, 'articles': articles})

def showbook(request, book_name="None"):
    try:
        book = Book1.objects.get(name=book_name)
        return render(request, 'book.html', {'book': book})
    except Book1.DoesNotExist:
        return redirect("/")  # 書本不存在，重定向到首頁

def showauthor(request, author_name="None"):
    try:
        author = Author.objects.get(name=author_name)
        return render(request, 'author.html', {'author': author})
    except Author.DoesNotExist:
        return redirect("/")  # 作者不存在，重定向到首頁

def showpublisher(request, publisher_name="None"):
    try:
        publisher = Publisher.objects.get(name=publisher_name)
        return render(request, 'publisher.html', {'publisher': publisher})
    except Publisher.DoesNotExist:
        return redirect("/")  # 出版商不存在，重定向到首頁
