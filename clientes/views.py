# clientes/views.py
import psycopg2
from django.shortcuts import render, redirect
from django.conf import settings

# Configuración de conexión
def get_connection():  #codigo para establecer la conexion desde views.py
    return psycopg2.connect(
        host="localhost",
        port="5432",
        dbname="base",
        user="user",
        password="1234"
    )

def landing(request):
    return render(request, "clientes/landing.html")

def formulario(request): #se crea la vista para el formulario, y que conecte con la BD
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')

        print("➡️ POST recibido:", nombre, email)#print para verificar que se recibe el POST

        if nombre and email:
            try:
                conn = get_connection()#establecer la conexion
                with conn.cursor() as cur:
                    cur.execute("INSERT INTO usuarios (nombre, email) VALUES (%s, %s)", (nombre, email))#insertar datos
                conn.commit()#commit para guardar los cambios
                conn.close()
                print("✅ Inserción completada")
                return redirect('listado')
            except Exception as e:
                print("❌ ERROR al insertar:", e)
                return render(request, "clientes/formulario.html", {'error': str(e)})

    return render(request, "clientes/formulario.html")


def listado(request):
    try:
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute("SELECT id, nombre, email FROM usuarios ORDER BY id ASC")
            usuarios = cur.fetchall()
        conn.close()
        return render(request, "clientes/listado.html", {'usuarios': usuarios})
    except Exception as e:
        return render(request, "clientes/listado.html", {'error': str(e), 'usuarios': []})

