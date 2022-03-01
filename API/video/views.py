from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Video
from .serializers import VideoSerializer
from django.http import Http404

# Create your views here.

#Clase Utilizada para definir los métodos HTTP que no requieren parametro ID para procesar operaciones.
class ListVideo(APIView):

	#Función HTTP-GET que permite obtener todos los registros del modelo API (Utilize Postman para consultar registros mediante la dirección URL: http://localhost:8000/videos/).
	def get(self, request):
		videos = Video.objects.all()
		video_json = VideoSerializer(videos, many=True)
		return Response(video_json.data)

	#Función HTTP-POST que permite crear un registro en el modelo API (Utilize Postman para agregar registros mediante la dirección URL: http://localhost:8000/videos/).
	def post(self, request):
		video_json = VideoSerializer(data=request.data) #Es un Marshall

		if video_json.is_valid():
			video_json.save()
			return Response(video_json.data, status=201)
		else:
			return Response(video_json.errors, status=400)

#Clase Utilizada para definir los métodos HTTP que su requieren parametro ID (primary key) para procesar operaciones.
class Detailvideo(APIView):

	#Función HTTP-GET que permite obtener los datos de un registro del modelo API (Utilize Postman para consultar un registro mediante la dirección URL: http://localhost:8000/videos/[ID]).
	def get(self, request, pk):
		try:
			video = Video.objects.get(pk = pk)
			video_json = VideoSerializer(video)
			return Response(video_json.data)
		except Video.DoesNotExist:
			raise Http404

	#Función HTTP-PUT que permite actualizar los datos de un registro del modelo API (Utilize Postman para editar registros mediante la dirección URL: http://localhost:8000/videos/[ID]).
	def put(self, request, pk):
		try:
			video = Video.objects.get(pk = pk)
			video_json = VideoSerializer(video, data=request.data)
			if video_json.is_valid():
				video_json.save()
				return Response(video_json.data)
			else:
				return Response(video_json.errors, status=400)
		except Video.DoesNotExist:
			raise Http404

	#Función HTTP-DELETE que permite eliminar los datos de un registro del modelo API (Utilize Postman para eliminar registros mediante la dirección URL: http://localhost:8000/videos/[ID]).
	def delete(self, request, pk):
		try:
			video = Video.objects.get(pk = pk)
			video.delete()
		except Video.DoesNotExist:
			raise Http404
