"""covid_india URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from homepage.views import home_view
from services import views as service_views
from medical_services import views as med_serv_views
from food_services import views as food_serv_views
from updatedata import views as data_views
from volunteer_ob.views import VolObViews
from thankyou import views as thank_views
from get_volunteers import views as vol_views
from hospitals import views as hosp_views
from oxygen_supliers import views as oxy_views
from django.contrib import admin

admin.autodiscover()
admin.site.enable_nav_sidebar = False

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view.as_view()),
    path('services/<slug>', service_views.index),
    path('remedesvir/<slug>', med_serv_views.index),
    path('food/<slug>', food_serv_views.index),
    path('updatedb/', data_views.index),
    path('volunteer_reg/', VolObViews.as_view()),
    path('thankyou/<pk>', thank_views.index),
    path('volunteers/<slug>', vol_views.index),
    path('hospital/<slug>', hosp_views.index),
    path('oxygen/<slug>', oxy_views.index)
]
