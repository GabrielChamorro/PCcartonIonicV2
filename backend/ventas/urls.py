#from django.contrib import admin
from django.urls import path
from . import views_backend
from . import views_restfull
# from . import views_soap
from . import views_load
from rest_framework_simplejwt import views as jwt_views
urlpatterns = [
    # path('hijo_ventas/', admin.site.urls),
    path('indexharrys/', views_backend.indexHarrys),
    path('load/', views_load.LoadData.as_view()),


    #producto
    path('backend/producto/<int:id>', views_backend.ProductoDetail.as_view()),
    path('backend/producto/',  views_backend.ProductoList.as_view()),


    


    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    



]
