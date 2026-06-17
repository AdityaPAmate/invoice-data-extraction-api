from django.http import JsonResponse
from .services.document_service import extract_text_from_document
from .services.image_text_extractor_service import extract_text_from_image
from django.views.decorators.csrf import csrf_exempt
from .services.ai_service import extract_invoice_data
from .services.validation_service import validate_gemini_response
from .services.memory_service import log_memory_usage
import gc
@csrf_exempt
def extract_invoice(request):
    if request.method == "POST":
        log_memory_usage('Started')
        file = request.FILES.get("file")

        if not file:
            return JsonResponse({
                "error": "No PDF file uploaded."
            }, status=400)
        try:
            invoice_text = extract_text_from_document(file)
            log_memory_usage('After text extraction: ')

            log_memory_usage('Before Gemini: ')
            gemini_response = extract_invoice_data(invoice_text)
            log_memory_usage('After Gemini: ')
            validated_response = validate_gemini_response(gemini_response)
            log_memory_usage('After Validation: ')

            response_data= {
                "success": True,
                "message": "Invoice extracted successfully.",
                "data": validated_response
            }

            del invoice_text
            del gemini_response
            del validated_response
            gc.collect()
            log_memory_usage('Final: ')
            return JsonResponse(response_data)
        except Exception as e:
            return  JsonResponse({
                'error': str(e)
            }, status= 500)


    return JsonResponse({
        "error": "Only POST requests are allowed."
    }, status=405)