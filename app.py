import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()
api=os.getenv("API-KEY")

genai.configure(api_key=api)

model = genai.GenerativeModel("gemini-1.5-flash")

st.set_page_config(page_title="GITA AI", layout="centered")
st.title("GITA AI")
st.header("छत्रपति संभाजी महाराज की जय!")
st.write("Life Solutions from Mahabharata & Bhagavad Gita")

st.write("""
Enter your life problem, and this app will provide a solution inspired by the teachings and scenarios 
from the Mahabharata and Bhagavad Gita. 🙏
""")


problem = st.text_area("Describe your problem:", height=150)

if st.button("Get Solution"):
    if problem.strip():
        with st.spinner("Hare Krishna! 🙏 Let me find a solution for you..."):
  
            classification_prompt = f"""
            Classify the following input as 'related' or 'not related' to life problems, ethical dilemmas, 
            or philosophical advice that can be answered using the Mahabharata or Bhagavad Gita:

            Input: {problem}

            Respond only with 'related' or 'not related'.
            """
            try:
                classification_response = model.generate_content(classification_prompt)
                classification = classification_response.text.strip().lower()

                if classification == 'related':

                    solution_prompt = f"""
                    A person is facing the following problem in life:
                    {problem}

                    1. Find a similar situation from the Mahabharata or Bhagavad Gita that relates to this problem.
                    2. Describe the scenario in detail and explain how it was resolved.
                    3. Provide a meaningful solution based on the teachings of the Mahabharata or Bhagavad Gita.
                    4. Include a relevant quote from the Mahabharata or Bhagavad Gita that supports the solution.
                    5. Give everything in simple english
                    """

                    response = model.generate_content(solution_prompt)
                    solution = response.text

                    st.success("✅ Here's your solution:")
                    st.write(solution)

                else:
                    st.warning("⚠️ Not related to Mahabharata or Bhagavad Gita.")

            except Exception as e:
                st.error(f"❌ Error: {e}")

    else:
        st.warning("⚠️ Please describe your problem.")

st.markdown("---")
st.write("💡 *Inspired by the wisdom of ancient Indian scriptures!*")
