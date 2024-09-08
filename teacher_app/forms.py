from django import forms

class ImageForm(forms.Form):
    image = forms.ImageField(label='Choose a Picture', label_suffix='', widget=forms.FileInput(attrs={'class': 'image'}))

    def clean_image(self):
        image = self.cleaned_data['image']
        if not image:
            raise forms.ValidationError('You must upload an image')
        if image.size > 1024*1024*2:
            raise forms.ValidationError('Image size must be less than 2MB')
        return image
    