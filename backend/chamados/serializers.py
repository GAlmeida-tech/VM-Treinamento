from rest_framework import serializers

from . models import Chamados

class Chamados_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Chamados
        fields= '__all__'

