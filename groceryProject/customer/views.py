from django.shortcuts import render

from .models import Customer_Detail


# Create your views here.

def index(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        number = request.POST.get('number')
        product = request.POST.get('product')
        place = request.POST.get('place')

        p = Customer_Detail(name=name, number=number,product = product,place =place)
        p.save()

        return render(request, 'customer/index.html', {'message': 'Your query is added'})

    else:
        return render(request, 'customer/index.html')


def show(request):
    names = Customer_Detail.objects.all()

    return render(request, 'customer/show.html', {'names': names})