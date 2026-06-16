# AI Invoice Data Extraction System

## Overview

AI Invoice Data Extraction System is a Django REST API that automatically extracts structured data from invoice images and PDF files.

The system uses **PaddleOCR** to extract text from invoices and **Google Gemini 2.5 Flash** to convert the extracted text into a standardized JSON containing invoice details and line items.

This API can be integrated with ERP, accounting, or invoice management systems to automate manual data entry.

---

## Features

* Upload invoice as PDF or image
* Supports PDF, PNG, JPG, and JPEG formats
* Automatic OCR using PaddleOCR
* AI-powered data extraction using Google Gemini
* Returns structured JSON
* Extracts invoice master details
* Extracts invoice line items
* Modular service-based architecture
* REST API built using Django REST Framework

---

## Technology Stack

### Backend

* Python
* Django
* Django REST Framework

### OCR

* PaddleOCR

### AI

* Google Gemini 2.5 Flash
* Google AI Studio API

### PDF Processing

* PyMuPDF (fitz)

### Image Processing

* Pillow (PIL)
* NumPy

### Testing

* Postman

---

## Project Structure

```text
file_extractor/

├── extract/
│   ├── prompts/
│   ├── services/
│   ├── utils/
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── file_extractor/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── manage.py
├── requirements.txt
└── README.md
```

---

## API Workflow

1. Upload invoice (PDF/Image)
2. Detect file type
3. Convert PDF pages into images (if required)
4. Extract text using PaddleOCR
5. Generate prompt
6. Send prompt to Google Gemini
7. Receive structured JSON
8. Return API response

---

## API Response

The API returns structured JSON containing:

* Invoice Information
* Company Details
* Buyer Details
* GST Details
* Tax Information
* Bank Details
* Totals
* Line Items

---

## Installation

Clone the repository

```bash
git clone <repository-url>
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file and add your Gemini API key.

```text
GEMINI_API_KEY=your_api_key_here
```

Run the Django server

```bash
python manage.py runserver
```

---

## API Testing

The API can be tested using Postman.

Example endpoint:

```
POST /api/upload-invoice/
```

Upload the invoice using **form-data** with the invoice file.

---

## Future Improvements

* Database storage
* Invoice history
* User authentication
* Batch invoice processing
* Confidence scores
* OCR preprocessing
* Multi-page invoice optimization
* ERP integration
* Export to Excel and CSV

---

## Author

Aditya Amate

Computer Engineering Student

Python | Django | SQL | AI Integration
