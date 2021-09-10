from maskdetector.predict import Predict
from django.http.response import JsonResponse
from maskdetector.maskserializer import MaskSerializer
from django.shortcuts import render

from django.http import JsonResponse

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.files.storage import default_storage


from PIL import Image
from io import BytesIO



import base64, secrets
from django.core.files.base import ContentFile



# Create your views here.

def index(request):
    return render(request, "maskdetector/maskpredict.html")
    

class PredictMas(APIView):
    
    def post(self, request, format=None):
        print("inside post")
        data = request.data
        serializer = MaskSerializer(data=data)
        
        if serializer.is_valid():
             _format, _dataurl       = serializer.data["image"].split(';base64,')
             _filename, _extension   = secrets.token_hex(20), _format.split('/')[-1]
             file = ContentFile( base64.b64decode(_dataurl), name=f"{_filename}.{_extension}")
             path = default_storage.save("static/"+file.name,file)
             print(path)
             p = Predict()
             base64_image = p.predict(path)
             
             return Response({"image": base64_image}, status= status.HTTP_200_OK)

        return Response({"error":"Something went wrong"}, status= status.HTTP_400_BAD_REQUEST)             