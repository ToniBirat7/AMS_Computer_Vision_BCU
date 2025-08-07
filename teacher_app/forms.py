<<<<<<< HEAD
<<<<<<< HEAD
from django import forms
from auth_app.models import Teacher

class ImageForm(forms.Form):
    image = forms.ImageField(
        label='Choose a Picture',
        label_suffix='',
        widget=forms.FileInput(attrs={
            'class': 'image',
            'accept': 'image/*'  # Accept only image files
        })
    )

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            # Check file size (2MB max)
            if image.size > 2 * 1024 * 1024:
                raise forms.ValidationError('Image size must be less than 2MB')
            
            # Check file type
            if not image.content_type.startswith('image/'):
                raise forms.ValidationError('Please upload a valid image file')
            
            return image
        return None
=======
=======
>>>>>>> 0d19833 (fix: contribution fix)
from django import forms
from auth_app.models import Teacher

class ImageForm(forms.Form):
<<<<<<< HEAD
    image = forms.ImageField(label='Choose a Picture', label_suffix='', widget=forms.FileInput(attrs={'class': 'image'}))

    def clean_image(self):
        image = self.cleaned_data['image']
        if not image:
            raise forms.ValidationError('You must upload an image')
        if image.size > 1024*1024*2:
            raise forms.ValidationError('Image size must be less than 2MB')
        return image

class TeacherEditForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = [
            'address','primary_number','secondary_number','dob','sex'
        ]
        widgets = {
            'dob': forms.TextInput(attrs={
                'disabled' : True
            }),
            'sex': forms.Select(attrs={
                'disabled' : True
            })
        }
>>>>>>> ba89ca1 (docs: fix contribution)
=======
    image = forms.ImageField(
        label='Choose a Picture',
        label_suffix='',
        widget=forms.FileInput(attrs={
            'class': 'image',
            'accept': 'image/*'  # Accept only image files
        })
    )

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            # Check file size (2MB max)
            if image.size > 2 * 1024 * 1024:
                raise forms.ValidationError('Image size must be less than 2MB')
            
            # Check file type
            if not image.content_type.startswith('image/'):
                raise forms.ValidationError('Please upload a valid image file')
            
            return image
        return None
>>>>>>> 0d19833 (fix: contribution fix)
