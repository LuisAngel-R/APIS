from django import forms
from .models import Docente, Estudiante, Administrador,Personal, Categoria
from django.contrib.auth.hashers import make_password


class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = [
            'numero_trabajador', 'apellidos', 'nombres', 'telefono', 
            'fecha_inicio', 'fecha_finalizacion', 'username', 'password', 'qr_code'
        ]
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_finalizacion': forms.DateInput(attrs={'type': 'date'}),
            'password': forms.PasswordInput(),  # Esto asegura que el campo de contraseña se muestre como un input tipo 'password'
        }

    def save(self, commit=True):
        # Obtiene la instancia original
        docente = super(DocenteForm, self).save(commit=False)
        # Hashea la contraseña antes de guardar
        docente.password = make_password(docente.password)  # Asegúrate de importar make_password
        if commit:
            docente.save()
        return docente
    
    

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = [
            'matricula', 'nombres', 'apellidos', 'programa_educativo', 'qr_code', 'username', 'password', 'estado'
        ]
        widgets = {
            'password': forms.PasswordInput(),  # Esto asegura que el campo de contraseña se muestre como un input tipo 'password'
        }

    def save(self, commit=True):
        # Obtiene la instancia original
        estudiante = super(Estudiante, self).save(commit=False)
        # Hashea la contraseña antes de guardar
        estudiante.password = make_password(estudiante.password)  # Asegúrate de importar make_password
        if commit:
            estudiante.save()
        return estudiante
    
class AdministradorForm(forms.ModelForm):
    class Meta:
        model = Administrador
        fields = [
            'numero_trabajador', 'apellidos', 'nombres', 'telefono', 
            'fecha_inicio', 'fecha_finalizacion', 'username', 'password', 'qr_code'
        ]
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_finalizacion': forms.DateInput(attrs={'type': 'date'}),
            'password': forms.PasswordInput(),  # Esto asegura que el campo de contraseña se muestre como un input tipo 'password'
        }

    def save(self, commit=True):
        # Obtiene la instancia original
        administrador = super(AdministradorForm, self).save(commit=False)
        # Hashea la contraseña antes de guardar
        administrador.password = make_password(administrador.password)  # Asegúrate de importar make_password
        if commit:
            administrador.save()
        return administrador
    
class PersonalForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = [
            'numero_trabajador', 'apellidos', 'nombres', 'telefono', 
            'fecha_inicio', 'fecha_finalizacion', 'username', 'password', 'qr_code'
        ]
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_finalizacion': forms.DateInput(attrs={'type': 'date'}),
            'password': forms.PasswordInput(),  # Esto asegura que el campo de contraseña se muestre como un input tipo 'password'
        }

    def save(self, commit=True):
        # Obtiene la instancia original
        personal = super(PersonalForm, self).save(commit=False)
        # Hashea la contraseña antes de guardar
        personal.password = make_password(personal.password)  # Asegúrate de importar make_password
        if commit:
            personal.save()
        return personal


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = [
            'nombre', 'codigo'
        ]
    def save(self, commit=True):
        # Obtiene la instancia original
        categoria = super(CategoriaForm, self).save(commit=False)
        # Hashea la contraseña antes de guardar
        categoria.password = make_password(categoria.password)  # Asegúrate de importar make_password
        if commit:
            categoria.save()
        return categoria
    
class LoginForm(forms.Form):
    numero_trabajador = forms.CharField(label='Número de Trabajador', max_length=10)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)