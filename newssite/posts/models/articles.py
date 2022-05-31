from django.db import models

from posts.models.category import Category

class Post(models.Model):
  title = models.CharField(max_length=150)
  body = models.CharField(max_length=700)
  photo = models.ImageField(upload_to='images/',blank=True)
  date = models.DateTimeField(auto_now_add=True,null=True)
  category = models.ForeignKey(Category,null=True,on_delete=models.CASCADE)

  def __str__(self):
    return self.title 

  @staticmethod # staticmetodni biz yaratgan madellarimiz hamma joyda ozinig ichki funksiyasi siftida taniydi

  def get_all_products():
    return Post.objects.all() # barcha postlarni chaqiradi, barcha obyektlarni 

  @staticmethod
  def get_all_products_by_categoryid(category_id):
    if category_id:
      return Post.objects.filter(category = category_id) # categoriya boyicha filtirlaydi
    else:
      return Post.get_all_products(); 



  
