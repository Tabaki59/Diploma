# Generated by Django 3.0.4 on 2021-04-23 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('category_id', models.IntegerField(db_column='Category_ID', primary_key=True, serialize=False)),
                ('category', models.TextField(db_column='Category')),
            ],
            options={
                'db_table': 'Categories',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DeliveryType',
            fields=[
                ('delivery_id', models.IntegerField(db_column='Delivery_ID', primary_key=True, serialize=False)),
                ('delivery', models.TextField(db_column='Delivery')),
                ('description', models.TextField(db_column='Description')),
            ],
            options={
                'db_table': 'Delivery_Type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'Favorites',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('genre_id', models.IntegerField(db_column='Genre_ID', primary_key=True, serialize=False)),
                ('genre', models.TextField(db_column='Genre')),
            ],
            options={
                'db_table': 'Genres',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('languge_id', models.IntegerField(db_column='Languge_ID', primary_key=True, serialize=False)),
                ('language', models.TextField(db_column='Language')),
            ],
            options={
                'db_table': 'Languages',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.IntegerField(db_column='Order_ID', primary_key=True, serialize=False)),
                ('product_count', models.IntegerField(db_column='Product_Count')),
                ('adress', models.TextField(blank=True, db_column='Adress', null=True)),
                ('data', models.DateField(db_column='Data')),
                ('price', models.FloatField(db_column='Price')),
            ],
            options={
                'db_table': 'Order',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('status_id', models.IntegerField(db_column='Status_ID', primary_key=True, serialize=False)),
                ('status', models.TextField(db_column='Status')),
            ],
            options={
                'db_table': 'Order_status',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('payment_id', models.IntegerField(db_column='Payment_ID', primary_key=True, serialize=False)),
                ('payment_name', models.TextField(db_column='Payment_Name')),
                ('description', models.TextField(db_column='Description')),
            ],
            options={
                'db_table': 'Payments',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Platforms',
            fields=[
                ('platform_id', models.IntegerField(db_column='Platform_ID', primary_key=True, serialize=False)),
                ('platform', models.TextField(db_column='Platform')),
            ],
            options={
                'db_table': 'Platforms',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.IntegerField(db_column='Product_ID', primary_key=True, serialize=False)),
                ('product_name', models.IntegerField(db_column='Product_Name')),
                ('photo', models.BinaryField(blank=True, db_column='Photo', null=True)),
                ('price', models.FloatField(db_column='Price')),
                ('description', models.TextField(blank=True, db_column='Description', null=True)),
                ('count', models.IntegerField(db_column='Count')),
                ('date', models.DateField(db_column='Date')),
            ],
            options={
                'db_table': 'Product',
                'managed': False,
            },
        ),
        migrations.AddField(
            model_name='profile',
            name='adress',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
