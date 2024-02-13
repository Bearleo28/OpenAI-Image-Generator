import customtkinter as CT
import tkinter as TK
from tkinter import filedialog as fd
import os
from openai import OpenAI
from PIL import Image, ImageTk
import requests, io





def generate():
    global image

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    user_prompt = prompt_entry.get("0.0", TK.END)
    user_style = str(style_dropdown.get().lower())
    response = client.images.generate(
        model="dall-e-3",
        prompt=user_prompt,
        size="1024x1024",
        n=1,
        style=user_style,
        quality="hd"
    )

    image_url = response.data[0].url

    
    response = requests.get(image_url)
    image = Image.open(io.BytesIO(response.content))
    #image.save("c:/Users/chuck/Desktop/Python GUI project apps/OpenAI image generator/AI_image.jpg")
    canvas_image = ImageTk.PhotoImage(image)
    

    

    set_canvas(canvas_image)




def set_canvas(image):
    
    canvas.image = image
    canvas.create_image(0, 0, anchor="nw", image=image)

def clear():
    canvas.delete('all')
    
    
def save_image():
    unclean_name = save_name.get("0.0", TK.END)
    name = unclean_name.strip()
    image.save(f"c:/Users/chuck/Desktop/Python GUI project apps/OpenAI image generator/{name}.jpg")

def choose_path():
    global path
    path = fd.askdirectory()
    print(path)
    

root = CT.CTk()
root.title("AI Image Generator")

input_frame = CT.CTkFrame(root)
input_frame.pack(side="left", padx=10, pady=10, expand=True)

prompt_label = CT.CTkLabel(input_frame, text="Prompt")
prompt_label.grid(row=0, column=0, padx=10, pady=10)
prompt_entry = CT.CTkTextbox(input_frame, height=60, width=300)
prompt_entry.grid(row=0, column=1, padx=10, pady=10)

style_label = CT.CTkLabel(input_frame, text="Style")
style_label.grid(row=1, column=0, padx=10, pady=10)
style_dropdown = CT.CTkComboBox(input_frame, values=["Vivid", "Natural"])
style_dropdown.grid(row=1, column=1, padx=10, pady=10)

generate_button = CT.CTkButton(input_frame, text="Generate", command=generate)
generate_button.grid(row=3, column=0, columnspan=2, sticky="news", padx=10, pady=10)

clear_button = CT.CTkButton(input_frame, text="Clear", command=clear)
clear_button.grid(row=4, column=0, columnspan=2, sticky="news", pady=20, padx=10)

save_button = CT.CTkButton(input_frame, text="Save Image", command=save_image)
save_button.grid(row=5, column=0, columnspan=2, padx=10, pady=20)

save_label = CT.CTkLabel(input_frame, text="Save As...")
save_label.grid(row=6, column=0, columnspan=1, padx=10, pady=10)
save_name = CT.CTkTextbox(input_frame, height=30, width=300)
save_name.grid(row=6, column=1, columnspan=2, padx=10, pady=10)

path_dir = CT.CTkButton(input_frame, text="Choose FilePath...", command=choose_path)
path_dir.grid(row=7, column=0, padx=10, pady=10)
path_label = CT.CTkLabel(input_frame, text=f"Save to : ")
path_label.grid(row=7, column=1, columnspan=2, padx=10, pady=10)

canvas = TK.Canvas(root, width=1024, height=1024, background="grey14", border=None )
canvas.pack(side="left")




root.mainloop()