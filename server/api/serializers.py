from rest_framework import serializers

from server.models import Voiture , ProblemeVoiture

class VoitureSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Voiture
        fields = ('id','matricule')


class ProblemeVoitureSerializer(serializers.ModelSerializer):
    voiture = VoitureSerializer()
    class Meta:
        model = ProblemeVoiture
        fields = ('voiture','nom_pb')