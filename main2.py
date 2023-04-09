###############################
### OBSERVAR Class & Objects###
###############################

from ClassEObjects import User
from post import Post

app_user_one = User("jeca@hotmail.com", "Jeca Jequiti", "1234","DevOps Engineer")
app_user_one.get_user_info()

app_user_two = User("hunu_123@hotmail.com", "Marcondes", "janete123","Faxineiro")
app_user_one.get_user_info()

new_post = Post("Limpando o banheiro no momento", app_user_two.name)
new_post.get_post_info()
