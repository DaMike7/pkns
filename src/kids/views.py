from django.db.models import Sum
from django.shortcuts import render,redirect
from base.models import Kid,Term,Payment
from django.shortcuts import get_object_or_404 as go4
from .forms import KidForm as kf
from .forms import PaymentForm as pf
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required as lr
from .filters import KidFilter,PaymentFilter



# Create your views here.

app_name = 'kids'

#USER ACTIONS
def userLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        
        else:
            messages.info(request,'Incorrect Username Or Password')
    context = {}
    return render(request,'base/site/login.html',context)

# KIDS VIEWS
@lr(login_url='login_page')
def kidsList(request):
    daycare_kids = Kid.objects.filter(kid_class="Daycare")
    nursery_kids = Kid.objects.filter(kid_class="Nursery")
    KF = KidFilter(request.GET,queryset=nursery_kids)
    nursery_kids = KF.qs

    return render(request,'kids/kid_list.html',{'daycare_kids':daycare_kids,'nursery_kids':nursery_kids,'kf':KF})

@lr(login_url='login_page')
def userLogout(request):
    logout(request)
    return redirect('login_page')

@lr(login_url='login_page')
def kidDetail(request,handle=None):
    url_queryset = go4(Kid,handle=handle)
    all_payments = Payment.objects.filter(kid = url_queryset)
    kid_url = {
        'kid_url': url_queryset,
        'all_payments': all_payments,
        }
    return render(request,'kids/kid_details.html',kid_url)

"""def deleteKid(request,kid_id):
    kid = go4(Kid,id=kid_id)
    if request.method == "POST":
        kid.delete()

        return redirect('kids_list')

    return render(request,'kids/delete_kid.html',{'kid':kid})"""

@lr(login_url='login_page')
def registerKid(request):
    form = kf()
    if request.method == 'POST':
        form = kf(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('kids_list')
        else:
            form.add_error('Invalid or Incorrect data')
    return render(request,'kids/register_form.html',{'form':form})


#TERM VIEWS
@lr(login_url='login_page')
def termList(request):
    terms = Term.objects.all()
    return render(request,'kids/term/term_list.html',{'terms':terms})

@lr(login_url='login_page')
def termDetail(request, handle=None):
    term = go4(Term, handle=handle)
    kids_in_term = Kid.objects.filter(term=term)
    total_kids = kids_in_term.count()

    all_payments = Payment.objects.filter(kid__in=kids_in_term)
    total_payments = all_payments.aggregate(Sum('amount'))['amount__sum'] or 0

    context = {
        'term_url': term,
        'total_kids': total_kids,
        'total_payments': total_payments,
        'kids_in_term': kids_in_term,
        'all_payments': all_payments,
    }

    return render(request, 'kids/term/term_details.html', context)



#PAYMENT VIEWS
@lr(login_url='login_page')
def paymentList(request):
    payments = Payment.objects.all()
    PF = PaymentFilter(request.GET,queryset=payments)
    payments = PF.qs

    return render(request,'kids/payment/payment_list.html',{'payments':payments,'pf':PF})


@lr(login_url='login_page')
def paymentDetail(request,handle=None):
    url_queryset = go4(Payment,handle=handle)
    payment_url = {'payment_url':url_queryset}
    return render(request,'kids/payment/payment_details.html',payment_url)

@lr(login_url='login_page')
def addPayment(request):
    form = pf()
    if request.method == 'POST':
        form = pf(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment_list')
        else:
            form.add_error('Invalid or Incorrect data')
    return render(request,'kids/payment/new_payment.html',{'form':form})
