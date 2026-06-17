import re
import fitz
import  gc
from .image_text_extractor_service import extract_text_from_image


def clean_invoice_text(text):
    """
    Clean extracted invoice text before sending it to Gemini.
    This function performs only safe, generic cleaning.
    """

    # Remove separator lines like:
    # - - - - - - - - - -
    # -------------------
    text = re.sub(r'(\s*-\s*){5,}', '', text)

    # Replace multiple spaces or tabs with a single space
    text = re.sub(r'[ \t]{2,}', ' ', text)

    # Replace 3 or more consecutive blank lines with 2
    text = re.sub(r'\n{3,}', '\n\n', text)

    # Strip whitespace from each line
    lines = [line.strip() for line in text.splitlines()]

    # Remove empty lines
    lines = [line for line in lines if line]

    return "\n".join(lines)


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

    elif content_type in ["image/png", "image/jpeg", "image/jpg"]:
        return extract_text_from_image(uploaded_file)

    else:
        raise Exception("Unsupported file type.")