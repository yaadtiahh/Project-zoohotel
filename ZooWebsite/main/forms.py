from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'text', 'avatar']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ваше имя'}),
            'text': forms.Textarea(attrs={'placeholder': 'Ваш отзыв'}),
        }
