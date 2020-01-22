from django.urls import path
from ecommerce import views
from .views import (
    ItemDetailView,
    CheckoutView,
    HomeView,
    register,
    OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    PaymentView,
    AddCouponView,
    RequestRefundView,
    login_view,register,logout_view
)

app_name = 'ecommerce'

urlpatterns = [
    path('register/$', register, name='register'),
    path('login/$', login_view, name='login'),
    path('logout/$', logout_view),


    path('', HomeView.as_view(), name='home'),
    path('vendor/profile/', views.vendorprofile, name='vendorprofile'),
    path('log/', views.log, name='log'),
    path('forgot-password/', views.forget, name='forgot'),
    path('signin/', views.loginpage, name='loginpage'),
    path('profile/', views.profile, name='profile'),
    path('index-profile/', views.index, name='profile-home'),
    path('logout/', views.logout, name='logout'),
    path('registration/', views.register, name='registration'),
    path('shop/buy-product/', views.shop, name = 'shop'),
    #path('login/', views.login, name='login'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund')
]
