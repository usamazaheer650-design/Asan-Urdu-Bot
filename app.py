import streamlit as st
import google.generativeai as genai

st.title("📚 آسان اردو بوٹ")

# سائیڈ بار میں API Key
api_key = st.sidebar.text_input("Gemini API Key ڈالیں:", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        user_text = st.text_area("جو سمجھ نہیں آ رہا یہاں لکھیں:")

        if st.button("اردو میں سمجھاؤ"):
            if user_text:
                response = model.generate_content(f"Explain this in very simple Urdu with examples: {user_text}")
                st.write(response.text)
            else:
                st.warning("پہلے کچھ لکھیں تو سہی!")
    except Exception as e:
        st.error(f"ایرر آ گیا ہے: {e}")
else:
    st.info("براہ کرم بائیں طرف اپنی API Key ڈالیں۔")
    
