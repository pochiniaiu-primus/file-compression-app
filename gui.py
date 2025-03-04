import tkinter as tk
from tkinter import filedialog, messagebox

from compressmodule import compress, decompress


def open_file():
    filename = filedialog.askopenfilename(initialdir='/', title='Select a file: ')
    return filename if filename else None


def compression(input_file, output_file):
    if not input_file:
        messagebox.showwarning("Warning", "No file selected for compression.")
        return

    try:
        compress(input_file=input_file, output_file=output_file)
        messagebox.showinfo("Success", f"File compressed successfully!\nSaved as: {output_file}")
    except Exception as e:
        messagebox.showerror("Error", f"Compression failed: {e}")


def decompression(input_file, output_file):
    if not input_file:
        messagebox.showwarning("Warning", "No file selected for decompression.")
        return

    try:
        decompress(input_file=input_file, output_file=output_file)
        messagebox.showinfo("Success", f"File decompressed successfully!\nSaved as: {output_file}")
    except Exception as e:
        messagebox.showerror("Error", f"Decompression failed: {e}")


def start_gui():
    window = tk.Tk()

    window.title("Compression Engine")
    window.geometry("280x150")
    window.config(padx=10, pady=10)

    compress_button = tk.Button(window, text="Compress File", width=35,
                                command=lambda: compression(open_file() or "",
                                                            'compressed_output.txt'), highlightthickness=0)
    decompress_button = tk.Button(window, text="Decompress File", width=35,
                                  command=lambda: decompression(open_file() or "",
                                                                'decompressed_output.txt'), highlightthickness=0)

    exit_button = tk.Button(window, text="Exit", width=35, command=window.quit, highlightthickness=0)

    compress_button.grid(row=0, column=0, padx=5, pady=5)
    decompress_button.grid(row=1, column=0, padx=5, pady=5)
    exit_button.grid(row=2, column=0, padx=5, pady=5)

    window.mainloop()
