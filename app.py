import streamlit as st
import google.generativeai as genai

st.title("📚 آسان اردو بوٹ")

# سائیڈ بار میں API Key
api_key = st.sidebar.text_input("Gemini API Key:", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        user_text = st.text_area("یہاں وہ لکھیں جو سمجھ نہیں آ رہا:")

        if st.button("اردو میں سمجھاؤ"):
            if user_text:
                response = model.generate_content(f"Explain this in simple Urdu with examples: {user_text}")
                st.write(response.text)
            else:
                st.warning("کچھ لکھیں تو سہی!")
    except Exception as e:
        st.error(f"ایرر: {e}")
else:
    st.info("بائیں طرف API Key ڈالیں۔")
    
