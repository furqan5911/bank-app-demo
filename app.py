
import streamlit as st
import google.generativeai as genai

API_KEY = "AIzaSyD4fcsx2GHbl4WNWgPkoJLof7uxmDf66MY"
genai.configure(api_key=API_KEY)



# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Define the options for the dropdown menu with descriptions
services = {
    "Invite Friends": "Users can send referrals directly via the chatbot (SMS, WhatsApp, Email), track referral rewards, and see how many friends have successfully signed up.",
    "Easyload & Bill Payments": "Facilitates mobile top-ups and bill payments through the chatbot interface.",
    "Rewards Management": "Track and redeem loyalty points, cashback, or rewards. Suggest relevant promotions and offers.",
    "Utility Bill Payments": "Allows users to view and pay utility bills seamlessly through the chatbot.",
    "Savings and Goals": "Set savings goals (e.g., vacations, purchases) and automate small regular contributions.",
    "Debit Card Management": "Request new or replacement debit cards, activate cards, and manage queries.",
    "One-Stop Shop for All Services": "Provides a directory for all available Easypaisa services and quick access links.",
    "Ticket Booking": "Automate ticket booking for events or travel, with real-time updates and reminders.",
    "Retail Locator (Near Retailer)": "Find the nearest Easypaisa agent or cash withdrawal location using geo-based search.",
    "Security and Fraud Detection": "Receive real-time alerts for suspicious transactions and manage card blocking or unblocking.",
    "Customer Support": "Assist with FAQs, troubleshooting, and escalate issues to human agents if needed.",
    "Additional Features": "Introduce investment options, subscription management, and related services."
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
    Provide concise, realistic answers strictly related to this service. Include conversational flow where relevant.
    If the user's query pertains to a different service or is outside Easypaisa's offerings, politely inform them.

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

 
# # Configure Streamlit page
# st.set_page_config(page_title="💬 Service Chatbot")

# # Initialize session state for chat history
# if "messages" not in st.session_state:
#     st.session_state["messages"] = []

# # Define the options for the dropdown menu with descriptions
# services = {
#     "Invite Friends": "Users can send referrals directly via Easypaisa chatbot (SMS, WhatsApp, Email), track referral rewards, and see how many friends have successfully signed up.",
#     "Easyload and Bill Payments": "Facilitates mobile top-ups and bill payments through the chatbot interface. Users can view payment history and set reminders.",
#     "Rewards Management": "Track and redeem loyalty points, cashback, or rewards. Personalized offers are provided based on user behavior and transaction history.",
#     "Utility Bill Payments": "Allows users to view and pay utility bills seamlessly through the chatbot. Reminders for upcoming bills can be set.",
#     "Savings and Goals": "Set savings goals (e.g., vacations, purchases) and automate small regular contributions. Progress monitoring helps users track goal achievements.",
#     "Debit Card Management": "Request new or replacement debit cards, activate cards, and manage card-related queries through the chatbot.",
#     "One-Stop Shop for All Services": "Explore all available Easypaisa services via a directory. Access links to popular services like money transfers and ticket booking.",
#     "Gift Services": "Send and receive gifts via the chatbot. Personalized gift suggestions are offered based on user activity and special occasions.",
#     "Ticket Booking": "Enables users to book tickets for events or travel directly via the chatbot.",
#     "Retail Locator (Near Retailer)": "Find the nearest Easypaisa agent or cash withdrawal location and get real-time directions.",
#     "Security and Fraud Detection": "Receive real-time alerts for suspicious transactions and manage card blocking or unblocking in case of theft or loss.",
#     "Customer Support": "Assist with troubleshooting and FAQs (e.g., password resets, failed transactions). Escalate issues to human agents when necessary.",
#     "Additional Features": "Introduce micro-investment options and manage subscription services linked to Easypaisa."
# }

# # Header for the chatbot
# st.header("✨Service Chatbot")

# # Dropdown menu for selecting a service
# selected_option = st.sidebar.selectbox("Choose a service domain:", services.keys())

# # Display the selected service description below the header
# st.subheader(f"Selected Service: {selected_option}")
# st.write(f"**Description:** {services[selected_option]}")

# # Function to get response from Gemini API
# def get_gemini_response(question, context):
#     model = genai.GenerativeModel("gemini-pro")
#     dynamic_prompt = f"""
#     You are a chatbot specializing in Easypaisa, Pakistan's digital banking app. 
#     Focus exclusively on the selected service: {context}. 
#     Provide concise and realistic answers strictly related to this service. 
#     If the user's query pertains to a different service or is outside Easypaisa's offerings, politely inform them that it's beyond your scope.

#     Description: {services[context]}

#     User query: {question}
#     """
#     response = model.generate_content(dynamic_prompt)
#     return response.text

# # Display previous chat messages
# for message in st.session_state["messages"]:
#     role = message["role"]
#     content = message["content"]
#     with st.chat_message(role):
#         st.markdown(content)

# # Chat input box
# prompt = st.chat_input("Ask about the selected service:")

# # Handle user input and generate a response
# if prompt:
#     # Add user message to the session state
#     st.session_state["messages"].append({"role": "user", "content": prompt})

#     # Get response from Gemini API
#     response = get_gemini_response(prompt, selected_option)

#     # Add assistant message to the session state
#     st.session_state["messages"].append({"role": "assistant", "content": response})

#     # Display user and assistant messages using st.chat_message
#     with st.chat_message("user"):
#         st.markdown(prompt)
#     with st.chat_message("assistant"):
#         st.markdown(response)



