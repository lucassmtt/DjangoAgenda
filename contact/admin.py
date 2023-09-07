from django.contrib import admin

from contact.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'email',
    ordering = ('-id',)
    # list_filter = ('created_date'), # as the name said, filter by created date
    search_fields = ('id', 'first_name', 'last_name', 'email')
    list_per_page = 20
    list_max_show_all = 200