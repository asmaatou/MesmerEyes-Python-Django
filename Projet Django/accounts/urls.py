from django.urls import path
from . import views

urlpatterns = [

    path('login/',views.Login,name='login'),
    path('register/',views.register,name='register'),
    path('Logout/',views.Logout,name='Logout'),

    ##########################################################################################################################
    
    path('Profil/',views.Index_customer,name="Index_customer"),
    path('Setting/',views.Setting_customer,name="Setting_customer"),
    path('Admin/',views.Index_admin,name="Index_admin"),
    

    ##########################################################################################################################

    path('Manageprod/',views.Management_product,name="Management_product"),
    path('Manageprod/Addprod/',views.Management_addproduct,name="Management_addproduct"),
    path('Manageprod/Updateprod/<int:product_id>',views.Management_updateproduct,name="Management_updateproduct"),
    path('Manageprod/Deleteprod/<int:product_id>',views.Management_deleteproduct,name="Management_deleteproduct"),

    ##########################################################################################################################

    path('Managecat/',views.Management_category,name="Management_category"),
    path('Managecat/Addcat/',views.Management_addcategory,name="Management_addcategory"),
    path('Managecat/Updatecat/<int:cat_id>',views.Management_updatecategory,name="Management_updatecategory"),
    path('Managecat/Deletecat/<int:cat_id>',views.Management_deletecategory,name="Management_deletecategory"),

    ##########################################################################################################################

    path('Managebrand/',views.Management_brand,name="Management_brand"),
    path('Managebrand/Addbrand/',views.Management_addbrand,name="Management_addbrand"),
    path('Managebrand/Updatebrand/<int:brand_id>',views.Management_updatebrand,name="Management_updatebrand"),
    path('Managebrand/Deletebrand/<int:brand_id>',views.Management_deletebrand,name="Management_deletebrand"),

    ##########################################################################################################################
    
    path('Managepicture/',views.Management_image,name="Management_image"),
    path('Managepicture/Addimage/',views.Management_addimg,name="Management_addimg"),
    path('Managepicture/Updateimage/<int:img_id>',views.Management_updateimg,name="Management_updateimg"),
    path('Managepicture/Deleteimage/<int:img_id>',views.Management_deleteimg,name="Management_deleteimg"),

    ##########################################################################################################################

    path('ManageOrders/',views.Management_orders,name="Management_orders"),

    ##########################################################################################################################

    path('Managecustomer/',views.Management_customer,name="Management_customer"),

    ##########################################################################################################################

    path('Manageadmin/',views.Management_admin,name="Management_admin"),
    path('Manageadmin/Updateadmin/<int:admin_id>',views.Management_updateadmin,name="Management_updateadmin"),
    path('Manageadmin/Deleteadmin/<int:admin_id>',views.Management_deleteadmin,name="Management_deleteadmin"),

]
