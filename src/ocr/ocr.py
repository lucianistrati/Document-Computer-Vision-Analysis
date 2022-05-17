from pdf2image import convert_from_path
from PIL import Image

import pytesseract
import pdb
import cv2
import os


def convert_pdf_to_images(pdf_filepath: str, img_filepath: str=""):
    pages = convert_from_path(pdf_filepath, 500)
    img_filepath = os.path.splitext(pdf_filepath)[0]
    for i, page in enumerate(pages):
        page.save(img_filepath + f"_{i}.jpeg", "JPEG")


def get_text_from_image(image, preprocess=None):
    print(type(image))
    pdb.set_trace()
    # check to see if we should apply thresholding to preprocess the
    # image
    if preprocess == "thresh":
        gray = cv2.threshold(image, 0, 255,
                             cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    # make a check to see if median blurring should be done to remove
    # noise
    elif preprocess == "blur":
        gray = cv2.medianBlur(image, 3)
    else:
        gray = image

    # write the grayscale image to disk as a temporary file so we can
    # apply OCR to it
    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, gray)

    # load the image as a PIL/Pillow image, apply OCR, and then delete
    # the temporary file
    text = pytesseract.image_to_string(Image.open(filename))
    # os.remove(filename)

    return text


def main():
    filepath = "data/ocr_data/cv/index.png"
    img = cv2.imread(filepath)
    print(get_text_from_image(img))


if __name__ == '__main__':
    main()