import streamlit as st
import google.generativeai as genai

st.title("📚 آسان اردو بوٹ")

# سائیڈ بار میں API Key
api_key = st.sidebar.text_input("Gemini API Key ڈالیں:", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        
        # یہاں ہم نے ماڈل کا نام تبدیل کر کے 'gemini-pro' کر دیا ہے
        model = genai.GenerativeModel('gemini-pro')
        
        user_text = st.text_area("جو سمجھ نہیں آ رہا یہاں لکھیں:")

        if st.button("اردو میں سمجھاؤ"):
            if user_text:
                with st.spinner('جواب تیار کیا جا رہا ہے...'):
                    response = model.generate_content(f"Explain this in simple Urdu with examples: {user_text}")
                    st.write(response.text)
            else:
                st.warning("پہلے کچھ لکھیں تو سہی!")
    except Exception as e:
        st.error(f"تکنیکی مسئلہ: {e}")
else:
    st.info("براہ کرم بائیں طرف اپنی API Key ڈالیں۔")
    
