from django.contrib import admin

from abonnement.models import Abonnement


class abonnementAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return True
    def has_delete_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return True

admin.site.register(Abonnement, abonnementAdmin)