# https://community.openai.com/t/dall-e-3-not-accepting-api-request/572857
# https://community.openai.com/t/dall-e-api-extending-images-other-ratio/23163/8
from openai import OpenAI
from config import openAI_key
import base64
from prepare_img import transform_image
import requests

def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

def create_prompt(client):
  image = encode_image("cropped_image.jpg")
  response = client.chat.completions.create(
      model="gpt-4-vision-preview",
      messages=[
          {
          "role": "user",
          "content": [
              {"type": "text", "text": "describe this image briefly and in general, short sentences. imagine and add 3 new details to it, don't say they're imaginary or new. they must not be sound, you should be able to see them and no parrots"},
              {
              "type": "image_url",
              "image_url": {
                  "url": f"data:image/jpeg;base64,{image}",
              },
              },
          ],
          }
      ],
  max_tokens=300
  )
  return response.choices[0].message.content

client = OpenAI(api_key=openAI_key)

square_size = int(input("Square size in px: "))
transform_image(square_size)
prompt = create_prompt(client)
print(prompt)
#more_stuff = input("More details to the prompt (leave empty if not needed): ")

response = client.images.edit(
  model="dall-e-2",
  image=open("result_image.png", "rb"),
  mask=open("result_image.png", "rb"),
  # prompt=f"{prompt} {more_stuff}",
   prompt=prompt,
  n=1,
  size="1024x1024"
)

image_url = response.data[0].url
print(image_url)

response = requests.get(image_url)
if response.status_code == 200:
    with open("downloaded_image.png", "wb") as f:
        f.write(response.content)
    print("Image downloaded successfully.")
else:
    print("Failed to download image. Status code:", response.status_code)
