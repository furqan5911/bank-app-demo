
import streamlit as st
import google.generativeai as genai

API_KEY = "AIzaSyD4fcsx2GHbl4WNWgPkoJLof7uxmDf66MY"
genai.configure(api_key=API_KEY)
 
# Configure Streamlit page
st.set_page_config(page_title="💬 Service Chatbot")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Define the options for the dropdown menu with descriptions
services = {
    "Invite Friends": "Users can send referrals directly via Easypaisa chatbot (SMS, WhatsApp, Email), track referral rewards, and see how many friends have successfully signed up.",
    "Easyload and Bill Payments": "Users can schedule recurring mobile top-ups or perform one-time top-ups via the chatbot. Utility bill payments are simplified with automated processes.",
    "Rewards Management": "Track and redeem loyalty points, cashback, or rewards. Personalized offers are provided based on user behavior and transaction history.",
    "Utility Bill Payments": "Fetch bill information (e.g., amount due, last payment) and pay utility bills through a conversational flow. Recurring bill payments are also supported.",
    "Savings and Goals": "Set savings goals (e.g., vacations, purchases) and automate small regular contributions. Progress monitoring helps users track goal achievements.",
    "Debit Card Management": "Request new or replacement debit cards, activate cards, and manage card-related queries through the chatbot.",
    "One-Stop Shop for All Services": "Explore all available Easypaisa services via a directory. Access links to popular services like money transfers and ticket booking.",
    "Gift Services": "Send and receive gifts via the chatbot. Personalized gift suggestions are offered based on user activity and special occasions.",
    "Ticket Booking": "Automate the ticket booking process for events and travel. Get real-time updates on ticket status and booking reminders.",
    "Retail Locator (Near Retailer)": "Find the nearest Easypaisa agent or cash withdrawal location and get real-time directions.",
    "Security and Fraud Detection": "Receive real-time alerts for suspicious transactions and manage card blocking or unblocking in case of theft or loss.",
    "Customer Support": "Assist with troubleshooting and FAQs (e.g., password resets, failed transactions). Escalate issues to human agents when necessary.",
    "Additional Features": "Introduce micro-investment options and manage subscription services linked to Easypaisa."
}

# Header for the chatbot
st.header("✨Service Chatbot")

# Dropdown menu for selecting a service
selected_option = st.sidebar.selectbox("Choose a service domain:", services.keys())

# Display the selected service description below the header
st.subheader(f"Selected Service: {selected_option}")
st.write(f"**Description:** {services[selected_option]}")

# Function to get response from Gemini API
def get_gemini_response(question, context):
    model = genai.GenerativeModel("gemini-pro")
    dynamic_prompt = f"""
    You are a chatbot specializing in Easypaisa, Pakistan's digital banking app. 
    Focus exclusively on the selected service: {context}. 
    Provide concise and realistic answers strictly related to this service. 
    If the user's query pertains to a different service or is outside Easypaisa's offerings, politely inform them that it's beyond your scope.

    Description: {services[context]}

    User query: {question}
    """
    response = model.generate_content(dynamic_prompt)
    return response.text

# Display previous chat messages
for message in st.session_state["messages"]:
    role = message["role"]
    content = message["content"]
    with st.chat_message(role):
        st.markdown(content)

# Chat input box
prompt = st.chat_input("Ask about the selected service:")

# Handle user input and generate a response
if prompt:
    # Add user message to the session state
    st.session_state["messages"].append({"role": "user", "content": prompt})

    # Get response from Gemini API
    response = get_gemini_response(prompt, selected_option)

    # Add assistant message to the session state
    st.session_state["messages"].append({"role": "assistant", "content": response})

    # Display user and assistant messages using st.chat_message
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        st.markdown(response)
