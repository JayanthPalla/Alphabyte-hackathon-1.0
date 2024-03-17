from rest_framework import permissions
from .models import ApplicantUser

class IsApplicantUser(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user is an instance of App1User and is authenticated
        return request.user.is_authenticated and isinstance(request.user, ApplicantUser)
