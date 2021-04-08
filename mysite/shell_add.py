from django.contrib.auth.models import User
from blog.models import Post 
# user = User.objects.get(username='admin')
# post = Post(
#     title = 'Another post',
#     slug = 'another-post',
#     body = 'post body',
#     author = user
#     )

# Post.objects.create(title='One more post', slug = 'one-more-post',body = 'post body', author = user)

#  post.title='New title'

all_posts = Post.objects.all()

post = Post.objects.get(id=1)
post.tags.add('music', 'jazz', 'django')
post.tags.all()
post.tags.remove('django')