from django.shortcuts import render
from mesmerEyesApp.models import *
from .forms import *
from .models import *
from accounts.decorators import unauthenticated_user


@unauthenticated_user
def Proceed_To_Checkout(request):
    total_amt=0
    if request.method == "POST":    
        form=OrderCreateForm(request.POST)
        if form.is_valid:
            order=form.save(commit=False)
            order.customer=request.user
            order.save()
            for p_id,item in request.session['cartdata'].items():
                total_amt+=int(item['qty'])*float(item['price'])
                product=Product.objects.get(id=int(p_id))
                OrderRow.objects.create(order=order,product=product,quantity=item['qty'],amount=item['price'])
            
            del request.session['cartdata']
        context={
            'amount':total_amt,
            'customer':request.user,
            'order':order,
            }
        return render(request,"customer/validatecheckout.html",context)

    else:
        form=OrderCreateForm()
        for p_id,item in request.session['cartdata'].items():
            total_amt+=int(item['qty'])*float(item['price'])
        context={
            'items':request.session['cartdata'],
            'total_amt':total_amt,
            'form':form
            }
        return render(request, 'customer/checkout.html',context)
