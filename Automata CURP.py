import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import re

# Patrón de expresión regular para validar la CURP
curp_pattern = re.compile(r'^[JFDV]{4}$')

def show_automaton(curp_start, canvas, ax):
    # Limpia la figura anterior
    ax.clear()

    # Crea un grafo dirigido con NetworkX
    G = nx.DiGraph()

    # Añadir nodos y aristas al grafo basados en la CURP
    for i, letter in enumerate(curp_start):
        G.add_edge(f'q{i}', f'q{i+1}', label=letter)

    # Configurar la figura para el autómata
    pos = nx.spring_layout(G)  # Posicionamiento de los nodos
    nx.draw(G, pos, ax=ax, with_labels=True, node_size=1500, node_color='lightblue', font_size=15)
    
    edge_labels = {(u, v): d['label'] for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Actualizar el canvas
    canvas.draw()

def validate_and_show(curp, canvas, ax):
    if curp_pattern.match(curp):
        show_automaton(curp, canvas, ax)
    else:
        messagebox.showerror("Error", "La CURP ingresada no es válida o no contiene las letras permitidas.")

# Configuración inicial de la ventana Tkinter.
root = tk.Tk()
root.title("Visualizador de Autómata por CURP")

# Crear figura para el autómata
fig, ax = plt.subplots(figsize=(5, 5))

# Creación de widgets.
curp_label = tk.Label(root, text="Ingrese las primeras 4 letras de su CURP:")
curp_entry = tk.Entry(root)
validate_button = tk.Button(root, text="Validar y Mostrar", command=lambda: validate_and_show(curp_entry.get().upper(), canvas, ax))
canvas = FigureCanvasTkAgg(fig, master=root)  # Canvas para matplotlib

# Colocación de widgets.
curp_label.pack()
curp_entry.pack()
validate_button.pack()
canvas.get_tk_widget().pack()  # Empaquetar el canvas en la ventana Tkinter

# Inicia el bucle principal de la aplicación.
root.mainloop()
