# Class & Objects
# OBSERVAR main2.py

class User:  # Cria-se a classe
    def __init__(self, email, name, password, current_job_title): # __init__ paràmetro construtor // #self referencia para acessar variaveis
        self.email = email
        self.name = name
        self.password = password
        self.current_job_title = current_job_title

    def change_password(self, new_password):
        self.password = new_password

    def change_job_title(self, new_job_title):
        self.current_job_title =  new_job_title

    def get_user_info(self):
        print(f"User {self.name} currently work as a {self.current_job_title}. You contact them at {self.email}")

## Aqui, alguns exemplos

# app_user_one = User("jeca@hotmail.com", "Jeca Jequiti", "1234","DevOps Engineer")
# app_user_one.get_user_info()
#
# app_user_one = User("hunu_123@hotmail.com", "Marcondes", "janeteboquete","Faxineiro")
# app_user_one.get_user_info()


# app_user_one.change_job_title("DevOps Senior")
# app_user_one.get_user_info()