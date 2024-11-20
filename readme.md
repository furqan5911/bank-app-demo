## README for Service Chatbot Application

### Overview
This is a **Service Chatbot Application** built using **Streamlit** and the **Google Gemini AI API**. The chatbot specializes in answering queries related to Easypaisa, a digital banking app in Pakistan. Users can select specific service domains, ask questions, and receive concise, relevant responses from the chatbot. The app dynamically adjusts its responses based on the selected service.

---

### Features
1. **Dynamic Service Selection**: Users can choose from a list of Easypaisa services, and the chatbot tailors its responses accordingly.
2. **Service Descriptions**: Each service includes a brief description to guide users about its purpose.
3. **Interactive Chat Interface**: Users can interact with the chatbot using a conversational UI.
4. **Focus on Relevance**: The chatbot restricts answers to the selected service domain, ensuring clear and precise guidance.

---

### Prerequisites
Before running the application, ensure you have the following installed:
- **Python 3.8 or above**
- **Streamlit**: Install it using `pip install streamlit`.
- **Google Generative AI API**: Install the required package using `pip install google-generativeai`.
- An API key for accessing the **Gemini API**. Make sure the API key is set up properly for authentication.

---

### How to Run the Application
1. **Clone or Download the Code**:
   Save the provided Python file (`app.py`) to your local machine.

2. **Install Dependencies**:
   Run the following command to install the required libraries:
   ```bash
   pip install streamlit google-generativeai
   ```

3. **Run the Application**:
   Use the following command in the terminal or command prompt:
   ```bash
   streamlit run app.py
   ```

4. **Access the Web Interface**:
   After running the above command, Streamlit will provide a local URL (e.g., `http://localhost:8501`). Open this URL in your web browser.

---

### How to Use the Application
1. Select a service from the **sidebar dropdown menu** (e.g., "Easyload and Bill Payments", "Customer Support").
2. Read the **service description** displayed below the chatbot header for guidance.
3. Enter a query in the chat input box related to the selected service.
4. View the chatbot's response based on your input and the selected service.

---

### File Details
- **Purpose**: The file provides an interactive chatbot interface for Easypaisa users to inquire about specific services.
- **Core Libraries**:
  - `streamlit`: For creating the web interface.
  - `google-generativeai`: For interacting with the Gemini API to generate AI-powered responses.
- **Dynamic Prompting**: Each query is enriched with contextual information about the selected service to improve response accuracy.

---

### Notes
- **API Integration**: Ensure your Google Gemini API key is properly configured. If the API key isn't set up, the chatbot will not function.
- **Limitations**: The chatbot responds only within the context of Easypaisa's services. Queries outside this domain will prompt a polite "out of scope" message.

---

### Troubleshooting
- If you encounter an error like `ModuleNotFoundError`, ensure all required libraries are installed using `pip install`.
- If the chatbot responses seem off, verify the correctness of the API key and ensure the Gemini API is reachable.

---

