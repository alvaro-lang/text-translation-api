from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from ..models.History import History
from ..serializers.HistorySerializer import HistorySerializer

class HistoryViewSet(ModelViewSet):
    serializer_class = HistorySerializer
    http_method_names = ['get']
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return History.objects.filter(user=self.request.user).order_by('-id')[:5]
