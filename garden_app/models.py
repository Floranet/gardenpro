from django.db import models
from django.conf import settings

# Create your models here.
class user_reg(models.Model):
    STATUS=(
        ('applied','Applied'),
        ('approved','Approved'),
        ('rejected','Rejected'),
    )
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(unique=True,max_length=100)
    phone = models.CharField(max_length=10)
    password=models.CharField(max_length=100)
    confirm_password=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    status=models.CharField(max_length=20,choices=STATUS,default='applied')
    def __str__(self):
        return self.first_name
    
class prof_reg(models.Model):
    STATUS=(
        ('applied','Applied'),
        ('approved','Approved'),
        ('rejected','Rejected'),
    )
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    em=models.EmailField(unique=True,max_length=100)
    phno = models.CharField(max_length=10)
    passw = models.CharField(max_length=100)
    confirm_pass=models.CharField(max_length=100)
    add=models.CharField(max_length=100)
    status=models.CharField(max_length=20,choices=STATUS,default='applied')
    def __str__(self):
        return self.fname
    
class Feed_user(models.Model):
    RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        ]
        
    feedback_text = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rating: {self.rating}, Feed_user: {self.feedback_text[:50]}..."
    
class Feed_prof(models.Model):
    RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        ]
        
    feedback_text = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rating: {self.rating}, Feed_prof: {self.feedback_text[:50]}..."
            
# class Category(models.Model):
#     name = models.CharField(max_length=100)
#     user = models.ForeignKey(user_reg, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.name} (User: {self.user.first_name})"


# Checklist model
class Checklist(models.Model):
    task = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(user_reg, on_delete=models.CASCADE)

    def __str__(self):
        return self.task



class Reminder(models.Model):
    title = models.CharField(max_length=200)
    reminder_text = models.TextField(blank=True)
    date = models.DateField()
    user = models.ForeignKey(user_reg, on_delete=models.CASCADE)
    task_title = models.CharField(max_length=200, blank=True, null=True)  # Title of the task
    task_status = models.BooleanField(default=False)
    time = models.TimeField()
    def __str__(self):
        return self.title

    
class products(models.Model):
    img=models.ImageField(blank=True,null=True)
    prod_name=models.CharField(max_length=100)
    prod_type=models.CharField(max_length=100)
    quantity=models.IntegerField()
    price=models.CharField(max_length=100)
    seller_name=models.CharField(max_length=100)
    seller_phone = models.CharField(max_length=10)

    def __str__(self):
        return self.prod_name
    



class cart(models.Model):
    prod_name = models.CharField(max_length=100)
    prod_type = models.CharField(max_length=100)
    quantity = models.IntegerField()  # Store as integer
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Store as decimal
    seller_name = models.CharField(max_length=100)
    seller_phone = models.CharField(max_length=10)
    first_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.prod_name

class pay(models.Model):
    prod_name = models.CharField(max_length=100)
    quantity = models.IntegerField()  # Store as integer
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Store as decimal
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.prod_name


from django.db import models

class resource(models.Model):
    title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to='videos/', blank=True, null=True)
    image_file = models.ImageField(upload_to='images/', blank=True, null=True)
    description = models.TextField()
    name = models.CharField(max_length=100)  # Name of the uploader

    def __str__(self):
        return self.title

    def get_media_url(self):
        if self.video_file:
            return self.video_file.url
        elif self.image_file:
            return self.image_file.url
        return None

    
class shop(models.Model):
    name = models.CharField(max_length=100)
    shopid =models.IntegerField(unique=True)
    email =models.EmailField(max_length=100)
    phone =models.CharField(max_length=10)
    description =models.TextField(max_length=100)
    location =models.CharField(max_length=100)
    img =models.ImageField(upload_to='shopimages/')
    category_choices =(
        ('Plants','Plants'),
        ('Tools','Tools'),
        ('Seeds','Seeds')
    )
 

    category =models.CharField(choices=category_choices,max_length=100)
    professional=models.ForeignKey(prof_reg,on_delete=models.CASCADE)

class Task(models.Model):
    title = models.CharField(max_length=200)
    status = models.BooleanField(default=False)  # False means incomplete, True means completed
    user = models.ForeignKey('user_reg', on_delete=models.CASCADE)  # User associated with the task
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title
    

from django.db import models
from django.utils.timezone import now

class ChatMessage(models.Model):
    sender = models.CharField(max_length=100)  # Artist or Buyer username
    receiver = models.CharField(max_length=100)  # Receiver's username
    content = models.TextField()
    timestamp = models.DateTimeField(default=now)
    media=models.FileField(upload_to='chat_media/',null=True,blank=True)
    
    
    
    
    
class pReminder(models.Model):
    title = models.CharField(max_length=200)
    reminder_text = models.TextField(blank=True)
    date = models.DateField()
    user = models.ForeignKey(prof_reg, on_delete=models.CASCADE)
    task_title = models.CharField(max_length=200, blank=True, null=True)  # Title of the task
    task_status = models.BooleanField(default=False)
    time = models.TimeField()
    def __str__(self):
        return self.title
    
    
    
    
class pTask(models.Model):
    title = models.CharField(max_length=200)
    status = models.BooleanField(default=False)  # False means incomplete, True means completed
    user = models.ForeignKey(prof_reg, on_delete=models.CASCADE)  # User associated with the task
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title
    
# Community
from django.db import models
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Photo(models.Model):
    # Use a generic foreign key to handle both user types
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    user = GenericForeignKey('content_type', 'object_id')
    
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='photos/')
    created_at = models.DateTimeField(default=timezone.now)
    views = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.title
    
    @property
    def like_count(self):
        return self.like_set.filter(is_like=True).count()
    
    @property
    def comment_count(self):
        return self.comment_set.filter(parent=None).count()

class Like(models.Model):
    # Generic foreign key for user
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    user = GenericForeignKey('content_type', 'object_id')
    
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    is_like = models.BooleanField()
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        unique_together = [['content_type', 'object_id', 'photo']]

class Comment(models.Model):
    # Generic foreign key for user
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    user = GenericForeignKey('content_type', 'object_id')
    
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    created_at = models.DateTimeField(default=timezone.now)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return f'{self.user}: {self.text[:50]}'

class Share(models.Model):
    SHARE_PLATFORMS = [
        ('WA', 'WhatsApp'),
        ('FB', 'Facebook'),
        ('TW', 'Twitter'),
        ('LI', 'LinkedIn'),
        ('EM', 'Email'),
    ]
    
    # Generic foreign key for user
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    user = GenericForeignKey('content_type', 'object_id')
    
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    platform = models.CharField(max_length=2, choices=SHARE_PLATFORMS)
    shared_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'{self.user} shared {self.photo.title} on {self.get_platform_display()}'

class PhotoView(models.Model):
    # Generic foreign key for user
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    user = GenericForeignKey('content_type', 'object_id')
    
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    viewed_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        unique_together = [['content_type', 'object_id', 'photo']]
        
    def __str__(self):
        return f'{self.user} viewed {self.photo.title}'
    



