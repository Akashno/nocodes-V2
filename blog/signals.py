from django.contrib.auth.models import User
from django.db.models.signals import post_save

from blog.models import Post, Comment


def set_author_name(sender,instance,created,**kwargs):
    if created:
        instance.author_name = instance.author.short_title
        instance.save()


def set_user_name(sender,instance,created, **kwargs):
    if created:
        instance.user_name = instance.user.username
        instance.save()

def set_author_first_comment(sender, instance, created, **kwargs):
    if created:
        admin = User.objects.get(username='admin')
        comment = Comment(post=instance,user=admin,body='please feel free to share your thoughts on this story')
        comment.save()


post_save.connect(receiver=set_author_name,sender=Post)
post_save.connect(receiver=set_user_name, sender=Comment)
post_save.connect(receiver=set_author_first_comment, sender=Post)