from django.shortcuts import render, redirect
from .models import Product, Categories, DeliveryType, Genres, Languages, Payments, Platforms, Order, OrderStatus, \
    Favorites, Profile, AuthUser, LastSearch
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.db.models import Max
from datetime import datetime, date, time
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Sum
import re


# Create your views here.
# Базовая страница
def BaseView(request):
    cart = Order.objects.filter(status=1, user_id=request.user.id)
    favorites = Favorites.objects.filter(user_id=request.user.id)
    return render(request, 'Base.html', {'user': request.user, 'cart': cart, 'favorites': favorites})


# Страница регистрации пользователя
def Create_user(request):
    error = False
    cart = Order.objects.filter(status=1, user_id=request.user.id)
    favorites = Favorites.objects.filter(user_id=request.user.id)
    if request.method == 'POST':
        username = request.POST.get('login')
        password = request.POST.get('password')
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        adress = request.POST.get('adress')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        if User.objects.filter(username=username).count() == 0:
            c_user = User.objects.create(
                username=username,
                password=password,
                email=email,
                first_name=f_name,
                last_name=l_name,
                is_superuser=0,
                is_staff=0,
                is_active=1,
                date_joined=datetime.now()
            )
            c_user.set_password(password)
            c_user.save()
            pr = Profile.objects.get(user_id=c_user.id)
            pr.adress = adress
            pr.phone_number = phone_number
            pr.save()
            auth = authenticate(request, username=username, password=password)
            login(request, auth)
            return render(request, 'Base.html',
                          {'error': error, 'user': c_user, 'cart': cart, 'favorites': favorites, })
        else:
            error = True
    return render(request, 'Create_user.html', {'error': error, 'cart': cart, 'favorites': favorites, })


# Страница входа пользователя
def Login_user(request):
    error = False
    cart = Order.objects.filter(status=1, user_id=request.user.id)
    favorites = Favorites.objects.filter(user_id=request.user.id)
    if request.method == 'POST':
        username = request.POST.get('login')
        password = request.POST.get('password')
        auth = authenticate(request, username=username, password=password)
        c_user = User.objects.get(username=username)
        if auth is not None:
            login(request, auth)
            return render(request, 'Base.html',
                          {'error': error, 'user': c_user, 'cart': cart, 'favorites': favorites, })
        else:
            error = True
    return render(request, 'Login_user.html', {'error': error, 'cart': cart, 'favorites': favorites, })


# Функция логаута пользователя
def Logout_user(request):
    cart = Order.objects.filter(status=1, user_id=request.user.id)
    favorites = Favorites.objects.filter(user_id=request.user.id)
    logout(request)
    return render(request, 'Base.html', {'cart': cart, 'favorites': favorites, })


# Страница деталей и редактирвоания профайла пользователя
def User_Details(request):
    profile = Profile.objects.get(user_id=request.user.id)
    cart = Order.objects.filter(status=1, user_id=request.user.id)
    favorites = Favorites.objects.filter(user_id=request.user.id)
    if request.method == 'POST':
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        adress = request.POST.get('adress')
        phone_number = request.POST.get('phone_number')
        change = User.objects.get(username=request.user.username)
        change.first_name = f_name
        change.last_name = l_name
        profile.adress = adress
        profile.phone_number = phone_number
        change.save()
        profile.save()
        return render(request, 'Base.html',
                      {'user': request.user, 'profile': profile, 'cart': cart, 'favorites': favorites, })
    return render(request, 'User_info.html',
                  {'user': request.user, 'profile': profile, 'cart': cart, 'favorites': favorites, })


def Search(request):
    cart = Order.objects.filter(status=1, user_id=request.user.id).values_list('product_id', flat=True)
    favorites = Favorites.objects.filter(user_id=request.user.id).values_list('product_id', flat=True)
    if request.method == 'POST':
        prod_name = request.POST.get('q')
        prod_name = prod_name.lower()
        if (LastSearch.objects.filter(user_id=request.user.id).count() == 0):
            max_unique_id = LastSearch.objects.order_by('id').last()
            unique_id = max_unique_id.id + 1  # Генерируем уникальный айди для строки
            LS = LastSearch.objects.create(id=unique_id, user_id=request.user.id, query=prod_name)
        if (prod_name != ''):
            LS = LastSearch.objects.get(user=request.user.id)
            LS.query = prod_name
            LS.save()
        else:
            LS = LastSearch.objects.get(user=request.user.id)
            LS.query = 'Ничего не ищу, но кнопку поиска потыкать захотел'
            LS.save()
    LS = LastSearch.objects.get(user=request.user.id)
    product = Product.objects.filter(product_name__icontains=LS.query)
    return render(request, 'Search_result.html',
                  {'products': product, 'user': request.user, 'cart': cart, 'favorites': favorites, })


