# gpt.py
import json
from openai import OpenAI

client = OpenAI()

CATEGORIES = ["Meals", "Transport", "Lodging", "Office Supplies", 
"Entertainment", "Other"]

def extract_receipt_info(image_b64):
    """
    Extract the information from the receipt image with ChatGPT LLM Api

    Args:
        image_b64 (str): The image file in form of base64 encoding.
    
    Returns:
        dict: A JSON-parsed dictionary with the following keys:
            - date (str | None): The receipt date.
            - amount (str | None): The total amount paid as shown on the receipt.
            - vendor (str | None): The merchant or vendor name.
            - category (str | None): One of the allowed categories, or null if unknown.
    """
    prompt = f"""
You are an information extraction system.
Extract ONLY the following fields from the receipt image:

date: the receipt date as a string
amount: the total amount paid as it appears on the receipt
vendor: the merchant or vendor name
category: one of [{", ".join(CATEGORIES)}]

Return EXACTLY one JSON object with these four keys and NOTHING ELSE.
Do not include explanations, comments, or formatting.
Do not wrap the JSON in markdown.
If a field cannot be determined, use null.

The output must be valid JSON.
"""
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        seed=43,
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_b64}"
                        }
                    }
                ]
            }
        ]
    )
    json_response = json.loads(response.choices[0].message.content)

    if '$' in json_response["amount"]:
        json_response["amount"] = json_response["amount"].replace("$", "")
    
    json_response["amount"] = float(json_response["amount"])
    
    return json_response

