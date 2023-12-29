from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import View
from django.http import HttpResponse,JsonResponse
from django.db.models import Q
from .models import UploadFileModel,FashionRetailSales
from .forms import FileForm
import pandas as pd
# Create your views here.

def import_data_from_csv(csv_file_path):
    # خواندن فایل CSV
    df = pd.read_csv(csv_file_path)

    # تبدیل DataFrame به لیست از دیکشنری‌ها
    data = df.to_dict(orient='records')

    # افزودن اطلاعات به دیتابیس
    # FashionRetailSales.objects.bulk_create([FashionRetailSales(**entry) for entry in data])
    for i in range(0, len(data)):
        d = data[i].items()
        for k,v in d:
            if k=='Customer Reference ID':
                obj = FashionRetailSales.objects.create(Customer=v)
            elif k=='Item Purchased':
                obj.item = v
            elif k=='Purchase Amount (USD)':
                print(type(v))
                print(v)
                if v is None or v==' ' or v=='nan':
                    v = 0
                    obj.amount = v
                else:
                    obj.amount = v
            elif k=='Date Purchase':
                obj.date_purchased = v
            elif k=='Review Rating':
                obj.Review_Rating = v
            elif k=='Payment Method':
                obj.Payment_Method = v
        obj.save()
        
                

class HomeView(View):
    def get(self, request, *args, **kwargs):
        data = FashionRetailSales.objects.all()
        quantity = data.count()
        return render(request,'home/home.html',{'form':FileForm(),'data':data,'quantity':quantity})
    

def upload_file(request):
    if request.method == 'POST':
        file = request.FILES.get('file')
        obj = UploadFileModel.objects.create(file=file)
        
        import_data_from_csv(obj.path())
        return HttpResponse('با موفقیت آپلود شد')
        
class AddNewItemView(View):
    
    def post(self, request):
        id_customer = request.POST.get('id')
        item = request.POST.get('item')
        amount = request.POST.get('amount')
        date = request.POST.get('date')
        rating = request.POST.get('review')
        payment = request.POST.get('payment')
        FashionRetailSales.objects.create(
            Customer = id_customer,
            item = item,
            amount = amount,
            date_purchased = date,
            Review_Rating = rating,
            Payment_Method = payment,
        )
        return redirect('/')

class SearchView(View):
    
    def get(self, request):
        q = request.GET.get('q')
        result = FashionRetailSales.objects.filter(
            Q(item__icontains=q)|
            Q(Customer__icontains=q)|
            Q(Payment_Method__icontains=q))
        quantity = result.count()
        return render(request,'home/home.html',{'data':result,'quantity':quantity})
    
def delete_item(request,pk):
    print(request.method)
    item = get_object_or_404(FashionRetailSales,pk=pk)
    item.delete()
    return JsonResponse({'response': 'succes delete item' })


def update_item(request,pk):
    if request.method == 'GET':
        instance = get_object_or_404(FashionRetailSales,pk=pk)
        return render(request,'home/updatedata.html',{'obj':instance})
    instance = get_object_or_404(FashionRetailSales,pk=pk)
    id_customer = request.POST.get('id')
    item = request.POST.get('item')
    amount = request.POST.get('amount')
    date = request.POST.get('date')
    rating = request.POST.get('review')
    payment = request.POST.get('payment')
    instance.Customer = id_customer
    instance.item = item
    instance.amount = amount
    instance.date_purchased = date
    instance.Review_Rating = rating
    instance.Payment_Method = payment
    instance.save()
    return redirect('/')