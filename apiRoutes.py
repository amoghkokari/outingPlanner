from pydantic import BaseModel, Field
from typing import Optional, List, Any
from google import genai
import requests

# -------------------------------
# User preference schema used for parsing Gemini responses
# -------------------------------
class PreferenceInfo(BaseModel):
    artist: Optional[List[str]] = Field(default=None, description="List of artists (e.g., musicians, performers)")
    book: Optional[List[str]] = Field(default=None, description="Books or authors")
    brand: Optional[List[str]] = Field(default=None, description="Brands or products")
    destination: Optional[str] = Field(default=None, description="Specific travel destination (e.g., NYC, Paris)")
    movie: Optional[List[str]] = Field(default=None, description="Movies")
    place: Optional[List[str]] = Field(default=None, description="Local places (e.g., 'museums', 'cafes')")
    podcast: Optional[List[str]] = Field(default=None, description="Podcasts or genres")
    tv_show: Optional[List[str]] = Field(default=None, description="TV shows or series")
    video_game: Optional[List[str]] = Field(default=None, description="Video games")
    location: Optional[str] = Field(default=None, description="Current location (e.g., city)")
    group_type: Optional[str] = Field(default=None, description="Group type (e.g., solo, couple)")
    age_group: Optional[str] = Field(default=None, description="Age group (e.g., 25-35)")
    preferences: Optional[List[str]] = Field(default=None)
    budget: Optional[str] = Field(default=None, description="Budget estimate or range")
    timeframe: Optional[str] = Field(default=None, description="Timeframe (e.g., this weekend)")
    current_state: Optional[str] = Field(default=None, description="Current mood or state")

# -------------------------------
# Generic Gemini API call function
# -------------------------------
def call_gemini(prompt, system_prompt, gemini_api_key, return_json=True):
    """
    Calls Gemini 2.5 Flash model with optional JSON schema parsing.

    Args:
        prompt (str): Prompt string to send to the model
        system_prompt (str): Instruction for the system
        gemini_api_key (str): API key for Gemini
        return_json (bool): If True, returns parsed JSON; else plain text

    Returns:
        Parsed response or raw text from Gemini
    """
    genai_client = genai.Client(api_key=gemini_api_key)

    config_kwargs = {
        "system_instruction": system_prompt,
        "temperature": 0.3,
        "seed": 142
    }

    # Add schema only if expecting JSON response
    if return_json:
        config_kwargs["response_mime_type"] = "application/json"
        config_kwargs["response_schema"] = PreferenceInfo

    response = genai_client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
        config=genai.types.GenerateContentConfig(**config_kwargs)
    )

    return response.parsed if return_json else response.text

# -------------------------------
# Qloo Insight API wrapper
# -------------------------------
def get_insights(payload, route, qloo_api_key):
    """
    Makes a POST request to Qloo's insights API.

    Args:
        payload (dict): Query parameters for Qloo API
        route (str): Route path (e.g., /v2/insights)
        qloo_api_key (str): API key for Qloo

    Returns:
        JSON response from Qloo or empty dict on failure
    """
    base_url = "https://hackathon.api.qloo.com"
    url = f"{base_url}{route}"

    headers = {
        "accept": "application/json",
        "X-Api-Key": qloo_api_key
    }

    try:
        response = requests.post(url, headers=headers, params=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"[Qloo API error] {e}")
        return {}
