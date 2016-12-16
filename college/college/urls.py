from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login
from students import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', login, name="my_login"),
    url(r'^admin/', admin.site.urls),
    url(r'^students/', include('students.urls')),
]
