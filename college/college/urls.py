from django.conf.urls import include, url
from django.contrib import admin

from students import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^students/', include('students.urls'))
]
