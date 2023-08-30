from django import forms

from petstagram_second.pets.models import Pet


class PetBaseForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ('name', 'date_of_birth', 'personal_pet_photo',)

        labels = {
            'name': 'Pet Name',
            'date_of_birth': 'Date of Birth',
            'personal_pet_photo': 'Link to Image',
        }

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter Name'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'personal_pet_photo': forms.URLInput(attrs={'placeholder': 'Enter Image'}),
        }


class PetCreateForm(PetBaseForm):
    pass


class PetEditForm(PetBaseForm):
    pass


class PetDeleteForm(PetBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
            field.required = False

