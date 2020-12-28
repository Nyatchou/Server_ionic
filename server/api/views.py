from rest_framework import generics
from server.models import ProblemeVoiture, Voiture
from .serializers import ProblemeVoitureSerializer, VoitureSerializer


class ProblemeVoitureViews(generics.ListAPIView):
    serializer_class = ProblemeVoitureSerializer
    queryset = ProblemeVoiture.objects.all()

    def get_queryset(self):
        matricule=self.kwargs['matricule']
        voiture = Voiture.objects.filter(matricule = matricule)
        if len(voiture) is not 0:
            idv = voiture[0].id
            return ProblemeVoiture.objects.filter(voiture = idv)
        return ProblemeVoiture.objects.filter(voiture = 0)

class VoitureViews(generics.ListAPIView):
    serializer_class = VoitureSerializer
    queryset = Voiture.objects.all()