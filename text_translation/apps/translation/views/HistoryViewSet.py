from rest_framework.viewsets import ModelViewSet

from ..models.History import History
from ..serializers.HistorySerializer import HistorySerializer

class HistoryViewSet(ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer

    http_method_names = ['get', 'post']