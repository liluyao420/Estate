#coding=utf-8
from django.conf.urls import url
from employee import views

urlpatterns = [
    url(r'^emp_list/$', views.empList),
    url(r'^emp_edit/(\d+)/$', views.empEdit),
    url(r'^emp_detail/(\d+)/$', views.empDetail),
    url(r'^emp_del/(\d+)/$', views.empDel),
    url(r'^emp_search/$', views.empSea),
    url(r'^employee_submit/(\d+)/$', views.employeeSubmit),

    url(r'^notice_list/$', views.noticeList),
    url(r'^notice_add/$', views.noticeAdd),
    url(r'^notice_del/(\d+)/$', views.noticeDel),
    url(r'^notice_search/$', views.noticeSearch)
]
