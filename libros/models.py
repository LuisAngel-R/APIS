from django.db import models

class Docente(models.Model):
    numero_trabajador = models.CharField(max_length=15)
    apellidos = models.CharField(max_length=50)
    nombres = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    fecha_inicio = models.DateField()  # Debe tener un valor
    fecha_finalizacion = models.DateField()  # Puede ser nulo si sigue activo
    estado = models.BooleanField(default=True)  # Campo para indicar si está activo
    username = models.CharField(max_length=30, unique=True)  # Asegura que el nombre de usuario sea único
    password = models.CharField(max_length=128)  # Almacena la contraseña hasheada
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"
    
class Estudiante(models.Model):
    matricula = models.CharField(max_length=20)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    programa_educativo = models.CharField(max_length=100)
    username = models.CharField(max_length=30, unique=True)  
    password = models.CharField(max_length=128)  
    estado = models.BooleanField(default=True)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

class Administrador(models.Model):
    numero_trabajador = models.CharField(max_length=10)
    apellidos = models.CharField(max_length=50)
    nombres = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    fecha_inicio = models.DateField()  # Debe tener un valor
    fecha_finalizacion = models.DateField()  # Puede ser nulo si sigue activo
    estado = models.BooleanField(default=True)  # Campo para indicar si está activo
    username = models.CharField(max_length=30, unique=True)  # Asegura que el nombre de usuario sea único
    password = models.CharField(max_length=128)  
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"
    
class Personal(models.Model):
    numero_trabajador = models.CharField(max_length=10)
    apellidos = models.CharField(max_length=50)
    nombres = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    fecha_inicio = models.DateField()  # Debe tener un valor
    fecha_finalizacion = models.DateField()  # Puede ser nulo si sigue activo
    estado = models.BooleanField(default=True)  # Campo para indicar si está activo
    username = models.CharField(max_length=30, unique=True)  # Asegura que el nombre de usuario sea único
    password = models.CharField(max_length=128)  
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"
    

class Categoria(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"
