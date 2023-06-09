"""unclestans URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from resturant.views import upload_view, update_view, menu_item_detail
from main.views import Index, About, MenuView, Entree, cart_view, Order, AddToCartView, remove_from_cart, update_quantity

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name='index'),
    path('about/', About.as_view(), name='about'),
    path('menu/', MenuView.as_view(), name='menu'),
    path('order/', Order.as_view(), name='order'),
    path('entree/', Entree.as_view(), name='entree'),
    path('upload/', upload_view, name='upload_view'),
    path('add_cart', AddToCartView.as_view(), name='add_to_cart'),
    path('cart/', cart_view, name='cart'),
    path('update_quantity/', update_quantity, name='update_quantity'),
    path('removecart/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('update/<int:item_id>/', update_view, name='update_view'),
    path('item/<int:item_id>/', menu_item_detail, name='menu_item_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
