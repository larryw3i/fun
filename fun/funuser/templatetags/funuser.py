
from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def get_funuser_name(context, user):
    funuser = Funuser.objects.filter(user=user).first()
    return funuser.full_name if (funuser and len(funuser.full_name) > 0) \
        else user.username


@register.simple_tag(takes_context=True)
def get_funuser_avatar_url(context, user):
    funuser = Funuser.objects.filter(user=user).first()
    return reverse(
            'funfile:get_file',
            kwargs={"file_id": funuser.avatar.name}
        ) \
        if (funuser and len(funuser.avatar.name) > 0) \
        else (settings.STATIC_URL + 'images/x_dove.webp')