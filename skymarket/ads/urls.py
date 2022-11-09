from rest_framework_nested import routers

from ads.views import AdViewSet, CommentViewSet

router_ad = routers.SimpleRouter()
router_ad.register('ads', AdViewSet, basename="ads")
router_comment = routers.NestedSimpleRouter(router_ad, 'ads', lookup='ad')
router_comment.register('comments', CommentViewSet, basename="comments")

urlpatterns = []

urlpatterns += router_ad.urls
urlpatterns += router_comment.urls
