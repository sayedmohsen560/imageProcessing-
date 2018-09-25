import cv2

def noise_removing(rescaled_file):
    dst = cv2.fastNlMeansDenoisingColored(rescaled_file, None, 10, 10, 7, 21)
    cv2.imwrite('noise_removing.jpg',dst)
