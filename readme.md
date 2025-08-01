# 🎒 TasteTrip Local

**Your AI-powered weekend travel planner.**  
Tell it how you feel, what you like, and where you want to go — and let TasteTrip craft your perfect weekend plan.

---

## 🧭 Features

- 💬 Natural language input for personalized travel recommendations
- 🧠 Uses Gemini 2.5 for smart preference extraction
- 🌐 Integrates Qloo API to recommend music, places, and activities
- 🗺️ Generates a full itinerary based on your mood, budget, and location

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/your-username/taste-trip-local.git
cd taste-trip-local
```

### 2. Create a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the app
```bash
streamlit run app.py
```

## 🔑 API Keys Required
You will need the following:

-   Google Generative AI API Key → [Get it here](https://aistudio.google.com/app/apikey)

-   Qloo API Key → [Apply for access via Qloo](https://www.qloo.com/)

Enter these keys in the Streamlit UI when prompted.

## 📁 Project Structure
```bash
app.py                 # Main Streamlit frontend
planner.py             # Core logic for input handling & itinerary
apiRoutes.py           # API wrappers for Gemini & Qloo
prompts.py             # Prompt templates and system instructions
requirements.txt       # Dependencies
README.md              # This file
```

## ✨ Credits
Built with ❤️ by Amogh Mahadev Kokari
-   [Portfolio](https://amoghkokari.github.io/portfolio.pdf)
-   [Linkedin](https://www.linkedin.com/in/amoghkokari/)

## 🧪 Sample Inputs
Try pasting this into the input box:

    “I’m exhausted from work and want to do something chill this weekend in New Jersey — maybe some music and fresh air, budget under $100.”

