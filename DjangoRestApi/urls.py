from django.urls import include, path
from rest_framework import routers
from DjangoRestApi.rest_api import views
from rental import views as rental_views
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'friends', rental_views.FriendViewSet)
router.register(r'belongings', rental_views.BelongingViewSet)
router.register(r'borrowings', rental_views.BorrowedViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
