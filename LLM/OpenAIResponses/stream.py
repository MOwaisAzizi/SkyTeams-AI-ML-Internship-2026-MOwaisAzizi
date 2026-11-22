prompt = "List the core ingredients to make classic egg pasta pasta in a single line."

# Open a connection for a streaming request
OpenAI.client.responses.create(model="gpt-5.4-mini", input=prompt, stream=true) as stream:
    current_text = ""

    # Complete the output text streaming
    for event in stream:
        if event.type == "response.output_text.delta":
            current_text += event.delta
            print(current_text)