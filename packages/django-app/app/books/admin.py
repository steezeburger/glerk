from django.contrib import admin, messages

from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_at',
        'modified_at',
        'deleted_at',
        'is_active',
        'uuid',
        'title',
        'isbn',
        'publication_date',
        'author',
    )
    list_filter = (
        'created_at',
        'modified_at',
        'deleted_at',
        'is_active',
        'publication_date',
    )
    date_hierarchy = 'created_at'

    actions = ['force_delete_books']

    @admin.action(description='!!! FORCE DELETE BOOKS !!!')
    def force_delete_books(self, request, queryset):
            queryset.delete(force_delete=True)
            self.message_user(
                request,
                "Force Deleted Books!",
                messages.SUCCESS)
