from rest_framework.permissions import SAFE_METHODS, BasePermission


class AuthorOrReadOnly(BasePermission):
    """Пермишн, который проверяет является ли юзер автором поста."""

    def has_object_permission(self, request, view, obj):
        return request.method in SAFE_METHODS or request.user == obj.author
