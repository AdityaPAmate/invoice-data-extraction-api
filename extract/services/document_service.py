import re
import fitz
import  gc
from .image_text_extractor_service import extract_text_from_image
from .text_cleaner_service import clean_invoice_text

def extract_text_from_document(uploaded_file):
    content_type = uploaded_file.content_type

    if content_type == "application/pdf":
        try:
            document = fitz.open(
                stream=uploaded_file.read(),
                filetype="pdf"
            )
            del uploaded_file
            extracted_text = []

            for page in document:
                extracted_text.append(page.get_text())

            document.close()

            # Join all page text
            text = "\n".join(extracted_text)
            del extracted_text
            # Clean extracted text
            text = clean_invoice_text(text)
            gc.collect()
            return text


        except Exception:
            raise Exception("Unable to read the PDF File.")
        #
        # finally:
        #     if document:
        #         document.close()

    elif content_type in ["image/png", "image/jpeg", "image/jpg"]:
        return extract_text_from_image(uploaded_file)

    else:
        raise Exception("Unsupported file type.")