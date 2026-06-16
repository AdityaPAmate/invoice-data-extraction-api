import fitz
import numpy as np

from PIL import Image
from paddleocr import PaddleOCR

ocr = None


def get_ocr():
    global ocr

    if ocr is None:
        print("Loading PaddleOCR model...")
        ocr = PaddleOCR(
            use_angle_cls=True,
            lang="en"
        )
        print("PaddleOCR loaded successfully.")

    return ocr


def extract_text_from_image(image_file):
    image = Image.open(image_file).convert("RGB")

    image_array = np.array(image)

    import gc

    result = get_ocr().ocr(image_array)

    extracted_text = []

    for page in result:
        extracted_text.extend(page["rec_texts"])

    text = "\n".join(extracted_text)

    del image_array
    del result

    gc.collect()

    return text