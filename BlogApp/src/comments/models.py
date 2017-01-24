from __future__ import unicode_literals

from django.conf import settings
from django.db import models

# Create your models here.

from posts.models import Post

class Comment(models.Model):
	user        = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	post 		= models.ForeignKey(Post, related_name='comments')
	content     = models.TextField()
	timestamp   = models.DateTimeField(auto_now_add=True)


	def __unicode__(self):
		return "{} commented '{}' on {}".format(self.user, self.content, self.post) 


