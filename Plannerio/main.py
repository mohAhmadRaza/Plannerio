import streamlit as st
import anthropic
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
api_key = os.getenv("ANTHROPIC_API_KEY")
client = anthropic.Anthropic(api_key=api_key)


# Function to display the app name in a circular interface
def display_app_name():
    st.markdown(
        """
        <div style="
            width: 150px;
            height: 150px;
            border-radius: 50%;
            background-color: #FF5722; /* Dark orange */
            color: white;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
            font-weight: bold;
            margin: auto;
            text-align: center;
        ">
            Plannerio
        </div>
        """,
        unsafe_allow_html=True
    )

# Display the app name
display_app_name()


# App title and sidebar disclaimer
st.title("Plannerio - Meal Plan Recommendation")
st.sidebar.header("Disclaimer")
st.sidebar.write(
    """
    Before starting any new meal plan, please consult with your family doctor to ensure it is suitable for your health needs.
    """
)

# User inputs
st.header("Please provide the following information:")

# Input fields
age = st.number_input("Age", min_value=1, max_value=120, value=25)
gender = st.selectbox("Gender", ["Select", "Male", "Female", "Other"])
activity_level = st.selectbox("Activity Level", ["Select", "Sedentary", "Moderately Active", "Active"])
dietary_restrictions = st.text_input("Dietary Restrictions (if any)")
goal = st.selectbox("Health Goal", ["Select", "Weight Loss", "Muscle Gain", "Maintain Weight"])
caloric_intake = st.number_input("Daily Caloric Intake", min_value=500, max_value=5000, value=2000)


# Button to get recommendation
if st.button("Get Meal Plan Recommendation"):
    # Basic recommendation logic (placeholder)
    if gender == "Select" or activity_level == "Select" or goal == "Select":
        st.error("Please select all required options.")
    else:
        # Example recommendation logic
        prompt = (
            f"**Meal Plan Recommendation Request**\n\n"
            f"**User Profile:**\n"
            f"- **Age:** {age}\n"
            f"- **Gender:** {gender}\n"
            f"- **Activity Level:** {activity_level}\n"
            f"- **Dietary Restrictions:** {dietary_restrictions if dietary_restrictions else 'None'}\n"
            f"- **Health Goal:** {goal}\n"
            f"- **Daily Caloric Intake:** {caloric_intake} calories\n\n"
            f"**Objective:**\n"
            f"Based on the provided information, please generate a customized meal plan that aligns with the user’s age, gender, activity level, dietary restrictions, health goal, and caloric intake. The meal plan should be balanced, nutritious, and tailored to meet the specific needs and preferences of the user. Include recommendations for breakfast, lunch, dinner, and snacks. Ensure the meal plan supports the user’s health goal effectively."
        )
        message = client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=250,
            temperature=0.7,
            system="You are a meal planner specialist",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        first = message.content
        second = first[0].text
        st.markdown(second)

        # Display additional recommendations or advice
        st.write("### Additional Recommendations")
        st.write("1. Include a variety of fruits and vegetables in your diet.")
        st.write("2. Stay hydrated by drinking plenty of water.")
        st.write("3. Monitor your progress and adjust your meal plan as needed.")

