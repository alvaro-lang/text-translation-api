from rest_framework import serializers

class TranslateTextSerializer(serializers.Serializer):
    source_text = serializers.CharField()
    language = serializers.CharField(max_length=50)
    style = serializers.ChoiceField(choices=['formally', 'informally'])

    def to_internal_value(self, data):
        if 'style' in data:
            data['style'] = data['style'].lower()
        
        return super().to_internal_value(data)