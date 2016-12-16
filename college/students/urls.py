from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login
from . import views

app_name = 'students'

urlpatterns = [
    url(r'^login/$', login, name="my_login"),
    url(r'^group_tmpl/$',
        views.GroupView.as_view(),
        name = 'group_tmpl'
    ),
    url(r'^student_tmpl/(?P<grp_id>\d{1,4})$',
        views.StudentView.as_view(),
        name = 'student_tmpl'
    ),
#    url(r'^action_tmpl/(?P<typ>[std|grp]+)/
#        (?P<act>[crt|dlt|edt]+)/(?P<obj_id>\d{0,4})$',
#        views.actions,
#        name = 'action_tmpl'
#    ),
    url(r'^crt_grp/(?P<pk>\d{0,4})$',
        views.CrtGroup.as_view(),
        name='crt_grp'
        ),
    url(r'^edt_grp/(?P<pk>\d{0,4})$',
        views.EdtGroup.as_view(),
        name='edt_grp'
        ),
    url(r'^dlt_grp/(?P<pk>\d{0,4})$',
        views.DltGroup.as_view(),
        name='dlt_grp'
        ),
    url(r'^crt_std/(?P<pk>\d{0,4})$',
        views.CrtStudent.as_view(),
        name='crt_std'
        ),
    url(r'^edt_std/(?P<pk>\d{0,4})$',
        views.EdtStudent.as_view(),
        name='edt_std'
        ),
    url(r'^dlt_std/(?P<pk>\d{0,4})$',
        views.DltStudent.as_view(),
        name='dlt_std'
        ),
    url(r'^new_tag/(?P<pk>\d+)$', views.new_tag, name='new_tag')
]
