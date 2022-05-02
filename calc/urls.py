from django.urls import path
from rest_framework import routers
from . import  views

router=routers.DefaultRouter()
router.register('via_postman',views.via_postman, basename='via_postman')
urlpatterns=[
    path('',views.home, name='home'),
    path('math_operation', views.math_operation, name='math_operation'),
    path('via_postman', views.via_postman, name='via_postman')
]