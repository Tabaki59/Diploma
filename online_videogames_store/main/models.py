# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.TextField(max_length=500, blank=True)
    adress = models.TextField(max_length=500, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Categories(models.Model):
    category_id = models.IntegerField(db_column='Category_ID', primary_key=True)  # Field name made lowercase.
    category = models.TextField(db_column='Category')  # Field name made lowercase. This field type is a guess.

    def __str__(self):
        return self.category

    class Meta:
        managed = False
        db_table = 'Categories'
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товаров'


class DeliveryType(models.Model):
    delivery_id = models.IntegerField(db_column='Delivery_ID', primary_key=True)  # Field name made lowercase.
    delivery = models.TextField(db_column='Delivery')  # Field name made lowercase. This field type is a guess.
    description = models.TextField(db_column='Description')  # Field name made lowercase. This field type is a guess.

    def __str__(self):
        return self.delivery

    class Meta:
        managed = False
        db_table = 'Delivery_Type'
        verbose_name = 'Способ доставки'
        verbose_name_plural = 'Способы доставки'


class Favorites(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey('Profile', models.DO_NOTHING, db_column='User_ID')  # Field name made lowercase.
    product = models.ForeignKey('Product', models.DO_NOTHING, db_column='Product_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Favorites'


class Genres(models.Model):
    genre_id = models.IntegerField(db_column='Genre_ID', primary_key=True)  # Field name made lowercase.
    genre = models.TextField(db_column='Genre')  # Field name made lowercase. This field type is a guess.

    def __str__(self):
        return self.genre

    class Meta:
        managed = False
        db_table = 'Genres'
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Languages(models.Model):
    languge_id = models.IntegerField(db_column='Languge_ID', primary_key=True)  # Field name made lowercase.
    language = models.TextField(db_column='Language')  # Field name made lowercase. This field type is a guess.

    def __str__(self):
        return self.language

    class Meta:
        managed = False
        db_table = 'Languages'
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'


class LastSearch(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='User_id')  # Field name made lowercase.
    query = models.TextField(db_column='Query')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Last_search'


class Order(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    order_id = models.IntegerField(db_column='Order_ID')  # Field name made lowercase.
    user = models.ForeignKey('Profile', models.DO_NOTHING, db_column='User_ID')  # Field name made lowercase.
    product = models.ForeignKey('Product', models.DO_NOTHING, db_column='Product_ID')  # Field name made lowercase.
    product_count = models.IntegerField(db_column='Product_Count')  # Field name made lowercase.
    adress = models.TextField(db_column='Adress', blank=True,
                              null=True)  # Field name made lowercase. This field type is a guess.
    delivery = models.ForeignKey(DeliveryType, models.DO_NOTHING, db_column='Delivery_ID', blank=True,
                                 null=True)  # Field name made lowercase.
    payment = models.ForeignKey('Payments', models.DO_NOTHING, db_column='Payment_ID', blank=True,
                                null=True)  # Field name made lowercase.
    status = models.ForeignKey('OrderStatus', models.DO_NOTHING, db_column='Status')  # Field name made lowercase.
    data = models.DateField(db_column='Data')  # Field name made lowercase.
    price = models.FloatField(db_column='Price')  # Field name made lowercase.
    total_price = models.FloatField(db_column='Total_price')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Order'


class OrderStatus(models.Model):
    status_id = models.IntegerField(db_column='Status_ID', primary_key=True)  # Field name made lowercase.
    status = models.TextField(db_column='Status')  # Field name made lowercase. This field type is a guess.

    def __str__(self):
        return self.status

    class Meta:
        managed = False
        db_table = 'Order_status'
        verbose_name = 'Статус закза'
        verbose_name_plural = 'Статусы'


class Payments(models.Model):
    payment_id = models.IntegerField(db_column='Payment_ID', primary_key=True)  # Field name made lowercase.
    payment_name = models.TextField(db_column='Payment_Name')  # Field name made lowercase. This field type is a guess.
    description = models.TextField(db_column='Description')  # Field name made lowercase. This field type is a guess.

    def __str__(self):
        return self.payment_name

    class Meta:
        managed = False
        db_table = 'Payments'
        verbose_name = 'Способ оплаты'
        verbose_name_plural = 'Способы оплаты'


class Platforms(models.Model):
    platform_id = models.IntegerField(db_column='Platform_ID', primary_key=True)  # Field name made lowercase.
    platform = models.TextField(db_column='Platform')  # Field name made lowercase. This field type is a guess.

    def __str__(self):
        return self.platform

    class Meta:
        managed = False
        db_table = 'Platforms'
        verbose_name = 'Платформа'
        verbose_name_plural = 'Платформы'


class Product(models.Model):
    product_id = models.IntegerField(db_column='Product_ID', primary_key=True)  # Field name made lowercase.
    product_name = models.TextField(db_column='Product_Name')  # Field name made lowercase.
    category = models.ForeignKey(Categories, models.DO_NOTHING, db_column='Category')  # Field name made lowercase.
    platform = models.ForeignKey(Platforms, models.DO_NOTHING, db_column='Platform',
                                 null=True)  # Field name made lowercase.
    photo = models.TextField(db_column='Photo', blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='Price')  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True,
                                   null=True)  # Field name made lowercase. This field type is a guess.
    count = models.IntegerField(db_column='Count')  # Field name made lowercase.
    genre = models.ForeignKey(Genres, models.DO_NOTHING, db_column='Genre', blank=True,
                              null=True)  # Field name made lowercase.
    localization = models.ForeignKey(Languages, models.DO_NOTHING, related_name='Localization',
                                     db_column='Localization', blank=True,
                                     null=True)  # Field name made lowercase.
    language = models.ForeignKey(Languages, models.DO_NOTHING, related_name='Language', db_column='Language',
                                 blank=True,
                                 null=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.

    def __str__(self):
        return self.product_name

    class Meta:
        managed = False
        db_table = 'Product'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