# Страница игр
def GamesView(request, platform_id, genre_id):
    cart = Order.objects.filter(status=1, user_id=request.user.id).values_list('product_id', flat=True)
    favorites = Favorites.objects.filter(user_id=request.user.id).values_list('product_id', flat=True)
    platforms = Platforms.objects.all()
    genres = Genres.objects.all()
    if (platform_id == 0 and genre_id == 0):
        products = Product.objects.exclude(category=2).exclude(count=0)
        pl = request.get_full_path()
        res_pl = re.search('/Games/(.+?)/', pl)
        if res_pl:
            found = res_pl.group(1)
        context = {
            'products': products,
            'platforms': platforms,
            'user': request.user,
            'cart': cart, 'favorites': favorites,
            'genres': genres,
            'found': found
        }
        return render(request, 'Games.html', context)
    else:
        if (genre_id != 0):
            products = Product.objects.filter(genre=genre_id).exclude(category=2).exclude(count=0)
        if (platform_id != 0):
            products = Product.objects.filter(platform=platform_id).exclude(category=2).exclude(count=0)
        if (platform_id != 0 and genre_id != 0):
            products = Product.objects.filter(platform=platform_id, genre=genre_id).exclude(category=2).exclude(count=0)
        pl = request.get_full_path()
        res_pl = re.search('/Games/(.+?)/', pl)
        if res_pl:
            found = res_pl.group(1)
        context = {
            'products': products,
            'platforms': platforms,
            'user': request.user,
            'cart': cart, 'favorites': favorites,
            'genres': genres,
            'found': found
        }
        return render(request, 'Games.html', context)


def ConsolesView(request):
    cart = Order.objects.filter(status=1, user_id=request.user.id).values_list('product_id', flat=True)
    favorites = Favorites.objects.filter(user_id=request.user.id).values_list('product_id', flat=True)
    products = Product.objects.filter(category=2).exclude(count=0)
    return render(request, 'Consoles.html',
                  {'user': request.user, 'products': products, 'cart': cart, 'favorites': favorites})


# Детализация товара
def Product_details(request, product_id):
    product = Product.objects.get(product_id=product_id)
    cart = Order.objects.filter(status=1, user_id=request.user.id, product_id=product_id)
    favorites = Favorites.objects.filter(user_id=request.user.id, product_id=product_id)
    return render(request, 'Product_details.html',
                  {'product': product, 'user': request.user, 'cart': cart, 'favorites': favorites, })


def Add_to_cart(request, product_id):
    profile = Profile.objects.get(user_id=request.user.id)
    product = Product.objects.get(product_id=product_id)

    if (Order.objects.filter(user_id=request.user.id, status=1,
                             product_id=product_id).count() == 0):  # Проверка наличия у юзера данного товара в корзине
        if Order.objects.filter(user_id=request.user.id, status=1).count() == 0:  # Если корзина у юзера пустая совсем

            max_unique_id = Order.objects.order_by('id').last()
            unique_id = max_unique_id.id + 1  # Генерируем уникальный айди для строки

            max_id = Order.objects.order_by('order_id').last()
            order_id = max_id.order_id + 1  # Генерируем айди для заказа, который будет повторяться в каждой записи текущей корзины текущего юзера

            order = Order.objects.create(id=unique_id,
                                         order_id=order_id,
                                         user_id=request.user.id,
                                         product_id=product_id,
                                         status=OrderStatus.objects.get(status_id=1),
                                         product_count=1,
                                         adress=profile.adress,
                                         price=product.price,
                                         data=datetime.now())

        else:  # Если корзина у юзера не пустая совсем

            max_unique_id = Order.objects.order_by('id').last()
            unique_id = max_unique_id.id + 1  # Генерируем уникальный айди для строки

            max_id = Order.objects.filter(user_id=request.user.id,
                                          status=1).last()  # присваиваем уже существующий айди заказа
            order_id = max_id.order_id  # Генерируем айди для заказа, который будет повторяться в каждой записи текущей корзины текущего юзера

            order = Order.objects.create(id=unique_id,
                                         order_id=order_id,
                                         user_id=request.user.id,
                                         product_id=product_id,
                                         status=OrderStatus.objects.get(status_id=1),
                                         product_count=1,
                                         adress=profile.adress,
                                         price=product.price,
                                         data=datetime.now())
    else:
        return redirect(request.META['HTTP_REFERER'])
    return redirect(request.META['HTTP_REFERER'])


