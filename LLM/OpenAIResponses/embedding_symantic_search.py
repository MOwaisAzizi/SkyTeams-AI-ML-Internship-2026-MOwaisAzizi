# Define a function to combine relevant product information
from scipy.spatial import distance

def create_product_text(product):
    return f"""Title: {product["title"]}
Description: {product["short_description"]}
Category: {product["category"]}
Features: {product["features"]}"""

# Combine information for each product
product_texts = [
    create_product_text(product)
    for product in products
]

# Create embeddings
product_embeddings = create_embeddings(product_texts)


def find_n_closest(query_vector, embeddings, n=3):
    distances = []

    for index, embedding in enumerate(embeddings):

        # Calculate cosine distance
        dist = distance.cosine(query_vector, embedding)

        # Store distance and index
        distances.append({
            "distance": dist,
            "index": index
        })

    # Sort by smallest distance
    distances_sorted = sorted(
        distances,
        key=lambda x: x["distance"]
    )

    # Return the n closest results
    return distances_sorted[:n]

# Create the query vector from query_text
query_text = "computer"
query_vector = create_embeddings(query_text)[0]

# Find the five closest distances
hits = find_n_closest(query_vector, product_embeddings, 5)

print(f'Search results for "{query_text}"')

for hit in hits:
    # Extract the product at each index in hits
    product = products[hit["index"]]
    print(product["title"])