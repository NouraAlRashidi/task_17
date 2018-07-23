from rest_framework.permissions import BasePermission



class IsOwnerOrIsStaff(BasePermission):
	message= "Not allowed to edit anything on this page. Get out!"
	def has_object_permission(self, request, view, obj):
		
		if request.user == obj.owner or request.user.is_staff:
			return True
		return False
