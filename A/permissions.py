"""
for customize permissions
"""
from rest_framework.permissions import BasePermission , SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):
    message = "not yours"
    # after user enter to view
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        # کاربری کع اومده باید اون چیز برای خودش باشه تا بتونه تغییر بده
        return obj.user == request.user