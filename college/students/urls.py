from django.conf.urls import url
from django.contrib import admin

from . import views

app_name = 'students'

urlpatterns = [
    url(r'^group_tmpl/$',
        views.GroupView.as_view(),
        name = 'group_tmpl'
    ),
    url(r'^student_tmpl/(?P<grp_id>\d{1,4})$',
        views.StudentView.as_view(),
        name = 'student_tmpl'
    ),
    url(r'^action_tmpl/(?P<typ>[std|grp]+)/(?P<act>[crt|dlt|edt]+)/(?P<obj_id>\d{0,4})$',
        views.actions,
        name = 'action_tmpl'
    ),
]
