messages = [
    {
        "role": "system",
        "content": "You are a product cataloging expert who provides concise classifications and descriptions."
    }
]

# Add user message with text and image
messages.append({
    "role": "user",
    "content": [
        {
            "type": "input_text",
            "text": "Classify this product and write a brief but punchy description for our catalog."
        },
        {
            "type": "input_image",
            "image_url": image_url
        }
    ]
})

# Create the response
response = client.responses.create(
    model="gpt-5.4-mini",
    input=messages
)

print(response.output_text)
visualize_image(image_url)