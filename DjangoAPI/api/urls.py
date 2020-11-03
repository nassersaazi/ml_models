from . import views 
from django.urls import include,path
from rest_framework import routers

router = routers.DefaultRouter()
router.register('api', views.ApprovalsView)

urlpatterns = [
    path('form/', views.myform,name='myform'),
    path('api/', include(router.urls)),
    path('status/', views.approvereject),
]
