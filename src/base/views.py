from django.shortcuts import render 
from .models import Payment,Kid,Term
from django.contrib.auth.decorators import login_required as lr

@lr(login_url='login_page')
def index(request): 
	newest_payments = Payment.objects.all()[0:5]
	newest_daycare_kids = Kid.objects.filter(kid_class="Daycare")[0:4]
	newest_nursery_kids = Kid.objects.filter(kid_class="Nursery")[0:4]

	return render(request, 'base/site/index.html',{'payments':newest_payments,'daycare_kids':newest_daycare_kids,'nursery_kids': newest_nursery_kids})
