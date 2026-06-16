import fitz
import numpy as np

from PIL import Image
from paddleocr import PaddleOCR

# Initialize only once
try:
    ocr = PaddleOCR(
        use_angle_cls=True,
        lang="en"
    )
except Exception as e:
    print(f"Failed to initialize PaddleOCR: {e}")
    raise


def extract_text_from_image(image_file):
    image = Image.open(image_file).convert("RGB")

    image_array = np.array(image)

    result = ocr.ocr(image_array)

    print(result)

    extracted_text = []

    for page in result:
        extracted_text.extend(page["rec_texts"])

    text = "\n".join(extracted_text)

    print(text)

    return text