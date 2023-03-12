from django.urls import path
from app import views
from .views import Index
from .views import Signup

from .views import Cart
from .views import Checkout

urlpatterns = [
    path('',Index.as_view(),name='index'),
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('logout',views.logout,name='logout'),
    path('cart',Cart.as_view(),name='cart'),
    path('checkout',Checkout.as_view(),name="checkout")
]