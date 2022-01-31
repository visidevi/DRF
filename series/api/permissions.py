from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsMeOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # if request.method in SAFE_METHODS:
        if request.method == 'GET':
            return True
        else:
            return bool(request.user.is_authenticated and request.user.username == "visidevi")

    def has_object_permission(self, request, view, obj):
        # Si el objeto es x en especifico, solo ver capitulos del mismo xdxd
        if request.method == 'GET':
            return True
        else:
            return bool(request.user.is_authenticated
                        and request.user.username == "visidevi")
