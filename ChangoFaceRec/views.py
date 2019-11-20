from rest_framework import viewsets

from ChangoFaceRec.serializers import GetIndexSerializer
from . import models
from . import serializers
from rest_framework.decorators import action
from rest_framework.response import Response
import face_recognition
import io
import base64


# Create your views here.


##@package Views
#En este modulo estan definidas las operaciones de la API
# * abm de personas
# * reconocimiento de personas


## get_encoding
# toma como parametro una imagen en base64 y devuelve los face_encodings
# que face-recognition va a usar para comparar la imagen de la cara con otras
# es importante que la imagen dada sea de una cara y no que contenga la cara ya que no se recorta la imagen
# @param base64: una imagen en base64

def get_encoding(base_64):
    image = face_recognition.load_image_file(io.BytesIO(base64.b64decode(base_64)))
    width = image.shape[0]
    height = image.shape[1]
    encoding = face_recognition.face_encodings(image, known_face_locations=[(0, width, height, 0)])
    return encoding[0]


## compare_faces
# toma como parametros una lista de encodings y otro encoding a comparar con los demas
# devuelve el indice del primer encoding de la lista con el que el encoding a comparar fue considerado la misma cara
# @param all_persons: una lista de encodings
# @param face: un enconding a comparar con la lista all_persons

def compare_faces(all_persons, face):
    results = face_recognition.compare_faces(all_persons, face)
    i = 0
    for x in results:
        if x:
            return i
        i += 1
    return -1


## get_all_encodings
# toma como parametro una lista de personas y devuelve una lista de los encodings de las caras de esas personas
# @param all_persons: lista de personas


def get_all_encodings(all_persons):
    encodings = []
    for x in all_persons:
        encodings.append(get_encoding(x.face))
    return encodings


class PersonViewSet(viewsets.ModelViewSet):
    ## ViewSet de persona
    # provee las operaciones de alta baja y modificacion de personas mediante la interfaz REST

    queryset = models.Person.objects.all()
    serializer_class = serializers.PeronsSerializer

    @action(detail=False, methods=['post'], serializer_class=GetIndexSerializer)
    ## get_index
    # Busca y devuelve el indice de la persona (o -1 si no se encuentra) dada una imagen de la cara codificada en
    # base 64
    def get_index(self, request):
        all_persons = models.Person.objects.all()
        picture = self.get_serializer(data=request.data)
        if picture.is_valid():
            picture = picture.data
            face = picture.get('face')
            print(face)
            index = compare_faces(get_all_encodings(all_persons), get_encoding(face))
            if index != -1:
                index = all_persons[index].id
            return Response(index)

        return Response("Error", status=500)
