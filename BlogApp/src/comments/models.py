from __future__ import unicode_literals
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from django.db import models

# Create your models here.

from posts.models import Post

class Comment(models.Model):
	user           = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	post 		   = models.ForeignKey(Post, related_name='comments')
	parent         = models.ForeignKey("self", null=True, blank=True)
	content        = models.TextField()
	timestamp      = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ["-timestamp"]


	def __unicode__(self):
		if self.parent is not None:
			return "{} responded '{}' to {}'s comment '{}'".format(self.user, self.content, self.parent.user, self.parent.content) 
		return "{} commented '{}' on {}".format(self.user, self.content, self.post) 

	def is_parent(self):
		if self.parent is None:
			return True
		else:
			return False		

	def is_child(self):
		if self.parent is not None:
			return True
		else:	
			return False		

	def get_children(self):
		if self.is_child():
			return None
		else:
			return Comment.objects.filter(parent=self)			


