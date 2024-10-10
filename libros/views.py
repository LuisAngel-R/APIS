from django.shortcuts import render, redirect, get_object_or_404 # Importamos render para devolver templates
from .forms import DocenteForm, EstudianteForm, AdministradorForm, PersonalForm, CategoriaForm, LoginForm
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from .models import Docente 
from .models import Estudiante
from .models import Administrador
from .models import Categoria
from .models import Personal
from django.contrib.auth.hashers import make_password
import qrcode
from django.core.files.base import ContentFile
# Vista para la página de inicio de sesión
def login_view(request):
    return render(request, 'login.html')  # Renderizamos la plantilla login.html

# Vista para la página de inicio de libros (puedes personalizar esta vista según tu necesidad)
def homeView(request):
    return render(request, 'home.html')  # Cambiar el nombre de la plantilla según lo que desees

def book_view(request):
    return render(request, 'book.html')

def category_view(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo')
        nombre = request.POST.get('nombre')

        # Crea una instancia del modelo Docente
        categoria = Categoria(
            codigo=codigo,
            nombre=nombre,
        )

        # Guarda el objeto en la base de datos
        categoria.save()

        
        return redirect('listcategory_view')  
    return render(request, 'category.html')

def adminalta_view(request):
    if request.method == 'POST':
        numero_trabajador = request.POST.get('numero_trabajador')
        nombres = request.POST.get('nombres')
        apellidos = request.POST.get('apellidos')
        telefono = request.POST.get('telefono')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        fecha_inicio = request.POST.get('fecha_inicio')  # Debe ser requerido
        fecha_finalizacion = request.POST.get('fecha_finalizacion')  # Ahora es requerido

        # Verifica si las contraseñas coinciden
        if password != confirm_password:
            return render(request, 'adminalta.html', {
                'error': 'Las contraseñas no coinciden.',
                'numero_trabajador': numero_trabajador,
                'nombres': nombres,
                'apellidos': apellidos,
                'telefono': telefono,
                'username': username,
                'fecha_inicio': fecha_inicio,
                'fecha_finalizacion': fecha_finalizacion,
            })

        # Verifica que la fecha de inicio no sea nula
        if not fecha_inicio:
            return render(request, 'adminalta.html', {
                'error': 'La fecha de inicio es requerida.',
                'numero_trabajador': numero_trabajador,
                'nombres': nombres,
                'apellidos': apellidos,
                'telefono': telefono,
                'username': username,
                'fecha_finalizacion': fecha_finalizacion,
            })

        # Verifica que la fecha de finalización no sea nula
        if not fecha_finalizacion:
            return render(request, 'adminalta.html', {
                'error': 'La fecha de finalización es requerida.',
                'numero_trabajador': numero_trabajador,
                'nombres': nombres,
                'apellidos': apellidos,
                'telefono': telefono,
                'username': username,
                'fecha_inicio': fecha_inicio,
            })

        # Convierte las fechas de string a objeto de tipo date
        try:
            fecha_inicio = timezone.datetime.strptime(fecha_inicio, '%Y-%m-%d').date()
            fecha_finalizacion = timezone.datetime.strptime(fecha_finalizacion, '%Y-%m-%d').date()
        except ValueError:
            return render(request, 'adminalta.html', {
                'error': 'Formato de fecha no válido. Asegúrese de usar el formato YYYY-MM-DD.',
                'numero_trabajador': numero_trabajador,
                'nombres': nombres,
                'apellidos': apellidos,
                'telefono': telefono,
                'username': username,
                'fecha_inicio': fecha_inicio,
                'fecha_finalizacion': fecha_finalizacion,
            })

        # Crea una instancia del modelo Docente
        administrador = Administrador(
            numero_trabajador=numero_trabajador,
            nombres=nombres,
            apellidos=apellidos,
            telefono=telefono,
            username=username,
            password=make_password(password),  # Asegúrate de hashear la contraseña
            fecha_inicio=fecha_inicio,
            fecha_finalizacion=fecha_finalizacion  # Ahora es requerido
        )

        qr_data = f"Administrador: {numero_trabajador}, {apellidos} {nombres}"
        qr_image = qrcode.make(qr_data)

        # Guardar imagen del QR en un objeto BytesIO
        from io import BytesIO
        buffer = BytesIO()
        qr_image.save(buffer, format='PNG')
        buffer.seek(0)

        # Guardar el archivo QR en el modelo
        administrador.qr_code.save(f'{numero_trabajador}_qr.png', ContentFile(buffer.read()), save=False)
        administrador.save()

        # Guarda el objeto en la base de datos
        administrador.save()

        
        return redirect('listadmin_view')  
    return render(request, 'adminalta.html')

def teacher_view(request):
    if request.method == 'POST':
        numero_trabajador = request.POST.get('numero_trabajador')
        nombres = request.POST.get('nombres')
        apellidos = request.POST.get('apellidos')
        telefono = request.POST.get('telefono')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        fecha_inicio = request.POST.get('fecha_inicio')  # Debe ser requerido
        fecha_finalizacion = request.POST.get('fecha_finalizacion')  # Ahora es requerido

        # Verifica si las contraseñas coinciden
        if password != confirm_password:
            return render(request, 'teacher.html', {
                'error': 'Las contraseñas no coinciden.',
                'numero_trabajador': numero_trabajador,
                'nombres': nombres,
                'apellidos': apellidos,
                'telefono': telefono,
                'username': username,
                'fecha_inicio': fecha_inicio,
                'fecha_finalizacion': fecha_finalizacion,
            })

        # Verifica que la fecha de inicio no sea nula
        if not fecha_inicio:
            return render(request, 'teacher.html', {
                'error': 'La fecha de inicio es requerida.',
                'numero_trabajador': numero_trabajador,
                'nombres': nombres,
                'apellidos': apellidos,
                'telefono': telefono,
                'username': username,
                'fecha_finalizacion': fecha_finalizacion,
            })

        # Verifica que la fecha de finalización no sea nula
        if not fecha_finalizacion:
            return render(request, 'teacher.html', {
                'error': 'La fecha de finalización es requerida.',
                'numero_trabajador': numero_trabajador,
                'nombres': nombres,
                'apellidos': apellidos,
                'telefono': telefono,
                'username': username,
                'fecha_inicio': fecha_inicio,
            })

        # Convierte las fechas de string a objeto de tipo date
        try:
            fecha_inicio = timezone.datetime.strptime(fecha_inicio, '%Y-%m-%d').date()
            fecha_finalizacion = timezone.datetime.strptime(fecha_finalizacion, '%Y-%m-%d').date()
        except ValueError:
            return render(request, 'teacher.html', {
                'error': 'Formato de fecha no válido. Asegúrese de usar el formato YYYY-MM-DD.',
                'numero_trabajador': numero_trabajador,
                'nombres': nombres,
                'apellidos': apellidos,
                'telefono': telefono,
                'username': username,
                'fecha_inicio': fecha_inicio,
                'fecha_finalizacion': fecha_finalizacion,
            })

        # Crea una instancia del modelo Docente
        docente = Docente(
            numero_trabajador=numero_trabajador,
            nombres=nombres,
            apellidos=apellidos,
            telefono=telefono,
            username=username,
            password=make_password(password),  # Asegúrate de hashear la contraseña
            fecha_inicio=fecha_inicio,
            fecha_finalizacion=fecha_finalizacion  # Ahora es requerido
        )

        qr_data = f"Docente: {numero_trabajador}, {apellidos} {nombres}"
        qr_image = qrcode.make(qr_data)

        # Guardar imagen del QR en un objeto BytesIO
        from io import BytesIO
        buffer = BytesIO()
        qr_image.save(buffer, format='PNG')
        buffer.seek(0)

        # Guardar el archivo QR en el modelo
        docente.qr_code.save(f'{numero_trabajador}_qr.png', ContentFile(buffer.read()), save=False)
        docente.save()

        # Guarda el objeto en la base de datos
        docente.save()

        # Redirige a la vista de listado de docentes después de guardar
        return redirect('listteacher_view')  # Cambia 'listteacher_view' al nombre de la URL donde quieras redirigir

    return render(request, 'teacher.html')
    

def bookagregar_view(request):
    return render(request, 'bookagregar.html')

def catalog_view(request):
    return render(request, 'catalog.html')

def advancesettings_view(request):
    return render(request, 'advancesettings.html')

def personal_view(request):
    if request.method == 'POST':
        numero_trabajador = request.POST.get('numero_trabajador')
        nombres = request.POST.get('nombres')
        apellidos = request.POST.get('apellidos')
        telefono = request.POST.get('telefono')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        fecha_inicio = request.POST.get('fecha_inicio')  # Debe ser requerido
        fecha_finalizacion = request.POST.get('fecha_finalizacion')  # Ahora es requerido

        # Verifica si las contraseñas coinciden
        if password != confirm_password:
            return render(request, 'personal.html', {
                'error': 'Las contraseñas no coinciden.',
                'numero_trabajador': numero_trabajador,
                'nombres': nombres,
                'apellidos': apellidos,
                'telefono': telefono,
                'username': username,
                'fecha_inicio': fecha_inicio,
                'fecha_finalizacion': fecha_finalizacion,
            })

        # Verifica que la fecha de inicio no sea nula
        if not fecha_inicio:
            return render(request, 'personal.html', {
                'error': 'La fecha de inicio es requerida.',
                'numero_trabajador': numero_trabajador,
                'nombres': nombres,
                'apellidos': apellidos,
                'telefono': telefono,
                'username': username,
                'fecha_finalizacion': fecha_finalizacion,
            })

        # Verifica que la fecha de finalización no sea nula
        if not fecha_finalizacion:
            return render(request, 'personal.html', {
                'error': 'La fecha de finalización es requerida.',
                'numero_trabajador': numero_trabajador,
                'nombres': nombres,
                'apellidos': apellidos,
                'telefono': telefono,
                'username': username,
                'fecha_inicio': fecha_inicio,
            })

        # Convierte las fechas de string a objeto de tipo date
        try:
            fecha_inicio = timezone.datetime.strptime(fecha_inicio, '%Y-%m-%d').date()
            fecha_finalizacion = timezone.datetime.strptime(fecha_finalizacion, '%Y-%m-%d').date()
        except ValueError:
            return render(request, 'personal.html', {
                'error': 'Formato de fecha no válido. Asegúrese de usar el formato YYYY-MM-DD.',
                'numero_trabajador': numero_trabajador,
                'nombres': nombres,
                'apellidos': apellidos,
                'telefono': telefono,
                'username': username,
                'fecha_inicio': fecha_inicio,
                'fecha_finalizacion': fecha_finalizacion,
            })

        # Crea una instancia del modelo Docente
        personal = Personal(
            numero_trabajador=numero_trabajador,
            nombres=nombres,
            apellidos=apellidos,
            telefono=telefono,
            username=username,
            password=make_password(password),  # Asegúrate de hashear la contraseña
            fecha_inicio=fecha_inicio,
            fecha_finalizacion=fecha_finalizacion  # Ahora es requerido
        )

        qr_data = f"Personal: {numero_trabajador}, {apellidos} {nombres}"
        qr_image = qrcode.make(qr_data)

        # Guardar imagen del QR en un objeto BytesIO
        from io import BytesIO
        buffer = BytesIO()
        qr_image.save(buffer, format='PNG')
        buffer.seek(0)

        # Guardar el archivo QR en el modelo
        personal.qr_code.save(f'{numero_trabajador}_qr.png', ContentFile(buffer.read()), save=False)
        personal.save()

        # Guarda el objeto en la base de datos
        personal.save()

        
        return redirect('listpersonal_view')  
    return render(request, 'personal.html')

def listadmin_view(request):
    administradores = Administrador.objects.all()  # Recupera todos los docentes de la base de datos
    if request.method == 'POST' and 'delete' in request.POST:
        administrador_id = request.POST.get('administrador_id')
        administrador = get_object_or_404(Administrador, id=administrador_id)
        administrador.delete()  # Esto elimina al docente de la base de datos
    return render(request, 'listadmin.html', {'administradores': administradores}) 

def listpersonal_view(request):
    personales = Personal.objects.all()  # Recupera todos los docentes de la base de datos
    if request.method == 'POST' and 'delete' in request.POST:
        personal_id = request.POST.get('personal_id')
        personal = get_object_or_404(Personal, id=personal_id)
        personal.delete()  # Esto elimina al docente de la base de datos
    return render(request, 'listpersonal.html', {'personales': personales}) 

def report_view(request):
    return render(request, 'report.html')

def loan_view(request):
    return render(request, 'loan.html')

def loanpending_view(request):
    return render(request, 'loanpending.html')

def loanreservation_view(request):
    return render(request, 'loanreservation.html')

def student_view(request):
    if request.method == 'POST':
        matricula = request.POST.get('matricula')
        nombres = request.POST.get('nombres')
        apellidos = request.POST.get('apellidos')
        programa_educativo = request.POST.get('programa_educativo')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Verifica si las contraseñas coinciden
        if password != confirm_password:
            return render(request, 'student.html', {
                'error': 'Las contraseñas no coinciden.',
                'numero_trabajador': matricula,
                'nombres': nombres,
                'apellidos': apellidos,
                'programa_educativo': programa_educativo,
                'username': username,
            })

        # Crea una instancia del modelo Estudiante
        estudiante = Estudiante(
            matricula=matricula,
            nombres=nombres,
            apellidos=apellidos,
            programa_educativo=programa_educativo,
            username=username,
            password=make_password(password),  # Asegúrate de hashear la contraseña
        )

        qr_data = f"Estudiante: {matricula}, {apellidos} {nombres}"
        qr_image = qrcode.make(qr_data)

        # Guardar imagen del QR en un objeto BytesIO
        from io import BytesIO
        buffer = BytesIO()
        qr_image.save(buffer, format='PNG')
        buffer.seek(0)

        # Guardar el archivo QR en el modelo
        estudiante.qr_code.save(f'{matricula}_qr.png', ContentFile(buffer.read()), save=False)
        estudiante.save()

        # Guarda el objeto en la base de datos
        estudiante.save()

        # Redirige a la vista de listado de docentes después de guardar
        return redirect('listsudent_view')  # Cambia 'listteacher_view' al nombre de la URL donde quieras redirigir

    return render(request, 'student.html')

def liststudent_view(request):
    estudiantes = Estudiante.objects.all()  # Recupera todos los estudiantes de la base de datos

    # Manejo del formulario al enviar una solicitud POST
    if request.method == 'POST':
        estudiante_id = request.POST.get('estudiante_id')

        # Si se presiona el botón para actualizar el estado
        if 'update_state' in request.POST:
            estudiante = get_object_or_404(Estudiante, id=estudiante_id)
            estudiante.estado = not estudiante.estado  # Cambia el estado (activo <-> inactivo)
            estudiante.save()  # Guarda los cambios
            return redirect('liststudent_view')  # Redirige a la misma vista para actualizar la lista

        # Si se presiona el botón de eliminar
        elif 'delete' in request.POST:
            estudiante = get_object_or_404(Estudiante, id=estudiante_id)
            estudiante.delete()  # Elimina al estudiante de la base de datos
            return redirect('liststudent_view')  # Redirige a la misma vista para actualizar la lista

    return render(request, 'liststudent.html', {'estudiantes': estudiantes})

def listteacher_view(request):
    docentes = Docente.objects.all()  # Recupera todos los docentes de la base de datos

    if request.method == 'POST' and 'delete' in request.POST:
        docente_id = request.POST.get('docente_id')
        docente = get_object_or_404(Docente, id=docente_id)
        docente.delete()  # Esto elimina al docente de la base de datos
        return redirect('listteacher_view')  # Redirige a la misma vista para actualizar la lista

    return render(request, 'listteacher.html', {'docentes': docentes})

def section_view(request):
    return render(request, 'section.html')

def Olvcontraseña_view(request):
    return render(request, 'Olvcontraseña.html')

def restablecerContraseña_view(request):
    return render(request, 'restablecerContraseña.html')

def fisicos_view(request):
    return render(request, 'fisicos.html')

def infobook_view(request):
    return render(request, 'infobook.html')

def listcategory_view(request):
    categorias = Categoria.objects.all()  # Recupera todos los docentes de la base de datos
    if request.method == 'POST' and 'delete' in request.POST:
        categoria_id = request.POST.get('categoria_id')
        categoria = get_object_or_404(Categoria, id=categoria_id)
        categoria.delete()  # Esto elimina al docente de la base de datos
        return redirect('listcategory_view') 
    
    return render(request, 'listcategory.html', {'categorias': categorias})


def homeView(request):
    if request.method == 'POST':
        numero_trabajador = request.POST.get('numero_trabajador')
        password = request.POST.get('password')
        
        try:
            # Busca el administrador por el número de trabajador
            administrador = Administrador.objects.get(numero_trabajador=numero_trabajador)
            
            # Verifica la contraseña
            if check_password(password, administrador.password):
                # Almacena el ID del administrador en la sesión
                request.session['administrador_id'] = administrador.id
                messages.success(request, 'Inicio de sesión exitoso')
                
                # Redirige a la vista de book
                return redirect('book')  # Redirigir a la vista de libros
            else:
                messages.error(request, 'Credenciales incorrectas')
        except Administrador.DoesNotExist:
            messages.error(request, 'Credenciales incorrectas')

    return render(request, 'login.html') 

# Nueva vista para book.html
def book_view(request):
    return render(request, 'book.html') # Renderiza la plantilla de libros





