from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login
from . import views

app_name = 'students'

urlpatterns = [
#    url(r'^login/$', login, name="my_login"),
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
    url(r'^action/(?P<way>\w{7})/(?P<pk>\d{0,4})$', views.common_act, name='common_act'),
    url(r'^new_tag/(?P<pk>\d+)$', views.new_tag, name='new_tag'),
    url(r'^register/$', views.RegisterFormView.as_view()),
    url(r'^login/$', views.LoginFormView.as_view()),
    url(r'^logout/$', views.LogoutView.as_view()),

]
