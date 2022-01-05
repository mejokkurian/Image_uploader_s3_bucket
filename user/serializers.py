from django.contrib.postgres import fields
from user.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import DropBox



class UserReg_Serialzer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all(),message=("Email already exists"))])
                                        
    class Meta:
        model = User
        fields =['id', 'name', 'password','mobile_number','email']
        
        extra_kwargs = {'password':{
        'write_only':True,
        'required' : True
        }}
        
    def create(self,validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    

class LoginSerializer(serializers.ModelSerializer):
     class Meta: 
        model = User
        fields =['email', 'password']
        
        extra_kwargs = {'password':{
        'write_only':True,
        'required' : True
        }}
        
class UserCostomize(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','name','email','mobile_number','password']
        
        extra_kwargs = {'password':{
        'write_only':True,
        'required' : True
        }}
        


class DropBoxSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = DropBox
        fields = '__all__'
        
        
