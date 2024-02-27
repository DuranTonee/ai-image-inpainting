# AI Image Inpainting

This project utilizes the OpenAI API, specifically the DALL-E model, for [image inpainting](https://platform.openai.com/docs/guides/images/usage). It takes an image as input, generates prompts to describe the image, and then uses the generated prompts to inpaint the image with additional details.

## How it works
Refer to the [preview folder](https://github.com/DuranTonee/ai-image-inpainting/tree/main/preview).

1. Original image (screenshot from the Sea of Thieves game):

   ![6_original_image](https://github.com/DuranTonee/ai-image-inpainting/assets/95922080/d3e60663-6887-4ed1-86b1-f9323b8181f0)

3. Crop the square from the middle of the image:

   ![6_cropped_image](https://github.com/DuranTonee/ai-image-inpainting/assets/95922080/fe84787e-5b83-4f75-928b-281c0da60801)

4. Scale the square to a lower resolution (user input, 350-500 is recommended) due to openai's limitations (1024x1024).
5. AI describes the image and adds new details for it (creating a prompt):

    **default prompt:** describe this image briefly and in general, short sentences. imagine and add 3 new details to it, don't say they're imaginary or new. they must not be sound, you should be able to see them and no parrots

    **output:** The image depicts a tranquil sunset over a coastal landscape. Sunlight filters through the haze, casting a warm glow over the scene. A ship sails in the distance along the calm sea, while the rocky coastline is adorned with lush, green foliage. In the sky, a flock of birds flies toward the horizon. On the cliff edge, a lighthouse stands, guiding the way for seafarers. Below the cliffs, a sandy beach stretches out, inviting exploration.

6. AI generates background for the square based on the output:

   ![6_downloaded_image](https://github.com/DuranTonee/ai-image-inpainting/assets/95922080/53f2d796-8a0b-4b02-ae0d-88cdeb7ac083)

## Usage
0. Clone the repository and install dependencies.
1. Place the input image as `original_image.jpg` in the project directory.
2. Run `image_gen.py`.
3. Follow the prompts to input the desired square size in pixels.
4. The script will generate a prompt to describe the image and inpaint it with additional details.
5. The result will be saved as `downloaded_image.png` in the project directory.
