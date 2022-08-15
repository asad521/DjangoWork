from django.contrib.auth.signals import  user_logged_in, user_logged_out,user_login_failed
from django.contrib.auth.models import User

def login_sucess(sender, request, user, **kwargs):
    print("------------------")
    print("Logged in User--------Run Intro")
    print("sender:":sender)
    print("reqeust:":request)
    print("User:":user)
    print(f"Kwargs:{kwargs}")
    print('234234')
    
    user_logged_in.connect(login_sucess, success=User)