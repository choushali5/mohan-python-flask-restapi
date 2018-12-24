# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 13:44:02 2018

@author: mohan.choushali
"""

from flask import Flask,request
from flask_restful import Resource,Api
from flask_jwt import JWT,jwt_required

from security import authenticate,identity

app = Flask(__name__)
app.secret_key = 'jose'
api = Api(app)
jwt = JWT(app,authenticate,identity) #/auth

items = []

class Item(Resource):
    
    #This is optimized code. leave for now
    '''def get(self,name):
        item = next(filter(lambda x : x['name']== name, items), None)
        return {'item':item},200 if item else 404'''
   
    @jwt_required()
    def get(self,name):
        for item in items:
            if(item['name'] == name):
                return item          
        return {'item' : None}, 404
    
    #This is optimized code. leave for now
    def post(self,name):
        if next(filter(lambda x : x['name']== name, items), None):
            return {'message':"An item with name '{}' already exists.".format(name)},404
        
        data = request.get_json()
        item = {'name':name, 'price':data['price'],'location':data['location']}
        items.append(item)
        return item, 201
    
'''def post(self,name):      
        data = request.get_json()
        item = {'name':name, 'price':data['price'],'location':data['location']}
        items.append(item)
        return item, 201'''

class ItemList(Resource):
    
    def get(self):
        return {'items' : items}
    

api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')

app.run(port=5005, debug=True)



