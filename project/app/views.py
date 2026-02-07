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
    data = q.objects.exclude(City='Samstipur')
    print(data)
    return render (req, 'landing.html', {'data4':data})


def b_create(req):
    # data = q.objects.bulk_create([q(obj1), q(obj2), q(obj3)])
    data = q.objects.bulk_create([q(Name="Chandan", Email='chandan678@gmail.com', Age =16, City='Laheriashary') , q(Name="Kunadan", Email='kunadan678@gmail.com', Age =17, City='Samstipur'), q(Name="Saurabh", Email='Saurabh678@gmail.com', Age =22, City='Aara'),q(Name="Anuj", Email='anuj678@gmail.com', Age =23, City='Champaran'),q(Name="Adarsh", Email='adrash678@gmail.com', Age =24, City='Muzzafarpur'),q(Name="Anish", Email='anish678@gmail.com', Age =25, City='Bhojpur')])
    all_data = q.objects.all()
    return render (req, 'landing.html', {'data':all_data })

def m_delete(req):
    num = req.POST.get('number')
    print(num)
    num= num.split(',')
    print(num)
    for i in num:
        data = q.objects.get(id = int(i))
        data.delete()
    all_data = q.objects.all()
    return render (req, 'landing.html', {'data':all_data })
