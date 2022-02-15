# TODO:  Напишите свой вариант
from rest_framework import viewsets, mixins, permissions

from api.serializers import GroupSerializer
from posts.models import Post, Group, Follow, Comment
from api.permissions import AuthorOrReadOnly
from yatube_api.api.serializers import CommentSerializer, FollowSerializers, PostSerializer


class ListCreateViewSet(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    pass


class FollowViewSet(ListCreateViewSet):

    queryset = Follow.objects.all()
    serializer_classes = FollowSerializers
    permission_classes = (permissions.IsAuthenticated,)


class PostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all()
    serializer_classes = PostSerializer
    permission_classes = (AuthorOrReadOnly,)


class CommenViewSet(viewsets.ModelViewSet):

    queryset = Comment.objects.all()
    serializer_classes = CommentSerializer
    permission_classes = (AuthorOrReadOnly,)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer



