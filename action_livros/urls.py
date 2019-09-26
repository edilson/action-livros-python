from django.contrib import admin
from django.conf.urls import include, url
from rest_framework_nested import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import view as views

router = routers.SimpleRouter()
router.register('autores', views.AutorViewSet, basename="autores")
router.register('editoras', views.EditoraViewSet, basename="editoras")

editoras_router = routers.NestedSimpleRouter(router, 'editoras', lookup='editoras')
editoras_router.register('livros', views.LivroViewSet, base_name='editoras-livros')

autores_router = routers.NestedSimpleRouter(router, 'autores', lookup='autores')

urlpatterns = [
    url(r'^v0.5/', include(router.urls)),
    url(r'^v0.5/', include(editoras_router.urls)),
    url(r'^v0.5/', include(autores_router.urls)),
    url(r'^api/token/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^api/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),
    url('admin/', admin.site.urls),
]
