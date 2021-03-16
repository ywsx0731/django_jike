"""recruitment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import path, include
from django.utils.translation import gettext as _
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
from jobs.models import Job


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class JobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'


class JobViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Job.objects.all()
    serializer_class = JobSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'jobs', JobViewSet)

urlpatterns = [
    url(r'^', include('jobs.urls')),

    # django rest api & api auth (login/logout)
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),

    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    url('^accounts/', include('registration.backends.simple.urls')),

    path('i18n/', include('django.conf.urls.i18n')),

]

admin.site.site_header = _('匠果科技招聘管理系统')