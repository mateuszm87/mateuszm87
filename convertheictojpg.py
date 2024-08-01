import os
from tkinter import Tk, Label, Button, filedialog
from PIL import Image
import pillow_heif

# Function to select source folder
def select_source_folder():
    folder = filedialog.askdirectory()
    source_folder_label.config(text=folder)
    return folder

# Function to select destination folder
def select_destination_folder():
    folder = filedialog.askdirectory()
    destination_folder_label.config(text=folder)
    return folder

# Function to convert HEIC to JPG
def convert_heic_to_jpg():
    source_folder = source_folder_label.cget("text")
    destination_folder = destination_folder_label.cget("text")
    
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    for filename in os.listdir(source_folder):
        if filename.lower().endswith('.heic'):
            heic_path = os.path.join(source_folder, filename)
            jpg_path = os.path.join(destination_folder, f"{os.path.splitext(filename)[0]}.jpg")
            
            heif_file = pillow_heif.read_heif(heic_path)
            image = Image.frombytes(
                heif_file.mode, 
                heif_file.size, 
                heif_file.data, 
                "raw"
            )
            image.save(jpg_path, "JPEG")
            print(f"Converted {filename} to {jpg_path}")

# Create the main window
root = Tk()
root.title("HEIC to JPG Converter")

# Create and place labels and buttons
Label(root, text="Select Source Folder:").grid(row=0, column=0, padx=10, pady=10)
source_folder_label = Label(root, text="")
source_folder_label.grid(row=0, column=1, padx=10, pady=10)
Button(root, text="Browse", command=select_source_folder).grid(row=0, column=2, padx=10, pady=10)

Label(root, text="Select Destination Folder:").grid(row=1, column=0, padx=10, pady=10)
destination_folder_label = Label(root, text="")
destination_folder_label.grid(row=1, column=1, padx=10, pady=10)
Button(root, text="Browse", command=select_destination_folder).grid(row=1, column=2, padx=10, pady=10)

Button(root, text="Convert", command=convert_heic_to_jpg).grid(row=2, column=1, padx=10, pady=10)

# Run the application
root.mainloop()
