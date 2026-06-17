from django.http import JsonResponse
from .services.document_service import extract_text_from_document
from .services.image_text_extractor_service import extract_text_from_image
from django.views.decorators.csrf import csrf_exempt
from .services.ai_service import extract_invoice_data
from .services.validation_service import validate_gemini_response
import gc
@csrf_exempt
def extract_invoice(request):
    if request.method == "POST":
        file = request.FILES.get("file")

        if not file:
            return JsonResponse({
                "error": "No PDF file uploaded."
            }, status=400)
        try:
            invoice_text = extract_text_from_document(file)
            del file
            gemini_response = extract_invoice_data(invoice_text)
            del invoice_text
            gc.collect()
            validated_response = validate_gemini_response(gemini_response)

            return JsonResponse({
                "success": True,
                "message": "Invoice extracted successfully.",
                "data": validated_response
            })
        except Exception as e:
            return  JsonResponse({
                'error': str(e)
            }, status= 500)


    return JsonResponse({
        "error": "Only POST requests are allowed."
    }, status=405)