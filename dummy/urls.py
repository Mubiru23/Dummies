from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static
urlpatterns = [
          path('',views.home,name='home'),
          path('gallery',views.gallery,name='gallery'),
          path('kids',views.kids,name='kids'),
          path('men',views.men,name='men'),
          path('women',views.women,name='women'),
          path('customizable',views.customizable,name='customizable'), 
          path('fashion',views.fashion,name='fashion'),  
          path('store',views.store,name='store'), 
] + static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)