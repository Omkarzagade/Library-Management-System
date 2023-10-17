from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
# Create your views here.
from .models import *
import requests
from datetime import date

def home(request):
    return render(request, 'home.html')


def singlebook(request, title, stock):
    page_number = 1
    url = f"https://frappe.io/api/method/frappe-library?page={page_number}&title={title}"
    resp= requests.get(url).json()['message'][0]
    Book.objects.create(title=title, authors= resp['authors'], isbn= resp['isbn'], publisher= resp['publisher'], pages= resp['  num_pages'], stock= stock).save()
    return None

def ImportBook(request):
    if request.method=='POST':
        val = request.POST.getlist('bb')
        qty = int(request.POST.get('cc'))
        for title in val:
            try:
                book_obj= Book.objects.get(title = title)
                book_obj.stock += qty
                book_obj.save()
            except:
                singlebook(request, title, qty)
    page_number = 1
    url = f"https://frappe.io/api/method/frappe-library?page={page_number}"
    resp= requests.get(url).json()
    books = resp['message']
    titles = [book['title'] for book in books]
    return render(request, 'import.html', locals())

def searchbook(request):
    if request.method=='POST':
        search=request.POST.get('aa')
        data= Book.objects.filter(title__icontains = search) | Book.objects.filter(authors__contains = search)
    else:
        data= Book.objects.all()
    return render(request, 'books.html', {'data':data})

def issuebook(request, id):
    book=Book.objects.get(id=id)
    members = Member.objects.all()

    if request.method == 'POST':
        m = request.POST.get('member')
        book.stock -= 1
        book.save()
        m= Member.objects.get(name = m)
        Transaction.objects.create(book = book, member = m).save()
        return HttpResponseRedirect('/search/')

    return render(request, 'bookissue.html', locals())

def returnbook(request):
    books = Book.objects.all()
    members = Member.objects.all()
    if request.method == 'POST':
        b = request.POST.get('book')
        m = request.POST.get('member')
        p = request.POST.get('r')
        book = Book.objects.get(title = b)
        book.stock += 1
        book.save()
        member = Member.objects.get(name = m)
        t = Transaction.objects.filter(book = book, member = member).first()
        t.return_date = date.today()
        fee = ((date.today() - t.issue_date).days + 1)*10
        t.rent_fee = fee
        if p == 'n':
            member.outstanding_debt += fee
        else:
            t.is_paid = True
        member.save()
        t.save()

    return render(request, 'return.html', locals())