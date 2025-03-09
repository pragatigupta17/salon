from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.landingpage, name='landingpage'),
    path('registration/', views.registration, name='registration'),
    path('registration_table/', views.registration_table, name='registration_table'),
    path('update/<int:pk>',views.update,name='update'),
    path('delete/<int:pk>',views.delete,name='delete'),
     path('edit/<int:pk>',views.edit,name='edit'),
     path('clientbase/', views.clientbase, name='clientbase'),
    path('services/',views.services, name='services'),
    path('review/',views.review, name='review'),
    path('booking/',views.booking, name='booking'),
    path('appoiment/', views.appoiment, name='appoiment'),
    path('search/', views.search, name='search'),
    path('review_data/', views.review_data, name='review_data'),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)


