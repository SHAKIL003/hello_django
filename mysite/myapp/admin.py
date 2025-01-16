from django.contrib import admin
from .models import Pslmatches, Player, TeamReview, PlayerCertificate

# Register your models here.

class TeamReviewInline(admin.TabularInline):
    model = TeamReview
    extra = 1

class TeamVarietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_added')
    inlines = [TeamReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('team_players',)

class TeamCertificateAdmin(admin.ModelAdmin):
    list_display = ('team', 'certificate_number', 'issued_date', 'valid_until')

admin.site.register(Pslmatches, TeamVarietyAdmin)
admin.site.register(Player, StoreAdmin)
admin.site.register(PlayerCertificate, TeamCertificateAdmin)

# admin.site.register(Pslmatches)
