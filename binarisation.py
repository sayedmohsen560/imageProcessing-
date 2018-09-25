import cv2
from PIL import Image

def bin_my_image (image_to_binraize_file):
    bin_file = Image.open(image_to_binraize_file)  # open colour image
    bin_file = bin_file.convert('1')  # convert image to black and white
    bin_file.save('test_result.png')



def binraztion (rescaled_file):
    img = cv2.imread(rescaled_file)
    grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blackandwhite_image = cv2.adaptiveThreshold(grey_img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
    cv2.imwrite('test_blackandwhite.jpg',blackandwhite_image)