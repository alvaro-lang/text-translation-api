from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.HistoryViewSet import HistoryViewSet
from .views.TranslateTextView import translate_text

router = DefaultRouter()
router.register(r'history', HistoryViewSet, basename='history')

urlpatterns = [
    path('', include(router.urls)),
    path('translate', translate_text, name='translate_text'),
]