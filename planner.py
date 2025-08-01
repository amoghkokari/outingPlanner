from apiRoutes import call_gemini, get_insights
from prompts import taste_extraction_prompt, itinerary_prompt, system_prompts
import json

def extract_preferences(user_input, api_key):
    """
    Extracts structured preferences from user's input using Gemini API.
    """
    prompt = taste_extraction_prompt.format(user_input=user_input)
    json_out = call_gemini(prompt, system_prompts['data_extractor'], api_key)
    return json_out


def call_qloo_insight_api(preferences, qloo_api_key):
    """
    Calls Qloo's insight API to get affinity-ranked places based on user preferences.
    """
    payload = {
        "filter.type": "urn:entity:place",
        "signal.location.query": preferences.destination,
        "sort_by": "affinity",
        "take": 10
    }

    route = "/v2/insights"
    qloo_resp = get_insights(payload, route, qloo_api_key)

    return qloo_resp


def extract_qloo_insight(preferences, qloo_api_key):
    """
    Processes Qloo API response and extracts relevant information about recommended places.
    """
    qloo_resp = call_qloo_insight_api(preferences, qloo_api_key)
    places = []

    for entity in qloo_resp['results']['entities']:
        place = {
            'name': entity['name'],
            'location': entity['location'],
            'disambiguation': entity['disambiguation'],
            'properties': entity['properties'],
            'tags': [tag['name'] for tag in entity['tags']]
        }
        places.append(place)

    return places


def build_itinerary(user_input, places, api_key):
    """
    Builds a personalized itinerary using Gemini API based on user input and Qloo places.
    """
    prompt = itinerary_prompt(user_input, places)
    json_out = call_gemini(prompt, system_prompts['travel_planner'], api_key, return_json=False)
    return json_out


def handle_user_input(user_input, timeframe, budget, destination, api_key, qloo_api_key):
    """
    Orchestrates the full flow:
    1. Enriches user input with budget, timeframe, and destination
    2. Extracts preferences using Gemini
    3. Fetches insights from Qloo
    4. Builds final itinerary using Gemini
    """
    enriched_input = (
        f"{user_input}, TimeFrame: {timeframe}, "
        f"Budget_Range: {budget}, Destination: {destination}"
    )

    preferences = extract_preferences(enriched_input, api_key)
    places = extract_qloo_insight(preferences, qloo_api_key)
    travel_plan = build_itinerary(enriched_input, places, api_key)

    return travel_plan
