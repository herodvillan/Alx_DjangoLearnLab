from django import forms

class ExampleForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea, required=False)

#lets try this
