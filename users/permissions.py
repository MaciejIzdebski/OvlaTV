from rest_framework import permissions
from . import models
import json

class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Write permissions are only allowed to the owner of the obj.
        return obj.person.id == request.user.id


class IsPersonOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, person):
        # Write permissions are only allowed to the owner of the obj.
        return person.client.user.id == request.user.id


class IsClientOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Write permissions are only allowed to the owner of the obj.
        return obj.user.id == request.user.id