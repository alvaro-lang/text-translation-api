from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from openai import OpenAI

from ..serializers.TranslateTextSerializer import TranslateTextSerializer

@api_view(['POST'])
def translate_text(request):
    serializer = TranslateTextSerializer(data=request.data)

    if serializer.is_valid():
        source_text = serializer.validated_data['source_text']
        language = serializer.validated_data['language']
        style = serializer.validated_data['style']

        prompt = f"Translate {style} into {language} this text: {source_text}"

        input_tokens = len(prompt) / 4
        max_tokens = int(input_tokens * 2)

        try:
            client = OpenAI(api_key=settings.OPENAI_API_KEY)
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": prompt}
                ],
                max_tokens=max_tokens
            )
            text_translated = response.choices[0].text.strip()

        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response({'text_translated': text_translated}, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)