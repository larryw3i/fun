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

    list_display = ('user','get_wearticle_title', 'content', 'like', 'dislike', 'date_time' , 'content_length')

    search_fields = ['content', 'user__username']
    
    list_filter = ['content', 'user__username']

    ordering = ['date_time', 'user']

    list_per_page = 2

    list_max_show_all = 3

    exclude = ['like', 'dislike',]

    readonly_fields = ('content_length',)

    raw_id_fields = ('user', 'wearticle', )

    fieldsets = (
        (
            'Wearticle & user', 
            {
                'fields' : ('wearticle', 'user'),
                'description' : 'Wearticle & user'
            }
        ), 
        (
            'Content', 
            {
                'fields' : ('content','content_length'),
                'description' : 'Content'
            }
        )
    )

    def save_model(self, request, obj, form, change):
        if change and len(obj.content) > 10:
            self.message_user(
                request, 
                'a long comment'
            )
            obj.content += '(long)'
        super(CommentAdmin, self).save_model(request, obj, form, change)


    def content_length(self, obj):
        return len(obj.content)

    content_length.short_description = 'content length'

    def get_wearticle_title(self, obj):
        return obj.wearticle.title

    get_wearticle_title.short_description = 'article'

    def set_like_to_zero(self, request, queryset):
        rows_updated = queryset.update(like = 0)
        self.message_user(request, '%s like(s) be set to 0'%rows_updated )

    set_like_to_zero.short_description = 'set like to 0'


    def set_dislike_to_zero(self, request, queryset):
        rows_updated = queryset.update(dislike = 0)
        self.message_user(request, '%s dislike(s) be set to 0'%rows_updated )

    set_dislike_to_zero.short_description = 'set dislike to 0'

    pass
