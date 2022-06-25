from django.shortcuts import render, redirect,get_object_or_404
from .forms import *
from .models import *
from django.views import View
from django.template.loader import render_to_string
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.http import JsonResponse
from .decorators import *
from mesmerEyesApp.forms import *
from Orders.models import *

def register(request):

    form=CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,'Account was created for'+username)
            return redirect('login')
    
    context={
        'form':form,
    }
    return render(request,'accounts/register.html',context)

def Login(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('IndexView')
            
    return render(request,'accounts/login.html')

def Logout(request):
    logout(request)
    return redirect('IndexView')

#Customer/Admin##########################################################################################################
@unauthenticated_user
def Index_customer(request):
	try:
		user=Customer.objects.get(user=request.user)
		order=Order.objects.filter(customer=request.user)
		if not order:
			context={
			'user':user,
			}
		else:
			for o in order:
				orders=OrderRow.objects.filter(order=o)
			nbrorder=orders.count()
			context={
				'user':user,
				'orders':orders,
				'nbrorder':nbrorder,
			}
			
		return render(request,'customer/index_customer.html',context)
	except Customer.DoesNotExist:
		return redirect('IndexView')

@unauthenticated_user
def Setting_customer(request):
	user=request.user.customer
	form=CustomerFormCustomer(instance=user)
	if request.method == 'POST':
		form=CustomerFormCustomer(request.POST, request.FILES, instance=user)
		if form.is_valid():
			form.save()
			return redirect('Index_customer')	

	return render(request,'customer/setting_user.html',{'form':form})

@unauthenticated_user 
def Index_admin(request):
	nbrprod=Product.objects.count()
	nbrbrand=Brand.objects.count()
	nbrcat=Categories.objects.count()
	nbrimg=Album_images.objects.count()
	nbradmin=Admin.objects.count()
	nbrorder=Order.objects.count()
	
	nbrcust=Customer.objects.count()
	context={
		'nbrprod':nbrprod,
		'nbrbrand':nbrbrand,
		'nbrcat':nbrcat,
		'nbrimg':nbrimg,
		'nbrcust':nbrcust,
		'nbradmin':nbradmin,
		'nbrorder':nbrorder
	}
	return render(request,'admin/index_admin.html',context) 

#Dashboard-Product#########################################################################################################
    
def Management_product(request):
	prod=Product.objects.all()
	
	context={
		'prod':prod
	}
	return render(request,'admin/manageproducts.html',context)


def save_all_prod(request,form,template_name):
	data = dict()
	if request.method == "POST":
		if form.is_valid():
			form.save()
			data['form_is_valid']=True
			prod=Product.objects.all()
			data['Management_product'] = render_to_string('admin/manageproducts.html',{'prod':prod})
	else:
		data['form_is_valid']=False
	
	context={
		'form': form
	}
	data['html_form'] = render_to_string(template_name,context,request)
	return JsonResponse(data)

def Management_addproduct(request):
	if request.method == "POST":
		form = ProductForm(data=request.POST,files=request.FILES)
	if request.method == "GET":
		form = ProductForm()
	return save_all_prod(request,form,'admin/manageaddprod.html')


def Management_updateproduct(request,product_id):
	prod = get_object_or_404(Product , pk=product_id )
	if request.method == 'POST':
		form = ProductForm(request.POST,request.FILES,instance=prod)
	else:
		form = ProductForm(instance=prod)
	return save_all_prod(request,form,'admin/manageupdateprod.html')


def Management_deleteproduct(request,product_id):
	data = dict()
	prod = get_object_or_404(Product , pk=product_id )
	if request.method == 'POST':
		prod.delete()
		data['form_is_valid']=True
		prod=Product.objects.all()
		data['Management_product'] = render_to_string('admin/manageproducts.html',{'prod':prod})
	else:
		context={
		'prod':prod
		}
		data['html_form'] = render_to_string('admin/managedeleteprod.html',context,request=request)
	return JsonResponse(data)

#Category#########################################################################################################################


def Management_category(request):
	cat=Categories.objects.all()
	context={
		'cat':cat
	}
	return render(request,'admin/managecategory.html',context)


def save_all_cat(request,form,template_name):
	data = dict()
	if form.is_valid():
		form.save()
		data['form_is_valid']=True
		cat=Categories.objects.all()
		data['Management_category'] = render_to_string('admin/managecategory.html',{'cat':cat})
	else:
		data['form_is_valid']=False
		
	context={
		'form': form
	}
	
	data['html_form'] = render_to_string(template_name,context,request=request)
	return JsonResponse(data)

def Management_addcategory(request):
	if request.method == 'POST':
		form = CategoriesForm(request.POST)
	else:
		form = CategoriesForm()
	return save_all_cat(request,form,'admin/manageaddcat.html')


def Management_updatecategory(request,cat_id):
	cat = get_object_or_404(Categories,pk=cat_id )
	if request.method == 'POST':
		form = CategoriesForm(request.POST,instance=cat)
	else:
		form = CategoriesForm(instance=cat)
	return save_all_cat(request,form,'admin/manageupdatecat.html')


def Management_deletecategory(request,cat_id):
	data = dict()
	cat = get_object_or_404(Categories,pk=cat_id)
	if request.method == 'POST':
		cat.delete()
		data['form_is_valid']=True
		cat=Categories.objects.all()
		data['Management_category'] = render_to_string('admin/managecategory.html',{'cat':cat})
	else:
		context={
		'cat':cat
		}
		data['html_form'] = render_to_string('admin/managedeletecat.html',context,request=request)
	return JsonResponse(data)


#Brand#########################################################################################################################

def Management_brand(request):
	gam=Brand.objects.all()
	
	context={
		'gam': gam
	}
	return render(request,'admin/managebrand.html',context)


def save_all_brand(request,form,template_name):
	data = dict()
	if form.is_valid():
		form.save()
		data['form_is_valid']=True
		gam=Brand.objects.all()
		data['Management_brand'] = render_to_string('admin/managebrand.html',{'gam': gam})
	else:
		data['form_is_valid']=False
		
	context={
		'form': form
	}
	
	data['html_form'] = render_to_string(template_name,context,request=request)
	return JsonResponse(data)


def Management_addbrand(request):
	if request.method == 'POST':
		form = BrandForm(request.POST,request.FILES)
	else:
		form = BrandForm()
	return save_all_brand(request,form,'admin/manageaddbrand.html')


def Management_updatebrand(request,brand_id):
	gam = get_object_or_404(Brand , pk=brand_id )
	if request.method == 'POST':
		form = BrandForm(request.POST,request.FILES,instance=gam)
	else:
		form = BrandForm(instance=gam)
	return save_all_brand(request,form,'admin/manageupdatebrand.html')

def Management_deletebrand(request,brand_id):
	data = dict()
	gam = get_object_or_404(Brand , pk=brand_id )
	if request.method == 'POST':
		gam.delete()
		data['form_is_valid']=True
		gam=Brand.objects.all()
		data['Management_brand'] = render_to_string('admin/managebrand.html',{'gam': gam})
	else:
		context={
			'gam': gam
		}
		data['html_form'] = render_to_string('admin/managedeletebrand.html',context,request=request)
	return JsonResponse(data)

#Image#########################################################################################################################

def Management_image(request):
	img=Album_images.objects.all()
	context={
		'img': img
	}
	return render(request,'admin/manageimage.html',context)


def save_all_images(request,form,template_name):
	data = dict()
	if form.is_valid():
		form.save()
		data['form_is_valid']=True
		images=Album_images.objects.all()
		data['Management_image'] = render_to_string('admin/manageimage.html',{'img': images})
		print("test1")
	else:
		data['form_is_valid']=False
		print("test2")
	
	data['html_form'] = render_to_string(template_name,{'form': form},request=request)
	return JsonResponse(data)


def Management_addimg(request):
	if request.method == "POST":
		form = ImageForm(request.POST,request.FILES)
	if request.method == "GET":
		form = ImageForm()

	return save_all_images(request,form,'admin/manageaddimg.html')


def Management_updateimg(request,img_id):
	img = get_object_or_404(Album_images , pk=img_id )
	if request.method == 'POST':
		form = ImageForm(request.POST,request.FILES,instance=img)
	else:
		form = ImageForm(instance=img)
	return save_all_images(request,form,'admin/manageupdateimg.html')


def Management_deleteimg(request,img_id):
	data = dict()
	img = get_object_or_404(Album_images , pk=img_id )
	if request.method == 'POST':
		img.delete()
		data['form_is_valid']=True
		img=Album_images.objects.all()
		data['Management_image'] = render_to_string('admin/manageimage.html',{'img': img})
	else:
		context={
			'img': img
		}
		data['html_form'] = render_to_string('admin/managedeleteimg.html',context,request=request)
	return JsonResponse(data)

#customers#########################################################################################################################
def Management_customer(request):
	cust=Customer.objects.all()
	context={
		'cust':cust
	}
	return render(request,'admin/managecustomers.html',context)

#orders#########################################################################################################################
def Management_orders(request):
	orders=Order.objects.all()
	context={
		'orders': orders
	}
	return render(request,'admin/manageorders.html',context)

#admin#########################################################################################################################
def Management_admin(request):
	admin=Admin.objects.all()
	context={
		'admin':admin
	}
	return render(request,'admin/manageadmin.html',context)

def save_all_admin(request,form,template_name):
	data = dict()
	if form.is_valid():
		form.save()
		data['form_is_valid']=True
		admin=Admin.objects.all()
		data['Management_admin'] = render_to_string('admin/manageadmin.html',{'admin':admin})
	else:
		data['form_is_valid']=False
		
	context={
		'form': form
	}
	
	data['html_form'] = render_to_string(template_name,context,request=request)
	return JsonResponse(data)

def Management_updateadmin(request,admin_id):
	admin = get_object_or_404(Admin , pk=admin_id )
	if request.method == 'POST':
		form = AdminForm(request.POST,request.FILES,instance=admin)
	else:
		form = AdminForm(instance=admin)
	return save_all_admin(request,form,'admin/manageupdateadmin.html')

def Management_deleteadmin(request,admin_id):
	data = dict()
	admin = get_object_or_404(Admin , pk=admin_id )
	if request.method == 'POST':
		admin.delete()
		data['form_is_valid']=True
		admin=Admin.objects.all()
		data['Management_admin'] = render_to_string('admin/manageadmin.html',{'admin':admin})
	else:
		context={
			'admin':admin
		}
		data['html_form'] = render_to_string('admin/managedeleteadmin.html',context,request=request)
	return JsonResponse(data)








"""
@admin_only
def Management_customer(request):
	cust=Customer.objects.all()
	context={
		'cust':cust
	}
	return render(request,'admin/managecustomers.html',context)

@admin_only
def save_all(request,form,template_name):
	data = dict()
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			data['form_is_valid']=True
			cust=Customer.objects.all()
			data['Management_customer'] = render_to_string('admin/managecustomers.html',{'cust':cust})
		else:
			data['form_is_valid']=False
		
	context={
		'form': form
	}
	
	data['html_form'] = render_to_string(template_name,context,request=request)
	return JsonResponse(data)

@admin_only
def Management_addcust(request):
	if request.method == 'POST':
		form = CustomerForm(request.POST)
	else:
		form = CustomerForm()
	return save_all(request,form,'admin/manageaddcust.html')

@admin_only
def Management_updatecust(request,cust_id):
	cat = get_object_or_404(Customer,pk=cat_id )
	if request.method == 'POST':
		form = CustomerForm(request.POST,instance=cust)
	else:
		form = CustomerForm(instance=cust)
	return save_all(request,form,'admin/manageupdatecust.html')

@admin_only
def Management_deletecust(request,cust_id):
	data = dict()
	cat = get_object_or_404(Customer,pk=cust_id )
	if request.method == 'POST':
		cust.delete()
		data['form_is_valid']=True
		cust=Customer.objects.all()
		data['Management_customer'] = render_to_string('admin/managecustomer.html',{'cust':cust})
	else:
		context={
		'cust':cust
		}
		data['html_form'] = render_to_string('admin/managedeletecust.html',context,request=request)
	return JsonResponse(data)
"""