# Extract a list of product short descriptions from products
product_descriptions = [
    product['short_description'] for product in products
]
print(product_descriptions[0])
print("----------------------")
# Create embeddings for each product description using batching
response = client.embeddings.create(
    model="text-embedding-3-small",
    input=product_descriptions
)

response_dict = response.model_dump()
print(response_dict)
# Extract the embeddings from response_dict and store in products
for i, product in enumerate(products):
    product['embedding'] = response_dict["data"][i]["embedding"]

print(products[0].items())