from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
import google.generativeai as genai

from ..models.History import History
from ..serializers.TranslateTextSerializer import TranslateTextSerializer

@api_view(['POST'])
def translate_text(request):
    serializer = TranslateTextSerializer(data=request.data)

    if serializer.is_valid():
        source_text = serializer.validated_data['source_text']
        language = serializer.validated_data['language']
        style = serializer.validated_data['style']

        prompt = f"Translate {style} into {language} the following text literally, without explanation or interpretation and with only one answer: {source_text}"

        try:
            genai.configure(api_key=settings.GEMINI_API_KEY)
            model = genai.GenerativeModel("gemini-1.5-pro-latest")
            response = model.generate_content(prompt)

            text_translated = response.text

            if request.user.is_authenticated:
                History.objects.create(
                    user=request.user,
                    source_text=source_text,
                    translated_text=text_translated
                )

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'text_translated': text_translated}, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)