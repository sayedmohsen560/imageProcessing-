import cv2



def simple_thresholding (image_file):
    gray_scale = cv2.cvtColor(image_file, cv2.COLOR_BGR2GRAY)
    ret, simple_threshold = cv2.threshold(gray_scale,127,255,cv2.THRESH_BINARY)
    cv2.imwrite('simple.png',simple_threshold)



def adaptive_thresholding (image_file):
    gray_scale = cv2.cvtColor(image_file, cv2.COLOR_BGR2GRAY)
    th2 = cv2.adaptiveThreshold(gray_scale, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
    th3 = cv2.adaptiveThreshold(gray_scale, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
    cv2.imwrite('mean.png',th2)
    cv2.imwrite('gaussen.png', th3)


def otsu_thresholding (imge_file):
    img = cv2.cvtColor(imge_file, cv2.COLOR_BGR2GRAY)
    ret2, th2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    blur = cv2.GaussianBlur(img, (5, 5), 0)
    ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    cv2.imwrite('results.png',cv2.threshold(img, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1])
    cv2.imwrite('otsu.png',th2)
    cv2.imwrite('otsugaussien.png',th3)


imgs = cv2.imread('sce.jpg')
sod = cv2.imread('sod.png')
simple_thresholding(imgs)
adaptive_thresholding(imgs)
otsu_thresholding(imgs)