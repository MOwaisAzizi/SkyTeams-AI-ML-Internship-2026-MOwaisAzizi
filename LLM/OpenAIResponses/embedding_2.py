# Define a create_embeddings function
def create_embeddings(texts):
  response = client.embeddings.create(
    model="text-embedding-3-small",
    input=texts
  )
  response_dict = response.model_dump()
  
  return [data['embedding'] for data in response_dict['data']]

# Embed short_description and print

print(create_embeddings('short_description'))

# Embed list_of_descriptions and print
print(create_embeddings(['this is anohter text', 'and that is another one too']))