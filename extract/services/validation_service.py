import json
import gc
from .gst_service import verify_gst
def validate_gemini_response(response_text):
    """
    Cleans Gemini output and converts it into a Python object.
    """
    # Remove Markdown code fences if present
    cleaned_text = (
        response_text.replace("```json", "").replace("```", "").strip()
    )
    del response_text
    try:
        # Convert JSON string into Python object
        parsed_data = json.loads(cleaned_text)
        del cleaned_text
        gc.collect()
    except json.JSONDecodeError as e:
        raise ValueError(
            f"Gemini returned invalid JSON.\nError: {e}\nResponse:\n{cleaned_text}"
        )

    # -----------------------------
    # Structural Validation
    # -----------------------------

    if not isinstance(parsed_data, list):
        raise ValueError("Gemini response must be a list of invoices.")

    if len(parsed_data) == 0:
        raise ValueError("Gemini returned an empty invoice list.")

    for index, invoice in enumerate(parsed_data, start=1):

        if not isinstance(invoice, dict):
            raise ValueError(
                f"Invoice {index} must be a JSON object."
            )

        if "master" not in invoice:
            raise ValueError(
                f"Invoice {index} is missing the 'master' section."
            )

        if "items" not in invoice:
            raise ValueError(
                f"Invoice {index} is missing the 'items' section."
            )

        if not isinstance(invoice["master"], dict):
            raise ValueError(
                f"'master' in Invoice {index} must be an object."
            )

        if not isinstance(invoice["items"], list):
            raise ValueError(
                f"'items' in Invoice {index} must be a list."
            )

        gst_verified_data=verify_gst(parsed_data)
        # print(gst_verified_data)

    return gst_verified_data