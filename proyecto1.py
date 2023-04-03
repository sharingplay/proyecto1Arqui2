import tkinter as tk
import time

class Processor:
    def __init__(self, number, data):
        self.number = number
        self.data = data
    def __str__(self):
        return f"{self.number}"

    def updateData(self,data):
        self.data = data

    def getData(self):
        return self.data

class Ventana:
    def __init__(self, master):
        self.master = master

        # creates 4 text boxes for the processors
        self.text_box1 = tk.Text(self.master, height=10, width=30)
        self.text_box1.grid(row=0, column=0, padx=10, pady=10)

        self.text_box2 = tk.Text(self.master, height=10, width=30)
        self.text_box2.grid(row=0, column=1, padx=10, pady=10)

        self.text_box3 = tk.Text(self.master, height=10, width=30)
        self.text_box3.grid(row=1, column=0, padx=10, pady=10)

        self.text_box4 = tk.Text(self.master, height=10, width=30)
        self.text_box4.grid(row=1, column=1, padx=10, pady=10)

        # creates a text box to display the memory data
        self.text_box_memory = tk.Text(self.master, height=10, width=30)
        self.text_box_memory.grid(row=0, column=2, padx=10, pady=10)

        # creates a text box for additional information
        self.text_box_info = tk.Text(self.master, height=10, width=30)
        self.text_box_info.grid(row=1, column=2, padx=10, pady=10)

        # creates the buttons
        self.boton1 = tk.Button(self.master, text="Boton 1")
        self.boton1.grid(row=2, column=0, padx=10, pady=10)

        self.boton2 = tk.Button(self.master, text="Boton 2")
        self.boton2.grid(row=2, column=1, padx=10, pady=10)

        self.boton3 = tk.Button(self.master, text="Boton 3")
        self.boton3.grid(row=2, column=2, padx=10, pady=10)

        self.boton4 = tk.Button(self.master, text="Boton 4")
        self.boton4.grid(row=2, column=3, padx=10, pady=10)

    # updates the window information
    def actualizar(self, lista_procesadores):
        for i, procesador in enumerate(lista_procesadores):
            if i == 0:
                self.text_box1.delete(1.0, tk.END)
                self.text_box1.insert(tk.END, str(procesador.getData()))
            elif i == 1:
                self.text_box2.delete(1.0, tk.END)
                self.text_box2.insert(tk.END, str(procesador.getData()))
            elif i == 2:
                self.text_box3.delete(1.0, tk.END)
                self.text_box3.insert(tk.END, str(procesador.getData()))
            elif i == 3:
                self.text_box4.delete(1.0, tk.END)
                self.text_box4.insert(tk.END, str(procesador.getData()))

    def agregar_texto(self):
        texto = self.entrada_texto.get()  # obtiene el texto ingresado
        self.cuadro_texto.insert(tk.END, texto + "\n")  # agrega el texto al cuadro de texto

def main():

    #Create processors
    p1 = Processor(1, "primeros datos de prueba 1")
    p2 = Processor(2, "segundos datos de prueba 2")

    #Processors list
    processors = [p1,p2]

    #Creates display window
    root = tk.Tk()
    ventana = Ventana(root)

    #Updates display window
    ventana.actualizar(processors)

    # ejecuta la ventana
    root.mainloop()

if __name__ == "__main__":
    main()