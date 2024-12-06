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

    #Region
    path('backend/region/<int:id>', views_backend.RegionDetail.as_view()),
    path('backend/region/',  views_backend.RegionList.as_view()),

    #Ciudad
    path('backend/ciudad/<int:id>', views_backend.CiudadDetail.as_view()),
    path('backend/ciudad/',  views_backend.CiudadList.as_view()),

    #Comuna
    path('backend/comuna/<int:id>', views_backend.ComunaDetail.as_view()),
    path('backend/comuna/',  views_backend.ComunaList.as_view()),



    #producto
    path('backend/producto/<int:id>', views_backend.ProductoDetail.as_view()),
    path('backend/producto/',  views_backend.ProductoList.as_view()),

    path('backend/usuario/<int:id>', views_backend.UsuarioDetail.as_view()),
    path('backend/usuario/',  views_backend.UsuarioList.as_view()),

    path('backend/direccion/<int:id>', views_backend.DireccionDetail.as_view()),
    path('backend/direccion/',  views_backend.DireccionList.as_view()),


    #apis

    path('backend/login/', views_backend.LoginView.as_view(), name='token_obtain_pair'),


    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),



    path('iniciar-transaccion/', views_backend.WebpayTransaction.as_view(), name='iniciar_transaccion'),
    path('confirmar-transaccion/<str:token>/', views_backend.ConfirmarTransaccion.as_view(), name='confirmar_transaccion'),



]
