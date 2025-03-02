import tkinter as tk
from ctypes import windll

from compressmodule import compress, decompress


def compression(i, o):
    compress(input_file=i, output_file=o)


def decompression(i, o):
    decompress(input_file=i, output_file=o)


def start_gui():
    window = tk.Tk()

    window.title("Compression engine")
    window.geometry("600x400")
    window.config(padx=10, pady=10)

    compress_input_entry = tk.Entry(window)
    compress_output_entry = tk.Entry(window)

    decompress_input_entry = tk.Entry(window)
    decompress_output_entry = tk.Entry(window)

    compress_input_label = tk.Label(window, text="File to be compressed: ", anchor="w", justify="left")
    compress_output_label = tk.Label(window, text="Name of the compressed file: ", anchor="w", justify="left")

    decompress_input_label = tk.Label(window, text="File to be decompressed: ", anchor="w", justify="left")
    decompress_output_label = tk.Label(window, text="Name of the compressed file: ", anchor="w", justify="left")

    compress_button = tk.Button(window, text="Compress",
                                command=lambda: compression(compress_input_entry.get(),
                                                            compress_output_entry.get()))
    decompress_button = tk.Button(window, text="Decompress",
                                  command=lambda: decompression(decompress_input_entry.get(),
                                                                decompress_output_entry.get()))

    compress_input_label.grid(row=0, column=0)
    compress_input_entry.grid(row=0, column=1)
    compress_output_label.grid(row=1, column=0)
    compress_output_entry.grid(row=1, column=1)

    decompress_input_label.grid(row=3, column=0)
    decompress_input_entry.grid(row=3, column=1)
    decompress_output_label.grid(row=4, column=0)
    decompress_output_entry.grid(row=4, column=1)

    compress_button.grid(row=2, column=1)
    decompress_button.grid(row=5, column=1)

    window.mainloop()
