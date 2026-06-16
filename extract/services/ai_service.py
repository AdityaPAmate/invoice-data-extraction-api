import os

from google import genai

from ..prompts.invoice_prompt import get_invoice_prompt

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable is not set.")

client = genai.Client(api_key=GEMINI_API_KEY)


def extract_invoice_data(invoice_text):
    """
    Sends invoice text to Gemini and returns
    the extracted JSON response.
    """

    prompt = get_invoice_prompt(invoice_text)
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text
    except Exception as e:
        raise  Exception(f"Gemini API Error: {str(e)}")