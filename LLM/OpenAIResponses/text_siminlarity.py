from scipy.spatial import distance

# Embed the search text
search_text = "soap"
search_embedding = create_embeddings(search_text)[0]

distances = []

for product in products:
    # Compute cosine distance for each product embedding
    dist = distance.cosine(search_embedding, product['embedding'])
    distances.append(dist)

# Find the index of the smallest distance
min_dist_ind = np.argmin(distances)

# Print the most similar product short_description
print(products[min_dist_ind]['short_description'])