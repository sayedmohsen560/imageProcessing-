from PIL import Image




def rescale_my_image (image_file) :
    rescaled = Image.open (image_file)
    rescaled.save('result.png', dpi=(300, 300))



