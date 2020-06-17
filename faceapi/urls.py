from django.contrib import admin
from django.urls import path
from django.conf import settings
from register import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('verify/',views.verify),
    path('register/',views.regis),
    path('delete/',views.delete),
    path('delete_all/',views.clear_db),
    path('getdata/',views.getData),
]
