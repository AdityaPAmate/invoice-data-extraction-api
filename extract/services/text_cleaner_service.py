import re

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