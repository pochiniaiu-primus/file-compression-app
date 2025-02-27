import tkinter as tk
from compressmodule import compress, decompress


def compression(i, o):
    compress(input_file=i, output_file=o)


def start_gui():
    window = tk.Tk()

    window.title("Compression engine")
    window.geometry("600x400")
    window.config(padx=10, pady=10)

    input_entry = tk.Entry(window)
    output_entry = tk.Entry(window)

    input_label = tk.Label(window, text="File to be compressed: ", anchor="w", justify="left")
    output_label = tk.Label(window, text="Name of the compressed file: ", anchor="w", justify="left")
    compress_button = tk.Button(window, text="Compress")

    input_label.grid(row=0, column=0)
    input_entry.grid(row=0, column=1)
    output_label.grid(row=1, column=0)
    output_entry.grid(row=1, column=1)
    compress_button.grid(row=2, column=1)

    window.mainloop()
