from django.db import models

# Create your models here.
class Account(models.Model):
    """账户表"""
    username = models.CharField(max_length=64,unique=True)
    email = models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=255)
    register_data = models.DateTimeField(auto_now_add=True)
    signature = models.CharField("签名",max_length=255,null=True,blank=True)
    class Meta:
        verbose_name_plural = '账户'
    def __str__(self):
        return self.username

class Article(models.Model):
    title = models.CharField(max_length=255,unique=True)
    content = models.TextField()
    account = models.ForeignKey("Account",on_delete=models.CASCADE)
    tags = models.ManyToManyField("Tag",null=True)
    pub_date = models.DateField(auto_now_add=True)
    class Meta:
        verbose_name_plural = '文章'

    def get_comment(self):
        return 10

    def get_tages(self):
        return ','.join([i.name for i in self.tags.all()])

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=64,unique=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name