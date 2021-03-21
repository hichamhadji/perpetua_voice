from playlist.views import PlayListViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'playlists', PlayListViewSet, basename='playlist')
urlpatterns = router.urls