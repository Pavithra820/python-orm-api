from flask_restful import  Resource
from app.user.user_tables import User
from app import db
from flask import request
from flask_jwt_extended import create_access_token,jwt_required,get_jwt_identity

class GetUsers(Resource):
    def get(self):
        user = User.query.all()
        if user:
            return {'username': user.username, 'email':user.email}
        else:
            return {'message':'User not found'},404
        
    # to create users
        
    def post(self):
        try:
            data = request.get_json()
            new_user = User (
                username=data.get('username'),
                password=data.get('password'),
                email=data.get('email'),
                mobile=data.get('mobile'),
                city=data.get('city'),
                designation=data.get('designation')


            )
            db.session.add(new_user)
            db.session.commit()
            # generate access token using 
            access_token = create_access_token(identity=new_user.id)
       
            return {'message':'User registered sucessfully'},201
        except Exception as e:
            return {'message':'User registration failed','token':access_token},500


# logic for use login

class UserLogin(Resource):
    def post(self):
        
        try:
            data = request.get_json()
         
            username=data.get('username'),
            password=data.get('password'),
               
# check if the user exist in db
            user=User.query.filter_by(username=username).first()
            if user and user.password == data['password']:
                access_token = create_access_token(identity=user.id)
                return {'access_token':access_token},200
                # login to authenticate
                
            return {'message':'invalid password'},401
           
           
        except Exception as e:
            print(e)
            return {'message':'User registration failed'},500

# api to get information
class userInfo(Resource):
    try:
            
        @jwt_required()
        def get(self):
                current_user_id=get_jwt_identity()
                user=User.query.get(current_user_id)
                user_data ={
                    'id': user.id,
                    'username':user.username,
                    'email':user.email,
                    'mobile':user.mobile,
                    'city':user.city,
                    'designation':user.designation
                }
         
                return user_data,200
        
        
    except Exception as e:
        print(e)
        
        
