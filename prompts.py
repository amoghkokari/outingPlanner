# -------------------------------
# Prompt for extracting preferences from user input
# -------------------------------

taste_extraction_prompt = """
See if you can extract the following fields from the user's input:

- Artist
- Book
- Brand
- Destination (at least the state; infer from context)
- Movie
- Person
- Place
- Podcast
- TV Show
- Video Game
- Group type (e.g., solo, couple, family)
- Age group (e.g., 25–35)
- Preferences (music, food, activity styles)
- Budget (low, medium, high, or specific value)
- Timeframe (e.g., this weekend)

Respond in **valid JSON** format only.

User input: "{user_input}"
"""

# -------------------------------
# System instructions for Gemini model roles
# -------------------------------

system_prompts = {
    'data_extractor': (
        "You are an expert data extractor, skilled at identifying structured information "
        "from casual user language. Extract information with precision and return only valid JSON."
    ),
    'travel_planner': (
        "You are a friendly and knowledgeable local trip planning assistant. "
        "Use your local insights to help users enjoy their ideal weekend or short getaway."
    )
}

# -------------------------------
# Function to generate a travel itinerary prompt
# -------------------------------

def itinerary_prompt(user_input, qloo_places):
    """
    Creates a custom prompt to send to Gemini for generating a travel itinerary.
    
    Args:
        user_input (str): Raw input from the user
        qloo_places (list): Qloo-enhanced place recommendations

    Returns:
        str: Full prompt string for Gemini travel planner
    """
    
    return f"""
You are a local trip planner assistant.

User Input:
"{user_input}"

Qloo Recommendations:
{qloo_places}

---

Your job is to write a **personalized travel itinerary** that incorporates the user's input and the recommended places.

Make sure the itinerary:
- Acknowledges the user's mood or current state
- Aligns with their interests, preferences, and group type
- Focuses on the selected destination and explains why it's a good fit
- Suggests fun or relaxing activities within budget
- Sounds friendly and natural (not robotic)
- Uses bullet points or short paragraphs for clarity
- Covers timing, costs, and best activities for the day(s)

Do **not** output structured data or code.
Respond like a helpful local concierge giving thoughtful recommendations.
"""
