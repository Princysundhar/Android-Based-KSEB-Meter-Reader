"""KSEB_Meter_Reader URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import views

# ....................................................................... --->ADMIN
urlpatterns = [
    path('', views.log),
    path('login_post', views.login_post),
    path('logout', views.logout),
    path('admin_home', views.admin_home),
    path('add_branch', views.add_branch),
    path('add_branch_post', views.add_branch_post),
    path('view_branch', views.view_branch),
    path('update_branch/<id>', views.update_branch),
    path('update_branch_post/<id>', views.update_branch_post),
    path('delete_branch/<id>', views.delete_branch),
    path('add_unit_price', views.add_unit_price),
    path('add_unit_price_post', views.add_unit_price_post),
    path('view_unit_price', views.view_unit_price),
    path('update_unit_price/<id>', views.update_unit_price),
    path('update_unit_price_post/<id>', views.update_unit_price_post),
    path('delete_unit_price/<id>', views.delete_unit_price),
    path('add_notification', views.add_notification),
    path('add_notification_post', views.add_notification_post),
    path('view_notification', views.view_notification),
    path('delete_notification/<id>', views.delete_notification),
    path('view_rating', views.view_rating),
    path('add_consumer', views.add_consumer),
    path('view_area/<id>', views.view_area),
    path('view_consumer', views.view_consumer),
    path('add_staff', views.add_staff),
    path('staff_view_area/<id>', views.staff_view_area),
    path('view_staff', views.view_staff),

#.....................................................................................      --->KSEB BRANCH
    path('kseb_home',views.kseb_home),
    path('add_area',views.add_area),
    path('add_area_post',views.add_area_post),
    path('view_areas',views.view_areas),
    path('delete_area/<id>',views.delete_area),
    path('add_staffs',views.add_staffs),
    path('add_staff_post',views.add_staff_post),
    path('view_staffs',views.view_staffs),
    path('update_staff/<id>',views.update_staff),
    path('update_staff_post/<id>',views.update_staff_post),
    path('delete_staff/<id>',views.delete_staff),
    path('add_consumers',views.add_consumers),
    path('add_consumers_post',views.add_consumers_post),
    path('view_consumers',views.view_consumers),
    path('update_consumer/<id>',views.update_consumer),
    path('update_consumer_post/<id>',views.update_consumer_post),
    path('delete_consumer/<id>',views.delete_consumer),
    path('allocate_work_tostaff/<id>',views.allocate_work_tostaff),
    path('allocate_area/<id>',views.allocate_area),
    path('view_complaints',views.view_complaints),
    path('send_reply/<id>',views.send_reply),
    path('send_reply_post/<id>',views.send_reply_post),
    path('view_bill',views.view_bill),
    path('view_bill_post',views.view_bill_post),
    # path('view_bills',views.view_bills),

#............................................................................   ---> STAFF

    path('staff_home',views.staff_home),
    path('view_profile',views.view_profile),
    path('view_allocated_work',views.view_allocated_work),
    path('staff_view_consumer',views.staff_view_consumer),
    path('view_consumer_post',views.view_consumer_post),
    path('view_previous_reading/<id>',views.view_previous_reading),
    path('current_readings/<id>',views.current_readings),
    path('current_reading_post/<id>',views.current_reading_post),

#..................................................................................     ---> CONSUMER
    path('android_login',views.android_login),
    path('android_view_profile',views.android_view_profile),
    path('android_view_previous_bill',views.android_view_previous_bill),
    path('android_send_complaint',views.android_send_complaint),
    path('android_view_complaint',views.android_view_complaint),
    path('android_send_rate',views.android_send_rate),
    path('android_view_notification',views.android_view_notification),
    path('android_online_payment',views.android_online_payment),
    path('android_view_bill',views.android_view_bill),





]
