from rest_framework.views import APIView
from rest_framework.response import Response
from . import models
from .serializers import   QuestionSerializer , AnswerSerializer
from rest_framework.permissions import IsAuthenticated , IsAdminUser , IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from permissions import IsOwnerOrReadOnly
# Create your views here.


# class Home(APIView):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     def get(self, req):
#         # get params with GET method
#         # name = req.query_params["name"]
#
#         persons = models.Person.objects.all()
#         # if send many arg to ser must many=True
#         # when info read from db we must put in instance
#         # instance just for get method
#         ser_data = PersonSerializer(instance=persons , many=True)
#         # ser_data.data = return value of PersonSerializer class
#         return Response(data=ser_data.data)

class QuestionView(APIView):
    authentication_classes = [TokenAuthentication]
    serializer_class = QuestionSerializer
    def get(self,request):
        question = models.Question.objects.all()
        ser_data = QuestionSerializer(instance=question,many=True)
        return Response(ser_data.data ,status=status.HTTP_200_OK )


class QuestionCreateView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = QuestionSerializer
    def post(self,request):
        ser_data = QuestionSerializer(data=request.POST)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data,status=status.HTTP_201_CREATED)
        return Response(ser_data.errors,status=status.HTTP_400_BAD_REQUEST)


class QuestionUpdateView(APIView):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = QuestionSerializer
    def put(self, request, pk):
        question = models.Question.objects.get(pk=pk)
        # for check to sure use permissions
        self.check_object_permissions(request,question)
        # اطلاعات data روی instance اعمال میشه و partials برای وقتی ک فقط یک فیلد را عوض میکنیم
        ser_data = QuestionSerializer(instance=question, data=request.POST, partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(data=ser_data.data, status=status.HTTP_200_OK)
        return Response(data=ser_data.errors, status=status.HTTP_400_BAD_REQUEST)

class QuestionDeleteView(APIView):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = QuestionSerializer
    def delete(self,request,pk):
        question = models.Question.objects.get(pk=pk)
        self.check_object_permissions(request,question)
        question.delete()
        return Response("deleted successfully",status=status.HTTP_200_OK)