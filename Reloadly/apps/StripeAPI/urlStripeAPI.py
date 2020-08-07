from django.conf.urls import url,include
from django.contrib.auth import views as auth_views
from . import views
from .views import HomePageView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url('inicio/(?P<result>\w+?)/$',login_required(HomePageView), name='pagoStripeAPI'),
    url('inicio/',login_required(views.HomePageViewClass.as_view()), name='pagoStripeAPI'),
    url('config/', views.stripe_config),  # new
]