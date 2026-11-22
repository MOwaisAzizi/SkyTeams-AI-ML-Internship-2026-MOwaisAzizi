# Import base64 module
import base64

# Encode the image file as base64
with open(image_path, "rb") as f:
    image_base64 = base64.b64encode(f.read()).decode("utf-8")

# Create a response with text and image input
response = client.responses.create(
    model="gpt-5.4-mini",
    input=[
        {"role": "user", "content": [
            {"type": "input_text", "text": "What mode of transport contributed the highest number of vehicles during business hours? Answer very concisely."},
            {"type": "input_image", "image_url": f"data:image/png;base64,{image_base64}"}
        ]}
    ]
)

print(response.output_text)
visualize_image(image_url)