# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Dep(models.Model):
    num_dep = models.IntegerField(db_column='Num_dep', primary_key=True)  # Field name made lowercase.
    boss = models.ForeignKey('Worker', models.DO_NOTHING, db_column='Boss', blank=True, null=True, related_name='ID_worker')  # Field name made lowercase.
    count_workers = models.IntegerField(db_column='Count_workers', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Dep'


class Medical(models.Model):
    num_medical = models.IntegerField(db_column='Num_medical', primary_key=True)  # Field name made lowercase.
    num_order = models.ForeignKey('Order', models.DO_NOTHING, db_column='Num_order')  # Field name made lowercase.
    id_worker = models.ForeignKey('Worker', models.DO_NOTHING, db_column='ID_worker')  # Field name made lowercase.
    data_start_medical = models.DateField(db_column='Data_start_medical')  # Field name made lowercase.
    data_end_medical = models.DateField(db_column='Data_end_medical')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Medical'


class Mission(models.Model):
    num_mission = models.IntegerField(db_column='Num_mission', primary_key=True)  # Field name made lowercase.
    num_order = models.ForeignKey('Order', models.DO_NOTHING, db_column='Num_order')  # Field name made lowercase.
    id_worker = models.ForeignKey('Worker', models.DO_NOTHING, db_column='ID_worker')  # Field name made lowercase.
    place_order = models.CharField(db_column='Place_order', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    data_start_mission = models.DateField(db_column='Data_start_mission')  # Field name made lowercase.
    data_end_mission = models.DateField(db_column='Data_end_mission')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Mission'


class Order(models.Model):
    num_order = models.IntegerField(db_column='Num_order', primary_key=True)  # Field name made lowercase.
    type_order = models.CharField(db_column='Type_order', max_length=15, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    data_order = models.DateField(db_column='Data_order')  # Field name made lowercase.
    id_worker = models.ForeignKey('Worker', models.DO_NOTHING, db_column='ID_worker', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Order'


class Stafflist(models.Model):
    id_record = models.IntegerField(db_column='ID_record', primary_key=True)  # Field name made lowercase.
    num_dep = models.ForeignKey(Dep, models.DO_NOTHING, db_column='Num_dep')  # Field name made lowercase.
    post_name = models.CharField(db_column='Post_name', max_length=50, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    count_units = models.IntegerField(db_column='Count_units')  # Field name made lowercase.
    salary = models.FloatField(db_column='Salary')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StaffList'


class Statement(models.Model):
    num_statement = models.IntegerField(db_column='Num_statement', primary_key=True)  # Field name made lowercase.
    id_worker = models.ForeignKey('Worker', models.DO_NOTHING, db_column='ID_worker')  # Field name made lowercase.
    type_statement = models.CharField(db_column='Type_statement', max_length=15, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    data_statement = models.DateField(db_column='Data_statement', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Statement'


class Vacation(models.Model):
    num_vacation = models.IntegerField(db_column='Num_vacation', primary_key=True)  # Field name made lowercase.
    num_order = models.ForeignKey(Order, models.DO_NOTHING, db_column='Num_order')  # Field name made lowercase.
    id_worker = models.ForeignKey('Worker', models.DO_NOTHING, db_column='ID_worker')  # Field name made lowercase.
    data_start_vacation = models.DateField(db_column='Data_start_vacation')  # Field name made lowercase.
    data_end_vacation = models.DateField(db_column='Data_end_vacation')  # Field name made lowercase.
    type_vacation = models.CharField(db_column='Type_vacation', max_length=15, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Vacation'


class Worker(models.Model):
    id_worker = models.IntegerField(db_column='ID_worker', primary_key=True)  # Field name made lowercase.
    fio_worker = models.CharField(db_column='FIO_worker', max_length=70, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    dep = models.ForeignKey(Dep, models.DO_NOTHING, db_column='Dep')  # Field name made lowercase.
    post_name = models.CharField(db_column='Post_name', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    data_birth = models.DateField(db_column='Data_birth', blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(db_column='Sex', max_length=1, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    allowance = models.FloatField(db_column='Allowance', blank=True, null=True)  # Field name made lowercase.
    stage = models.IntegerField(db_column='Stage', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=15, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    work_reception_date = models.DateField(db_column='Work_reception_date')  # Field name made lowercase.
    data_termination = models.DateField(db_column='Data_termination', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Worker'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, db_collation='Cyrillic_General_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, db_collation='Cyrillic_General_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, db_collation='Cyrillic_General_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, db_collation='Cyrillic_General_CI_AS')
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, db_collation='Cyrillic_General_CI_AS')
    first_name = models.CharField(max_length=150, db_collation='Cyrillic_General_CI_AS')
    last_name = models.CharField(max_length=150, db_collation='Cyrillic_General_CI_AS')
    email = models.CharField(max_length=254, db_collation='Cyrillic_General_CI_AS')
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(db_collation='Cyrillic_General_CI_AS', blank=True, null=True)
    object_repr = models.CharField(max_length=200, db_collation='Cyrillic_General_CI_AS')
    action_flag = models.SmallIntegerField()
    change_message = models.TextField(db_collation='Cyrillic_General_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, db_collation='Cyrillic_General_CI_AS')
    model = models.CharField(max_length=100, db_collation='Cyrillic_General_CI_AS')

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, db_collation='Cyrillic_General_CI_AS')
    name = models.CharField(max_length=255, db_collation='Cyrillic_General_CI_AS')
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40, db_collation='Cyrillic_General_CI_AS')
    session_data = models.TextField(db_collation='Cyrillic_General_CI_AS')
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128, db_collation='Cyrillic_General_CI_AS')
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)
