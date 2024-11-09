

from rest_framework.permissions import BasePermission
from django.shortcuts import redirect

class IsAuthenticatedOrRedirect(BasePermission):
    login_url = '/admin/login/'

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            response = redirect(self.login_url)
            response['Location'] = self.login_url
            return False  
        return True
