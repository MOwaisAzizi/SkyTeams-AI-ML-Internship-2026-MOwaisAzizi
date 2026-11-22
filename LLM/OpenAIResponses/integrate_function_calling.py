import json
import requests
from openai import OpenAI

client = OpenAI()

def convert_timezone(date_time, from_timezone, to_timezone):
    url = "https://api.opentimezone.com/convert"

    payload = {
        "dateTime": date_time,
        "fromTimezone": from_timezone,
        "toTimezone": to_timezone
    }

    response = requests.post(url, json=payload)
    response.raise_for_status()

    data = response.json()
    return f"Time in {to_timezone}: {data.get('dateTime', 'N/A')}"


tools = [{
    "type": "function",
    "name": "convert_timezone",
    "description": "Convert a datetime between timezones.",
    "parameters": {
        "type": "object",
        "properties": {
            "date_time": {"type": "string"},
            "from_timezone": {"type": "string"},
            "to_timezone": {"type": "string"}
        },
        "required": ["date_time", "from_timezone", "to_timezone"],
        "additionalProperties": False
    }
}]
messages = [
    {
        "role": "user",
        "content": "What time is 2:30pm on January 20th in New York in Tokyo time?"
    }
]

# First API request
response = client.responses.create(
    model="gpt-5.4-mini",
    input=messages,
    tools=tools
)

# Add the model's response (function call) to conversation history
messages += response.output

print("---------------------")
print(response.output_text)

# Process function calls and execute the timezone conversion
for item in response.output:
    if item.type == "function_call":
        if item.name == "convert_timezone":

            timezone_result = convert_timezone(
                **json.loads(item.arguments)
            )

            messages.append({
                "type": "function_call_output",
                "call_id": item.call_id,
                "output": json.dumps({
                    "convert_timezone": timezone_result
                })
            })

# Second API request with function results
response = client.responses.create(
    model="gpt-5.4-mini",
    input=messages,
    tools=tools
)

print("---------------------")
print(response.output_text)