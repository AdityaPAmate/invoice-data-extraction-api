def get_invoice_prompt(invoice_text):
    return f"""
You are an expert Invoice Data Extraction AI.

Task:
Extract invoice information from the provided invoice text and return ONLY valid JSON.

IMPORTANT RULES:
1. Return ONLY JSON.
2. Do NOT add explanations, markdown, comments, notes, or extra text.
3. Keep the JSON structure exactly as provided below.
4. Do NOT change key names.
5. Do NOT add new keys.
6. If a value is not found, return an empty string "" for text fields.
7. For numeric fields:
   - Return numbers without currency symbols.
   - Use 0 if the value is not available.
8. Extract all invoice details accurately from the invoice text.
9. Extract all line items into the "items" array.
10. Preserve dates exactly as printed in the invoice.
11. If multiple items exist, create multiple objects inside the "items" array.
12. If bank details are available, extract them.
13. Extract GST, PAN, CIN, FSSAI, HSN, tax percentages, tax amounts, totals, payment terms, buyer details, seller details, shipping details and any other available information.
14. Ensure the output is valid JSON that can be parsed directly using json.loads().
15. Do NOT wrap the response inside markdown code blocks.
16. Never guess values.
17. Never perform assumptions when a value is not explicitly available.
18. Every numeric value must come from the invoice itself or be calculated only if it is mathematically obvious.
19. Do not invent missing invoice fields.
20. Extract values exactly as printed on the invoice.

LINE ITEM EXTRACTION RULES
1. Every row in the invoice table represents one item.
2. Map columns according to the actual table header of that invoice.
Do NOT assume every invoice has Qty, Rate or UOM columns.
3. If the invoice contains a Qty column, map it to: "qty"
4. If the invoice does NOT contain a Qty column:
   - Return qty as 0.
   - Do NOT use Weight, TOT KG, Net Weight, Gross Weight, Pack Size, Pieces, Boxes, Cartons or any other column as qty unless the invoice explicitly labels it as Quantity or Qty.
5. If the invoice contains columns like:
   TOT KG, TOTAL KG, WEIGHT, NET WEIGHT, GROSS WEIGHT
these represent weight and NOT quantity. Do NOT map them to qty.
6. If the invoice does not contain a Rate column:
   - Return rate as 0.
   - Do NOT calculate or invent rate.
7. Do NOT derive rate using:
   Amount ÷ Qty, Taxable Amount ÷ Qty, Weight ÷ Amount or any other formula.
8. Only populate rate if it is explicitly printed in the invoice.
9. taxable_amount must be the taxable value before tax.
10. amount must be the final amount including applicable tax if that is how the invoice presents it.
Otherwise return the printed line total.
11. tax_percent must match the GST percentage printed for that item.
12. CGST, SGST, IGST and CESS percentages and amounts must be extracted from the invoice whenever available.
13. If taxable amount, GST percentage and final amount are present, preserve them exactly.
14. Do not swap Amount, Taxable Amount and Rate.
15. Do not infer missing columns.

MASTER TOTAL RULES

1. total_items = total number of item rows.
2. total_qty:
   - Return the invoice's total quantity only if it is explicitly available.
   - Do NOT calculate total_qty by summing weights, TOT KG, Pack Size, Boxes or any other column.
   - If no total quantity is available, return 0.
3. subtotal, taxable_amount, CGST, SGST, IGST, CESS, total_tax, round_off, grand_total and other totals must match the invoice exactly.
4. amount_in_words must match exactly as printed.
5. Do not perform unnecessary calculations if totals are already available.

JSON Structure:
[
  {{
    "master": {{
      "invoice_no": "",
      "invoice_type": "",
      "invoice_date": "",
      "reference_no": "",
      "buyer_order_no": "",
      "company_name": "",
      "address": "",
      "phone": "",
      "email": "",
      "website": "",
      "gst_no": "",
      "pan_no": "",
      "cin_no": "",
      "fssai_no": "",
      "fssai_expiry": "",
      "state_name": "",
      "state_code": "",
      "customer_code": "",
      "consignee_name": "",
      "customer_name": "",
      "customer_address": "",
      "shipping_address": "",
      "site_name": "",
      "mobile_no": "",
      "customer_email": "",
      "customer_gst_no": "",
      "food_lic_no": "",
      "dl_no": "",
      "customer_category": "",
      "customer_state_name": "",
      "customer_state_code": "",
      "gate_pass_no": "",
      "gate_pass_date": "",
      "pick_list_no": "",
      "sale_type": "",
      "terms_of_payment": "",
      "terms_of_delivery": "",
      "beneficiary_name": "", 
      "bank_name": "",
      "bank_address": "",
      "bank_account_no": "",
      "bank_ifsc": "",
      "bank_branch": "",
      "due_date": "",
      "place_of_supply": "",
      "shipping_mode": "",
      "remarks": "",
      "reverse_charge": "",
      "total_items": 0,
      "total_qty": 0,
      "sub_total": 0,
      "taxable_amount": 0,
      "total_cgst": 0,
      "total_sgst": 0,
      "total_igst": 0,
      "total_cess": 0,
      "total_tax": 0,
      "discount": 0,
      "cash_discount_amount": 0,
      "round_off": 0,
      "other_amount": 0,
      "other_amount_label": "",
      "grand_total": 0,
      "amount_in_words": "",
      "payment_mode": "",
      "payment_status": ""
    }},
    "items": [
      {{
        "sr_no": 0,
        "item_name": "",
        "description": "",
        "hsn_sac": "",
        "part_no": "",
        "batch_no": "",
        "expiry_date": "",
        "qty": 0,
        "uom": "",
        "packing_unit": "",
        "free_qty": 0,
        "rate": 0,
        "mrp": 0,
        "discount_percent": 0,
        "spl_discount": 0,
        "trade_discount": 0,
        "discount_amt": 0,
        "taxable_amount": 0,
        "cgst_pct": 0,
        "cgst_amt": 0,
        "sgst_pct": 0,
        "sgst_amt": 0,
        "igst_pct": 0,
        "igst_amt": 0,
        "cess_pct": 0,
        "cess_amt": 0,
        "tax_percent": 0,
        "tax_amount": 0,
        "amount": 0
      }}
    ]
  }}
]

Invoice Text:
{invoice_text}
Return ONLY the JSON output.
"""