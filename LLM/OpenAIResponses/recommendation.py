# Combine the features for last_product and each product
last_product_text = "computer science"
product_texts = [
    create_product_text(product)
    for product in products
]

# Embed last_product_text and product_texts
last_product_embedding = create_embeddings(last_product_text)
product_embeddings = create_embeddings(product_texts)

# Extract the query embedding
last_product_embedding = last_product_embedding[0]

# Find the three closest products
hits = find_n_closest(
    last_product_embedding,
    product_embeddings,
    3
)

for hit in hits:
    product = products[hit['index']]
    print(product['title'])
    
    
    
# Prepare and embed the user_history, and calculate the mean embeddings
history_texts = [create_product_text(article) for article in user_history]

history_embeddings = create_embeddings(history_texts)

mean_history_embeddings = np.mean(history_embeddings, axis=0)

# Filter products to remove any in user_history
products_filtered = [
    product for product in products
    if product not in user_history
]

# Combine product features and embed the resulting texts
product_texts = [
    create_product_text(product) for product in products_filtered
]

product_embeddings = create_embeddings(product_texts)

hits = find_n_closest(mean_history_embeddings, product_embeddings)

for hit in hits:
    product = products_filtered[hit['index']]
    print(product['title'])