import cv2
import numpy as np


def detect_my_text (image_file):
    gray_scale = cv2.cvtColor(image_file, cv2.COLOR_BGR2GRAY)
    not_gray_scale = cv2.bitwise_not(gray_scale)
    thresh = cv2.threshold(not_gray_scale, 0, 255,
                           cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    return thresh


def compute_rotation_angel (image_file):
    coordinates = np.column_stack(np.where(image_file > 0))
    angle = cv2.minAreaRect(coordinates)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle

    return angle



def rotate_my_image (image_file, angle):
    (h, w) = image_file.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image_file, M, (w, h),
                             flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated



image = cv2.imread('text_skew_inputs_1.png')
stage1 = detect_my_text(image)
stage2 = compute_rotation_angel(stage1)
stage3 = rotate_my_image(stage1, stage2)
cv2.imwrite("result.png",stage3)