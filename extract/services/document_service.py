import fitz
from .image_text_extractor_service import extract_text_from_image

def extract_text_from_document(uploaded_file):
    content_type = uploaded_file.content_type
    # print(content_type)

    if content_type == "application/pdf":
        try:
            document = fitz.open(stream=uploaded_file.read(), filetype="pdf")

            extracted_text = []

            for page in document:
                extracted_text.append(page.get_text())

            document.close()
            # print('this is extracted text: ', "\n".join(extracted_text))
            return "\n".join(extracted_text)
        except:
            raise Exception('Unable to read the PDF File.')


    elif content_type in ["image/png", "image/jpeg", "image/jpg"]:
        # print('ocr')
        return extract_text_from_image(uploaded_file)


    else:

        raise Exception("Unsupported file type.")