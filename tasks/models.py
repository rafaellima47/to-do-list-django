from django.db import models
from django.contrib.auth.models import User

class TaskModel(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	title = models.CharField(max_length=200)
	description = models.TextField(null=True, blank=True)
	complete = models.BooleanField(default=False)

	created = models.DateField(auto_now_add=True)
	updated = models.DateField(auto_now=True)

	def __str__(self):
		if len(self.title) > 36:
			return self.title[:36] + "..."
		return self.title	

	class Meta:
		order_with_respect_to = 'user'

