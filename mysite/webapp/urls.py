from django.conf.urls import url
from . import views #. import means we are importing from current package


urlpatterns = [
    url(r'^hello',views.index,name='index')
]