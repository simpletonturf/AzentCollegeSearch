from django.conf.urls import url
from listApi import views

urlpatterns = [
    url(r'^api/collegeList$', views.college_list),
]
