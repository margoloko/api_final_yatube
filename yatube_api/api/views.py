from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins, permissions
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination

from api.serializers import GroupSerializer
from posts.models import Post, Group
from api.permissions import AuthorOrReadOnly
from api.serializers import (CommentSerializer, FollowSerializers,
                             PostSerializer)


class ListCreateViewSet(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    pass


class FollowViewSet(ListCreateViewSet):

    serializer_class = FollowSerializers
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['following__username', ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.request.user.follower.all()


class PostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommenViewSet(viewsets.ModelViewSet):

    serializer_class = CommentSerializer
    permission_classes = (AuthorOrReadOnly,)

    def get_post(self):
        return get_object_or_404(Post, id=self.kwargs.get('post_id'))

    def get_queryset(self):
        return self.get_post().comments.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.get_post())


class GroupViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
