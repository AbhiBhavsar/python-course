from django import forms


class ReviewForm(forms.Form):
    username = forms.CharField(label="Enter username", max_length=10, error_messages={
        "required": 'Cannot be empty',
        "max_length": "10 char allowed"
    })
