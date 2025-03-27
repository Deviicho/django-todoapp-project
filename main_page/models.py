from django.db import models
from django.contrib.auth.models import User

class List(models.Model):
    name = models.CharField(max_length=13 , null=False)
    its_User = models.ForeignKey(User , on_delete=models.CASCADE)
    #maybe add an is_empty to use it in the michanism of what to show if its empty or not
    
    def task_count(self):
        """Returns the number of tasks in this list."""
        return self.task_set.count()

    def can_add_task(self):
        """Checks if the list can accept more tasks."""
        MAX_TASKS_PER_LIST = 8  # Set your max number of tasks here
        return self.task_count() < MAX_TASKS_PER_LIST

    @staticmethod
    def can_user_create_list(user):
        """Checks if the user can create more lists."""
        MAX_LISTS_PER_USER = 20  # Set your max number of lists here
        return List.objects.filter(its_User=user).count() < MAX_LISTS_PER_USER
    
    class Meta:
        # Ensure unique list names per user
        constraints = [
            models.UniqueConstraint(fields=['name', 'its_User'], name='unique_list_name_per_user')
        ]
    
    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=50 , null=False)
    is_checked = models.BooleanField(default=False)
    its_List = models.ForeignKey(List , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']
        
        constraints = [
            models.UniqueConstraint(fields=['name', 'its_List' , 'is_checked' , 'created_at'], name='unique_task_name_per_list')
        ]
    
    def __str__(self):
        return self.name