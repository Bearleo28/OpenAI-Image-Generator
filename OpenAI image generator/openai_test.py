import os
from openai import OpenAI
from PIL import ImageTk, Image
import requests, io
import tkinter




client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


response = client.images.generate(
    model="dall-e-3",
    prompt="dominos pizza pixar movie poster",
    style="vivid",
    size="1024x1024",
    quality="hd",
    n=1
)

image_url = response.data[0].url

response = requests.get(image_url)
image = Image.open(io.BytesIO(response.content))
image = ImageTk.PhotoImage(image)
image = image.save('testphoto', 'jpeg')

#print(image_url)