def Del_from_cart(request, product_id):
    del_prod = Order.objects.filter(user_id=request.user.id, status=1, product_id=product_id)
    del_prod.delete()
    return redirect(request.META['HTTP_REFERER'])


def CartView(request):
    cart = Order.objects.filter(status=1, user_id=request.user.id).values_list('product_id', flat=True)
    favorites = Favorites.objects.filter(user_id=request.user.id)
    products = Product.objects.filter(product_id__in=cart)
    profile = Profile.objects.get(user_id=request.user.id)
    payments = Payments.objects.all()
    deliveries = DeliveryType.objects.all()
    price = products.aggregate(total_price=Sum('price'))
    if request.method == 'POST':
        order = Order.objects.filter(status=1, user_id=request.user.id)
        for obj in order:
            obj.status = OrderStatus.objects.get(status_id=2)
            obj.adress = request.POST.get('Adress')
            obj.delivery = DeliveryType.objects.get(delivery_id=request.POST.get('delivery_options'))
            obj.payment = Payments.objects.get(payment_id=request.POST.get('pay_options'))
            obj.data = datetime.now()
            obj.total_price = int(price.get("total_price", ""))
            obj.save()
            prod = Product.objects.get(product_id=obj.product.product_id)
            prod.count = prod.count - 1
            prod.save()
        return render(request, 'Order_success.html')
    return render(request, 'Cart.html',
                  {'user': request.user, 'cart': cart, 'favorites': favorites, 'products': products, 'profile': profile,
                   'payments': payments, 'deliveries': deliveries, 'price': price})


def Add_to_fav(request, product_id):
    # profile = Profile.objects.get(user_id=request.user.id)
    max_unique_id = Favorites.objects.order_by('id').last()
    unique_id = max_unique_id.id + 1  # Генерируем уникальный айди для строки
    fav = Favorites.objects.create(
        user_id=request.user.id,
        id=unique_id,
        product_id=product_id)
    return redirect(request.META['HTTP_REFERER'])


def Del_from_fav(request, product_id):
    del_prod = Favorites.objects.filter(user_id=request.user.id, product_id=product_id)
    del_prod.delete()
    return redirect(request.META['HTTP_REFERER'])


def FavView(request):
    favo_list = Favorites.objects.filter(user_id=request.user.id).values_list('product_id', flat=True)
    products = Product.objects.filter(product_id__in=favo_list)
    cart = Order.objects.filter(status=1, user_id=request.user.id)
    favorites = Favorites.objects.filter(user_id=request.user.id)
    return render(request, 'FavView.html',
                  {'user': request.user, 'cart': cart, 'products': products, 'favorites': favorites})


def OrdersView(request):
    cart = Order.objects.filter(status=1, user_id=request.user.id)
    favorites = Favorites.objects.filter(user_id=request.user.id)
    orders = Order.objects.filter(user_id=request.user.id).exclude(status=1).values('order_id', 'data', 'status',
                                                                                    'adress',
                                                                                    'total_price').distinct()  # Стягиваем с базы уникальные айдишники всеобщего заказа
    return render(request, 'OrderView.html',
                  {'user': request.user, 'cart': cart, 'favorites': favorites, 'orders': orders})


def Order_Details(request, order_id):
    cart = Order.objects.filter(status=1, user_id=request.user.id)
    favorites = Favorites.objects.filter(user_id=request.user.id)
    current_order = Order.objects.filter(user_id=request.user.id, order_id=order_id).last()
    current_order_products = Order.objects.filter(user_id=request.user.id, order_id=order_id).values('product_id',
                                                                                                     'order_id', 'data',
                                                                                                     'status', 'adress',
                                                                                                     'total_price')
    products = Product.objects.filter(product_id__in=current_order_products.values('product_id'))
    return render(request, 'OrderDetails.html',
                  {'user': request.user, 'cart': cart, 'favorites': favorites, 'products': products,
                   'current_order': current_order, 'current_order_products': current_order_products, })


def InfoView(request):
    cart = Order.objects.filter(status=1, user_id=request.user.id)
    favorites = Favorites.objects.filter(user_id=request.user.id)
    return render(request, 'Info.html', {'user': request.user, 'cart': cart, 'favorites': favorites})


def ContactView(request):
    cart = Order.objects.filter(status=1, user_id=request.user.id)
    favorites = Favorites.objects.filter(user_id=request.user.id)
    return render(request, 'Contact.html', {'user': request.user, 'cart': cart, 'favorites': favorites})
