from pydantic import BaseModel, Field
# Define the book recommendation schema
class MovieRecommendation(BaseModel):
    title: str = Field(description="The movie title")
    genre: str = Field(description="Primary genre")
    vibe: str = Field(description="One-word vibe: cozy, thrilling, emotional, or fun")
    why: str = Field(description="One sentence explaining why this matches")

# Generate structured recommendation
response = client.responses.parse(
    model="gpt-5.4-mini",
    instructions="You are a knowledgeable movie recommender.",
    input="Recommend a movie for someone who loved Inception and wants something mind-bending",
    text_format=MovieRecommendation,
)

# Extract the parsed output and results
recommendation = response.output_parsed
print(f"Title: {recommendation.title}")
print(f"Reason: {recommendation.why}")