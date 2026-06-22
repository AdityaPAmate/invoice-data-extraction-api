import requests

from django.conf import settings

BASE_URL = "https://gstverify.co.in/api/v1/verify"


def get_trade_name(gst_number):
    """
    Returns the trade name for a GST number.
    """

    if not gst_number:
        return None

    headers = {
        "X-API-Key": settings.GST_VERIFY_API_KEY
    }

    url = f"{BASE_URL}/{gst_number}"

    response = requests.get(
        url,
        headers=headers,
        timeout=10
    )

    response.raise_for_status()

    response_data = response.json()

    if response_data.get("success"):
        return response_data["data"]["trade_name"].strip().upper()

    return None


def verify_gst(parsed_data):

    master = parsed_data[0]["master"]

    company_name = master.get("company_name", "").strip().upper()
    customer_name = master.get("customer_name", "").strip().upper()

    company_gst = master.get("gst_no")
    customer_gst = master.get("customer_gst_no")

    company_trade_name = get_trade_name(company_gst)
    customer_trade_name = get_trade_name(customer_gst)

    print("Company Trade Name :", company_trade_name)
    print("Customer Trade Name:", customer_trade_name)

    # GST numbers are already correct
    if (
        company_trade_name == company_name and
        customer_trade_name == customer_name
    ):
        print("GST Numbers are Correct")
        return parsed_data

    # GST numbers are swapped
    elif (
        company_trade_name == customer_name and
        customer_trade_name == company_name
    ):
        print("GST Numbers are Swapped")

        master["gst_no"], master["customer_gst_no"] = (
            master["customer_gst_no"],
            master["gst_no"]
        )

        return parsed_data

    else:
        print("Unable to verify GST mapping")

    return parsed_data