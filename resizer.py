import os
import cv2
import tkinter as tk
from tkinter import messagebox

def resize_images(input_folder, output_folder, width, height):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]

    if not image_files:
        messagebox.showinfo("No images", "No images in folder")
        return

    for filename in image_files:
        img_path = os.path.join(input_folder, filename)
        img = cv2.imread(img_path)

        resized_img = cv2.resize(img, (width, height))

        output_path = os.path.join(output_folder, filename)
        cv2.imwrite(output_path, resized_img)
        print(f"Resized image saved to {output_path}")

def start_resizing():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    
    input_folder = os.path.join(script_dir, 'Input')
    output_folder = os.path.join(script_dir, 'Output')
    
    width = entry_width.get()
    height = entry_height.get()

    if not width or not height:
        messagebox.showwarning("Missing fields", "Both fields need filling")
        return

    resize_images(input_folder, output_folder, int(width), int(height))

root = tk.Tk()
root.title("Image Resizer")

tk.Label(root, text="Width:").grid(row=0, column=0, padx=10, pady=10)
entry_width = tk.Entry(root)
entry_width.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Height:").grid(row=1, column=0, padx=10, pady=10)
entry_height = tk.Entry(root)
entry_height.grid(row=1, column=1, padx=10, pady=10)

resize_button = tk.Button(root, text="Resize Images", command=start_resizing)
resize_button.grid(row=2, columnspan=2, pady=20)

root.mainloop()
