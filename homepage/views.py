from django.shortcuts import render
from django.views.generic import View, TemplateView
from inventory.models import Stock

from transactions.models import SaleBill, PurchaseBill,SaleItem


class HomeView(View):
    template_name = "home.html"
    def get(self, request):        
        labels = []
        data = []        
        s = Stock.objects.filter(is_deleted=False).order_by('-quantity')
        for item in s:
            labels.append(item.name)
            data.append(item.quantity)
        sales = SaleBill.objects.order_by('-time')[:3]
        purchases = PurchaseBill.objects.order_by('-time')[:3]
        context = {
            'labels'    : labels,
            'data'      : data,
            'sales'     : sales,
            'purchases' : purchases
        }
        return render(request, self.template_name, context)

class AboutView(TemplateView):
    template_name = "about.html"

def ListView(request):
    stock = SaleItem.objects.all().filter()
    name = SaleBill.objects.all().filter()
    print(stock)
    print(name)
    mylist=zip(stock,name)
    job_view = {'mylist':mylist}
    return render(request, 'viewdetails.html', {'mylist':mylist})