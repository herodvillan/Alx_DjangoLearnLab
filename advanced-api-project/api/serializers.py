from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']  # match model fields

    def validate_publication_year(self, value):
        if value > 2025:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

