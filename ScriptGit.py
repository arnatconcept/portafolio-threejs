import os
import subprocess
import tkinter as tk
from tkinter import messagebox, simpledialog

# Función para ejecutar comandos de Git y mostrar el resultado
def run_git_command(command, success_message=None):
    try:
        # Ejecuta el comando Git y captura el resultado
        result = subprocess.run(command, capture_output=True, text=True, shell=True)
        
        # Si el comando se ejecuta sin errores
        if result.returncode == 0:
            output = result.stdout
            # Muestra un mensaje de éxito o el resultado del comando
            messagebox.showinfo("Éxito", success_message or output)
        else:
            # Si ocurre un error, muestra el mensaje de error
            error = result.stderr
            messagebox.showerror("Error", f"Error al ejecutar el comando: {error}")
    except Exception as e:
        # Si ocurre una excepción inesperada, muestra el mensaje de excepción
        messagebox.showerror("Excepción", f"Error inesperado: {str(e)}")

# Función para el botón "git add" (Añadir archivos al staging)
def git_add():
    run_git_command("git add .", success_message="Archivos añadidos correctamente (git add .)")

# Función para el botón "git commit" (Crear commit con mensaje)
def git_commit():
    # Solicita al usuario que ingrese el mensaje del commit
    commit_message = simpledialog.askstring("Commit", "Introduce el mensaje del commit:")
    
    if commit_message:
        # Ejecuta git commit con el mensaje ingresado
        run_git_command(f'git commit -m "{commit_message}"', success_message="Commit realizado correctamente")

# Función para el botón "git push" (Subir cambios al repositorio remoto)
def git_push():
    run_git_command("git push origin master", success_message="Cambios subidos correctamente a GitHub")

# Función para el botón "git status" (Mostrar el estado actual del repositorio)
def git_status():
    run_git_command("git status")

# Configuración de la interfaz gráfica usando Tkinter
root = tk.Tk()
root.title("Gestor de Versiones Git")  # Título de la ventana

# Etiqueta principal
label = tk.Label(root, text="Gestiona tus versiones Git", font=("Arial", 16))
label.pack(pady=10)

# Botón para ejecutar "git add"
btn_add = tk.Button(root, text="Añadir archivos (git add .)", command=git_add, width=40, height=2)
btn_add.pack(pady=5)

# Botón para ejecutar "git commit"
btn_commit = tk.Button(root, text="Crear commit (git commit)", command=git_commit, width=40, height=2)
btn_commit.pack(pady=5)

# Botón para ejecutar "git push"
btn_push = tk.Button(root, text="Subir cambios (git push)", command=git_push, width=40, height=2)
btn_push.pack(pady=5)

# Botón para ejecutar "git status"
btn_status = tk.Button(root, text="Ver estado (git status)", command=git_status, width=40, height=2)
btn_status.pack(pady=5)

# Función para cerrar la aplicación
def cerrar_app():
    root.quit()

# Botón para salir de la aplicación
btn_exit = tk.Button(root, text="Salir", command=cerrar_app, width=40, height=2, bg="red", fg="white")
btn_exit.pack(pady=10)

# Establecer tamaño de la ventana
root.geometry("400x400")

# Iniciar el loop principal de la interfaz gráfica
root.mainloop()
