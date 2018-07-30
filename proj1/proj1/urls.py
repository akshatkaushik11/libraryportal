"""proj1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls import include
from app import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
url(r'^register/',views.register),
url(r'^login/',views.login,),
url(r'^librarian/',views.librarian),
url(r'^student/',views.student,),
url(r'^logoutsuccess/',views.logout_user),
url(r'^book_details/',views.book_details),
url(r'^student_profile/',views.student_profile),
url(r'^book_search/',views.book_search),
url(r'^main/',views.main_page,),
url(r'^book_list/',views.book_list),
url(r'^oauth/', include('social_django.urls', namespace='social')), 
url(r'^$',views.start),
 ]
