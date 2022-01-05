from user.models import User
from .serializers import UserReg_Serialzer,LoginSerializer,UserCostomize,DropBoxSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate,login
from rest_framework.response import Response
from rest_framework import status, viewsets,parsers
from rest_framework.views import APIView
from rest_framework import mixins 
from .models import DropBox


# Create your views here.

class UserRegistration(APIView):
    def post(self, request):
        try:
            name = request.data.get('name')
            password = request.data.get('password')
            mobile_number = request.data.get('mobile_number')
            email = request.data.get('email')
            user = User.objects.create_user(name=name,password=password,mobile_number=mobile_number,email=email)
            user.save()
            message = {"msg" : "User created successfully.","email":email}
            return Response(message,status=status.HTTP_201_CREATED)
        except:
            message = {"error" : "clients side error or user details already in use"}
            return Response(message,status=status.HTTP_400_BAD_REQUEST)
        

#------------- user login view ----------------- #    
class UserLogin(APIView): 
    def post(self, request):
        try:
            email = request.data.get('email')
            password = request.data.get('password')
            
            user = authenticate(username=email, password=password)
            serializers = LoginSerializer(user)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    refresh = RefreshToken.for_user(user)
                    
                    return Response({
                        "user"  : serializers.data,
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                    })
                else:
                    message = {"error":"user is not activate"}
                    return Response(message,status=status.HTTP_404_NOT_FOUND)
            else:
                message = {"error" : "invalide password or username"}
                return Response(message,status=status.HTTP_404_NOT_FOUND)
        except:
            message = {"error" : "clients side error"}
            return Response(message,status=status.HTTP_400_BAD_REQUEST)
        
    
    
# ------------- user edit,delete,update ---------- #
class Users(viewsets.GenericViewSet,mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,mixins.DestroyModelMixin,mixins.ListModelMixin):
    authentication_classes =  [JWTAuthentication]
    permission_classes     =  [IsAuthenticated]
    queryset               =  User.objects.all()
    serializer_class = UserCostomize
    
    

class DropBoxViewset(viewsets.ModelViewSet):
    queryset = DropBox.objects.all()
    serializer_class = DropBoxSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    http_method_names = ['get', 'post', 'patch', 'delete']
    
    



