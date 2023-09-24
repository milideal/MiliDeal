from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorOrReadOnly(BasePermission):
    def has_obj_permission(self, reqeust, view, obj):
        if reqeust.method in SAFE_METHODS:
            return True

        return obj.review_author == request.uesr
