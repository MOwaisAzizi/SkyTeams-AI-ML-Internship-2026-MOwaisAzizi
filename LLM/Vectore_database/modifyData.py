new_data = [
    {
        "id": "s100",
        "document": "A heartwarming film about a dog and its friendship with a young boy."
    },
    {
        "id": "s101",
        "document": "A documentary about wild animals and their natural habitats."
    },
    {
        "id": "s102",
        "document": "A comedy film about a family that adopts a mischievous puppy."
    }
]

collection = client.get_collection(
  name="netflix_titles",
  embedding_function=OpenAIEmbeddingFunction(model_name="text-embedding-3-small", api_key="<OPENAI_API_TOKEN>")
)

# Update or add the new documents
collection.upsert(
    ids=[doc['id'] for doc in new_data],
    documents=[doc['document'] for doc in new_data]
)

# Delete the item with ID "s95" and re-run the query
collection.delete(ids=["s95"])

result = collection.query(
    query_texts=["films about dogs"],
    n_results=3
)
print(result)