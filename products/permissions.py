from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)
    

from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsProductAdminOrHasPermission(BasePermission):
    """
    السماح بالقراءة للجميع، والتعديل فقط لمن لديهم الصلاحية المحددة.
    """
    required_permission = 'manage_products'

    def has_permission(self, request, view):
        # السماح بالقراءة للجميع
        if request.method in SAFE_METHODS:
            return True

        # السماح بالتعديل فقط لمن يمتلك الصلاحية
        if request.user.is_authenticated:
            if hasattr(request.user, 'profile'):
                return self.required_permission in request.user.profile.permissions

        return False


class IsBrandAdminOrHasPermission(BasePermission):
    """
    السماح بالقراءة للجميع، والتعديل فقط لمن لديهم الصلاحية المحددة.
    """
    required_permission = 'manage_brands'

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        if request.user.is_authenticated:
            if hasattr(request.user, 'profile'):
                return self.required_permission in request.user.profile.permissions

        return False


class IsCategoryAdminOrHasPermission(BasePermission):
    """
    السماح بالقراءة للجميع، والتعديل فقط لمن لديهم الصلاحية المحددة.
    """
    required_permission = 'manage_categories'

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        if request.user.is_authenticated:
            if hasattr(request.user, 'profile'):
                return self.required_permission in request.user.profile.permissions

        return False


class IsSubCategoryAdminOrHasPermission(BasePermission):
    """
    السماح بالقراءة للجميع، والتعديل فقط لمن لديهم الصلاحية المحددة.
    """
    required_permission = 'manage_subcategories'

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        if request.user.is_authenticated:
            if hasattr(request.user, 'profile'):
                return self.required_permission in request.user.profile.permissions

        return False


# from rest_framework.permissions import BasePermission, SAFE_METHODS

# class IsProductAdminOrHasPermission(BasePermission):
#     """
#     السماح بالقراءة للجميع، والتعديل فقط للمشرفين أو من لديهم الصلاحية المحددة.
#     """
#     required_permission = 'manage_products'

#     def has_permission(self, request, view):
#         # السماح بالقراءة للجميع
#         if request.method in SAFE_METHODS:
#             return True

#         # التحقق إذا كان المستخدم مشرفًا أو يمتلك الصلاحية في حقل permissions
#         if request.user.is_authenticated:
#             if request.user.is_staff:
#                 return True
#             if hasattr(request.user, 'profile'):
#                 return self.required_permission in request.user.profile.permissions

#         return False


# class IsBrandAdminOrHasPermission(BasePermission):
#     """
#     السماح بالقراءة للجميع، والتعديل فقط للمشرفين أو من لديهم الصلاحية المحددة.
#     """
#     required_permission = 'manage_brands'

#     def has_permission(self, request, view):
#         if request.method in SAFE_METHODS:
#             return True

#         if request.user.is_authenticated:
#             if request.user.is_staff:
#                 return True
#             if hasattr(request.user, 'profile'):
#                 return self.required_permission in request.user.profile.permissions

#         return False


# class IsCategoryAdminOrHasPermission(BasePermission):
#     """
#     السماح بالقراءة للجميع، والتعديل فقط للمشرفين أو من لديهم الصلاحية المحددة.
#     """
#     required_permission = 'manage_categories'

#     def has_permission(self, request, view):
#         if request.method in SAFE_METHODS:
#             return True

#         if request.user.is_authenticated:
#             if request.user.is_staff:
#                 return True
#             if hasattr(request.user, 'profile'):
#                 return self.required_permission in request.user.profile.permissions

#         return False


# class IsSubCategoryAdminOrHasPermission(BasePermission):
#     """
#     السماح بالقراءة للجميع، والتعديل فقط للمشرفين أو من لديهم الصلاحية المحددة.
#     """
#     required_permission = 'manage_subcategories'

#     def has_permission(self, request, view):
#         if request.method in SAFE_METHODS:
#             return True

#         if request.user.is_authenticated:
#             if request.user.is_staff:
#                 return True
#             if hasattr(request.user, 'profile'):
#                 return self.required_permission in request.user.profile.permissions

#         return False
