# from django.contrib import admin
# from django.urls import include,path
# from api.views import CompanyViewSet
# from rest_framework import routers

# router=routers.DefaultRouter()
# router.register(r'companies',CompanyViewSet)

# urlpatterns = [
#   path('api/v1/', include(router.urls))  # Add the prefix here
# ]
# companyapi/urls.py
# from django.urls import include, path

from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import include,path
from api.views import CompanyViewSet,EmployeeViewSet

router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'employee',EmployeeViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('admin/', admin.site.urls)
  # assuming you have this view
]

