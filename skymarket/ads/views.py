from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated

from ads.filters import AdFilter
from ads.models import Ad, Comment
from ads.permissions import OwnerOrStaffPermission
from ads.serializers import AdSerializer, AdDetailSerializer, CommentSerializer


class AdPagination(pagination.PageNumberPagination):
    page_size = 4


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    pagination_class = AdPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdFilter

    def get_serializer_class(self):
        if self.action in ('me', 'list'):
            self.serializer_class = AdSerializer
        else:
            self.serializer_class = AdDetailSerializer
        return super().get_serializer_class()

    def perform_create(self, serializer):
        serializer.save(author_id=self.request.user.pk)

    def get_permissions(self):
        if self.action == 'list':
            self.permission_classes = [AllowAny]
        elif self.action in ('update', 'destroy'):
            self.permission_classes = [IsAuthenticated, OwnerOrStaffPermission]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

    @action(detail=False, methods=['get'])
    def me(self, request, *args, **kwargs):
        self.queryset = self.get_queryset().filter(author_id=self.request.user.pk)
        return self.list(request, *args, **kwargs)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action in ('update', 'destroy'):
            self.permission_classes = [IsAuthenticated, OwnerOrStaffPermission]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

    def get_queryset(self):
        self.queryset = self.queryset.filter(ad=self.kwargs['ad_pk'])
        return super().get_queryset()

    def perform_create(self, serializer):
        serializer.save(author_id=self.request.user.pk, ad_id=self.kwargs['ad_pk'])

