from rest_framework import permissions
from rest_framework.permissions import IsAdminUser, SAFE_METHODS

class IsOwnerOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user

#--------------------------------------------------------------------------------
#-- Seeking to add a permission that allows the SuperAdmin User to Delete any User
#--------------------------------------------------------------------------------
class IsAdminUserOrReadOnly(IsAdminUser):

    def has_permission(self, request, view):
        is_admin = super(
            IsAdminUser, 
            self).has_permission(request, view)
        return request.method in SAFE_METHODS or is_admin