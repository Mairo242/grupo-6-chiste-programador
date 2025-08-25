import requests 
import tkinter as tk 

# --- Funciones de Lógica ---

def obtener_chiste():
    url = "https://official-joke-api.appspot.com/jokes/programming/random"
    try:
        response = requests.get(url)
        chiste_data = response.json()[0]
        return chiste_data
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con la API: {e}")
        return None

def mostrar_nuevo_chiste():

    global chiste_actual
    chiste_actual = obtener_chiste()

    if chiste_actual:
        setup.set(chiste_actual['setup'])
        punchline.set("") 
        boton_mostrar_punchline.pack(pady=10) 
        
def mostrar_punchline():

    if chiste_actual:
        punchline.set(chiste_actual['punchline'])
        boton_mostrar_punchline.pack_forget() 

# --- Configuración de la Ventana (Tkinter) ---
root = tk.Tk()
root.title("Chiste de Programador")
root.geometry("500x300")
root.configure(bg="#2c3e50") 


setup = tk.StringVar()
punchline = tk.StringVar()

# --- Creación de Widgets ---

label_setup = tk.Label(root, textvariable=setup, wraplength=450,
                       font=("Helvetica", 14, "bold"), fg="#ecf0f1", bg="#2c3e50")
label_setup.pack(pady=20, padx=10)


label_punchline = tk.Label(root, textvariable=punchline, wraplength=450,
                           font=("Helvetica", 12), fg="#f1c40f", bg="#2c3e50")
label_punchline.pack(padx=10)


boton_mostrar_punchline = tk.Button(root, text="Mostrar respuesta", command=mostrar_punchline,
                                    bg="#3498db", fg="white", font=("Helvetica", 10, "bold"), relief="raised")


boton_otro_chiste = tk.Button(root, text="Otro chiste", command=mostrar_nuevo_chiste,
                              bg="#2ecc71", fg="white", font=("Helvetica", 10, "bold"), relief="raised")
boton_otro_chiste.pack(pady=10)

# --- Inicio de la Aplicación ---

mostrar_nuevo_chiste()

root.mainloop()