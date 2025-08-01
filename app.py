import streamlit as st
from planner import handle_user_input

def main():
    # Set the Streamlit page configuration
    st.set_page_config(page_title="TasteTrip Local", page_icon="🎒")
    
    # App header and introduction
    st.title("🎒 TasteTrip Local")
    st.subheader("Tell me what you love, and I’ll plan your weekend!")

    # Sample prompt to guide user input
    seed_prompt = (
        "I don't know, had very heavy week, want to do something nearby in New Jersey "
        "this weekend, relax, also enjoy summer, maybe go to music show, dont want to "
        "spend more than $100"
    )

    # Initialize session state for key planning inputs
    if 'budget' not in st.session_state:
        st.session_state.budget = None
    
    if 'timeframe' not in st.session_state:
        st.session_state.timeframe = None

    if 'destination' not in st.session_state:
        st.session_state.destination = None

    # API Key input: Google Generative AI
    api_key = st.text_input('Enter Google Generative AI API KEY (Required)', type="password")
    st.link_button(
        "Click to get API KEY (select create api key in new project)",
        "https://makersuite.google.com/app/apikey",
        type="secondary"
    )

    # API Key input: Qloo
    qloo_api_key = st.text_input('Enter Qloo API KEY (Required)', type="password")
    
    # Inform the user of required fields
    st.write("⛔ Budget, Timeframe and destination are must")

    # Get user inputs for planning
    st.session_state.timeframe = st.text_area(
        label="When do you want to plan for this",
        value="coming weekend or Friday?",
        height=68
    )

    st.session_state.budget = st.slider(
        label="How much do you want to spend for this in dollars ($)",
        min_value=60, max_value=2000, value=(60, 120)
    )

    st.session_state.destination = st.text_area(
        label="Where do you want to go? (city, state, country/countries or demographic)",
        value="somewhere near New Jersey",
        height=68
    )

    # Suggest including more personal preferences for a tailored plan
    st.write(
        "✨ Including more about you—like your favorite artist, book, movie, podcast, "
        "TV show, video game, location, group type, age group, preferences, and current "
        "state of mind—will enhance your experience!"
    )

    user_input = st.text_area(
        label="What do you feel like doing during this outing",
        value=seed_prompt
    )
    
    # Main action button to generate plan
    if (
        st.button("Plan My Weekend")
        and user_input
        and st.session_state.budget
        and st.session_state.timeframe
        and st.session_state.destination
        and api_key
        and qloo_api_key
    ):
        itinerary = handle_user_input(
            user_input,
            st.session_state.timeframe,
            st.session_state.budget,
            st.session_state.destination,
            api_key,
            qloo_api_key
        )
        st.markdown("### 🗺️ Your Weekend Plan")
        st.markdown(itinerary)

    # Footer with credits and links
    st.write(
        "Made with ❤️ by Amogh Mahadev Kokari ©️ 2025 &nbsp;&nbsp;||&nbsp;&nbsp;"
        "[LinkedIn](https://www.linkedin.com/in/amoghkokari/) &nbsp;&nbsp;||&nbsp;&nbsp;"
        "[Portfolio](https://amoghkokari.github.io/portfolio.pdf) &nbsp;&nbsp;||&nbsp;&nbsp;"
        "[GitHub](https://github.com/amoghkokari)"
    )


# Entry point for running the Streamlit app
if __name__ == "__main__":
    main()
