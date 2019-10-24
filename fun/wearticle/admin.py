from django.contrib import admin

# Register your models here.


from wearticle.models import Wearticle, Comment

@admin.register(Wearticle)
class WearticleAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'uploaded_time')
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    actions = ['set_like_to_zero', 'set_dislike_to_zero']

    list_display = ('user', 'content', 'like', 'dislike', 'date_time')

    search_fields = ['content', 'user__username']

    def set_like_to_zero(self, request, queryset):
        rows_updated = queryset.update(like = 0)
        self.message_user(request, '%s like(s) be set to 0'%rows_updated )

    set_like_to_zero.short_description = 'set like to 0'


    def set_dislike_to_zero(self, request, queryset):
        rows_updated = queryset.update(dislike = 0)
        self.message_user(request, '%s dislike(s) be set to 0'%rows_updated )

    set_dislike_to_zero.short_description = 'set dislike to 0'

    pass
