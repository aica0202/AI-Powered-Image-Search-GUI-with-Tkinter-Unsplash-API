import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import requests
import io

# --- Unsplash API Key ---
UNSPLASH_ACCESS_KEY = ("I02aCKFmSsWXb9OIXmQstW1oDZmx1FEK-Ac-N7kIx_k")

# --- Global Variables ---
images = []          # List of PhotoImage objects
image_urls = []      # URLs for images
current_index = 0    # Current image in carousel
search_history = []  # Search terms history

# --- Functions ---


def search_images():
    global images, image_urls, current_index, search_history
    query = search_entry.get().strip()
    if not query:
        messagebox.showwarning("Warning", "Please enter a search term!")
        return

    # Add to search history
    if query not in search_history:
        search_history.append(query)
        history_listbox.insert(tk.END, query)

    # Fetch 5 random images for the query
    images.clear()
    image_urls.clear()
    current_index = 0
    try:
        for _ in range(5):
            url = f"https://api.unsplash.com/photos/random?query={query}&client_id={UNSPLASH_ACCESS_KEY}"
            response = requests.get(url).json()
            img_url = response['urls']['regular']
            image_urls.append(img_url)

            img_data = requests.get(img_url).content
            img = Image.open(io.BytesIO(img_data)).resize((512, 512))
            img_tk = ImageTk.PhotoImage(img)
            images.append(img_tk)

        update_image()
    except Exception as e:
        messagebox.showerror("Error", str(e))


def update_image():
    global current_index
    if images:
        canvas.image = images[current_index]
        canvas.create_image(0, 0, anchor="nw", image=images[current_index])
        current_index = (current_index + 1) % len(images)
        canvas.after(3000, update_image)  # Auto carousel every 3 seconds


def save_image():
    if not images:
        messagebox.showwarning("Warning", "No image to save!")
        return
    file_path = filedialog.asksaveasfilename(defaultextension=".png")
    if file_path:
        images[current_index -
               1]._PhotoImage__photo.write(file_path, format="png")
        messagebox.showinfo("Saved", f"Image saved to {file_path}")


def load_history(event):
    selected = history_listbox.get(history_listbox.curselection())
    search_entry.delete(0, tk.END)
    search_entry.insert(0, selected)
    search_images()


# --- GUI Setup ---
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Unsplash Image Search")
root.geometry("900x700")

# --- Input Frame ---
input_frame = ctk.CTkFrame(root)
input_frame.pack(side="left", fill="y", padx=10, pady=10)

ctk.CTkLabel(input_frame, text="Search Images").pack(pady=5)
search_entry = ctk.CTkEntry(input_frame, width=145)
search_entry.pack(pady=5)

ctk.CTkButton(input_frame, text="Search", command=search_images).pack(pady=5)
ctk.CTkButton(input_frame, text="Save Current Image",
              command=save_image).pack(pady=5)

# Search history list
ctk.CTkLabel(input_frame, text="Search History").pack(pady=5)
history_listbox = tk.Listbox(input_frame, width=30, height=10)
history_listbox.pack(pady=5)
history_listbox.bind("<<ListboxSelect>>", load_history)

# --- Canvas Frame ---
canvas = tk.Canvas(root, width=512, height=512, bg="black")
canvas.pack(side="left", padx=10, pady=10)

root.mainloop()
