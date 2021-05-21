"""online_videogames_store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from main import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', views.BaseView, name='Base'),
    path('Create_user/', views.Create_user, name='Create_user'),
    path('Login_user/', views.Login_user, name='Login_user'),
    path('Logout_user/', views.Logout_user, name='Logout_user'),
    path('User_Details/', views.User_Details, name='User_Details'),
    path('Product_details/<int:product_id>', views.Product_details, name='Product_details'),
    path('Games/<int:platform_id>/<int:genre_id>', views.GamesView, name='Games'),
    path('Consoles/', views.ConsolesView, name='Consoles'),
    path('Add_to_cart/<int:product_id>', views.Add_to_cart, name='Add_to_cart'),
    path('Del_from_cart/<int:product_id>', views.Del_from_cart, name='Del_from_cart'),
    path('Cart/', views.CartView, name='CartView'),
    path('Add_to_fav/<int:product_id>', views.Add_to_fav, name='Add_to_fav'),
    path('Del_from_fav/<int:product_id>', views.Del_from_fav, name='Del_from_fav'),
    path('Favorites/', views.FavView, name='FavView'),
    path('Orders/', views.OrdersView, name='OrdersView'),
    path('Order_Details/<int:order_id>', views.Order_Details, name='Order_Details'),
    path('ContactView/', views.ContactView, name='ContactView'),
    path('InfoView/', views.InfoView, name='InfoView'),
    path('Search/', views.Search, name='Search'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

