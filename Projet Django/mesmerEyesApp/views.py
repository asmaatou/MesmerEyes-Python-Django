from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.views import View
from django.template.loader import render_to_string
from .models import Album_images, Categories,Brand,Product
import random


def search(request):
    brand="None"
    type=request.GET.get('type')
    if not type:
        product = Product.objects.all()
    else:
        product = Product.objects.filter(Name_prod__icontains=type)
    if not product:
        product = Product.objects.filter(id_ga__Name_gam__icontains=type)
       

    nbr=product.count()
    p= Paginator(product,6)
    page = request.GET.get('page')
       
    try:
        result = p.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        result = p.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        result = p.page(p.num_pages)

    context={
        'product': product,
        'type': type,
        'nbr':nbr,
        'brand':brand,
        'paginate': True
    }
    return render(request, 'store/shop.html', context)

class IndexView(View):
    def get(self,request):
        products=Product.objects.all()[:3]
        return render(request,'store/index.html',{'product':products})

class AboutView(View):
    def get(self,request):
        return render(request,'store/about.html')

class ProductsView(View):
    def get(self,request,type):
        brand="None"
        
        if type=="All products":
            product=Product.objects.all()
            
        elif type=="Eyeglasses" or type=="Sunglasses":
            product=Product.objects.filter(id_cat=Categories.objects.get(Name_cat=type))

        elif type=="RAY-BAN" or type=="OAKLEY" or type=="RFLKT" or type=="5 TO SEE" or type=="MesmerEyes":
            product=Product.objects.filter(id_ga=Brand.objects.get(Name_gam=type))
            brand=Brand.objects.get(Name_gam=Brand.objects.get(Name_gam=type))
        elif type=="SALE":
            product=Product.objects.filter(is_sale=True)
        elif type=="M" or type=="W" or type=="BOTH":
            if type == "BOTH":
                product=Product.objects.filter(Gender="M/W")
            else:
                product=Product.objects.filter(Gender=type)
        
        nbr=product.count()
        p= Paginator(product,6)
        page = request.GET.get('page')
       
        try:
            result = p.page(page)
        except PageNotAnInteger:
        # If page is not an integer, deliver first page.
            result = p.page(1)
        except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
            result = p.page(p.num_pages)

        if not product:
            return  render(request,'store/shop.html',{'nbr':nbr,'brand':brand})
        
        
        context={
            'product':result,
            'type':type,
            'nbr':nbr,
            'brand':brand,
            'paginate': True
        }
        return render(request,'store/shop.html',context)

        

class ContactView(View):
    def get(self,request):
        return render(request,'store/contact.html')


class ProductDetailView(View):
    def get(self,request,product_id):
        product=Product.objects.get(pk=product_id)
        image=Album_images.objects.filter(id_product=product.pk)
        categorie=Categories.objects.get(Name_cat=product.id_cat)
        randomnumber=random.randint(1, Product.objects.count()-4)
        context={
            'product':product,
            'image2':image[0],
            'image3':image[1],
            'categorie':categorie,
            'relatedprod':Product.objects.all()[randomnumber:randomnumber+4]
        }
        return render(request,'store/shop-details.html',context)

class addTocart(View):
    def get(self,request):
        
        cart_p={}
        cart_p[str(request.GET['id'])]={
		    'image':request.GET['image'],
		    'title':request.GET['title'],
		    'qty':request.GET['qty'],
		    'price':request.GET['price'],
	    }
        if 'cartdata' in request.session:
            if str(request.GET['id']) in request.session['cartdata']:
                cart_data=request.session['cartdata']
                cart_data[str(request.GET['id'])]['qty']=int(cart_p[str(request.GET['id'])]['qty'])
                cart_data[str(request.GET['id'])]['price']=float(cart_p[str(request.GET['id'])]['price'])
                cart_data.update(cart_data)
                request.session['cartdata']=cart_data
            else:
                cart_data=request.session['cartdata']
                cart_data.update(cart_p)
                request.session['cartdata']=cart_data
        else:
            request.session['cartdata']=cart_p
        return JsonResponse({'data':request.session['cartdata'],'totalitems':len(request.session['cartdata'])})

class ShoppingCartDetail(View):
    def get(self,request):
        total_amt=0
        try:
            for p_id,item in request.session['cartdata'].items():
                total_amt+=int(item['qty'])*float(item['price'])
            context={
                'items':request.session['cartdata'],
                'totalitems':len(request.session['cartdata']),
                'total_amt':total_amt,
            }
            return render(request, 'store/shopping-cart.html',context)
        except KeyError:
            return render(request, 'store/shopping-cart.html',{'total_amt':total_amt,'totalitems':0})

# Delete cart
def delete_cart_item(request):
	p_id=str(request.GET['id'])
	if 'cartdata' in request.session:
		if p_id in request.session['cartdata']:
			cart_data=request.session['cartdata']
			del request.session['cartdata'][p_id]
			request.session['cartdata']=cart_data
	total_amt=0
	for p_id,item in request.session['cartdata'].items():
		total_amt+=int(item['qty'])*float(item['price'])
	t=render_to_string('ajax/cart-list.html',{'cart_data':request.session['cartdata'],'totalitems':len(request.session['cartdata']),'total_amt':total_amt})
	return JsonResponse({'data':t,'totalitems':len(request.session['cartdata'])})

# Update cart

def update_cart_item(request):
	p_id=str(request.GET['id'])
	p_qty=request.GET['qty']
	if 'cartdata' in request.session:
		if p_id in request.session['cartdata']:
			cart_data=request.session['cartdata']
			cart_data[str(request.GET['id'])]['qty']=p_qty
			request.session['cartdata']=cart_data
	total_amt=0
	for p_id,item in request.session['cartdata'].items():
		total_amt+=int(item['qty'])*float(item['price'])
	t=render_to_string('ajax/cart-list.html',{'cart_data':request.session['cartdata'],'totalitems':len(request.session['cartdata']),'total_amt':total_amt})
	return JsonResponse({'data':t,'totalitems':len(request.session['cartdata'])})