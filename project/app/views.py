from django.shortcuts import render
from app.models import Query as q
# Create your views here.
def landing(req):
    return render (req, 'landing.html')


def all(req):
    all_data = q.objects.all()
    print(all_data)
    return render (req, 'landing.html', {'data':all_data })


def filter1(req):
    data = q.objects.filter(Name='aayushi')
    print(data)
    return render (req, 'landing.html', {'data1':data})

def ascending(req):
    data = q.objects.order_by('Age')  #ascending
    # data = q.objects.order_by('-Age')  #dscending
    print(data)
    return render (req, 'landing.html', {'data2':data})

def mfilter(req):
    data = q.objects.filter(City='darbhanga',Age=21)
    print(data)
    return render (req, 'landing.html', {'data3':data})

def exclude1(req):
    data = q.objects.exclude(City='darbhanga')
    print(data)
    return render (req, 'landing.html', {'data4':data})


