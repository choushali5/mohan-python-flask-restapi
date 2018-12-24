# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 15:55:30 2018

@author: mohan.choushali
"""
from werkzeug.security import safe_str_cmp
from user import User
#In memory database we are suing here like json and only for 1 user right now

#Now this users can be optimized again
'''users = [        
            {
                    'id':1,
                    'username':'bob',
                    'password':'abc'
            }
        ]'''

users = [
        User(1,"bob","asdf")
        ]

#Now this username_mapping can be optimized again

'''username_mapping = {'bob':{
                    'id':1,
                    'username':'bob',
                    'password':'abc'
            }
}'''

username_mapping = {u.username : u for u in users}

#Now this userid_mapping can be optimized again

'''userid_mapping = {'1':{
                    'id':1,
                    'username':'bob',
                    'password':'abc'
            }
}'''

userid_mapping = {u.id : u for u in users}

def authenticate(username,password):
    user= userid_mapping.get(username,None)
    #if user and user.password == password:
    if user and safe_str_cmp(user.password,password):
        return user


def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id,None)