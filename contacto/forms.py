from django import forms

class FormularioContacto(forms.Form):

    nombre = forms.CharField(label='Nombre', required=True, max_length=100)
    email = forms.EmailField(label='Email', required=True)
    contenido = forms.CharField(label='Mensaje', required=True, max_length=800, widget=forms.Textarea)


    #your_name = forms.CharField(label='Your name', max_length=100)