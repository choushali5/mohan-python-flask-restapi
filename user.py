# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 16:07:52 2018

@author: mohan.choushali
"""

class User:
    
    def __init__(self,_id,username,password):
        self.id = _id
        self.username = username
        self.password = password
        
#Now go in security.py and import user class there