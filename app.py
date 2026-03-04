import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="آسان اردو بوٹ")
st.title("📚 آسان اردو بوٹ")

# سائیڈ بار میں API Key
api_key = st.sidebar.text_input("Gemini API Key ڈالیں:", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        
        # یہاں ہم نے 'models/' کا اضافہ کیا ہے
        model = genai.GenerativeModel('models/gemini-1.5-flash')
        
        user_text = st.text_area("جو سمجھ نہیں آ رہا یہاں لکھیں:")

        if st.button("اردو میں سمجھاؤ"):
            if user_text:
                with st.spinner('سوچ رہا ہوں...'): # موبائل پر لوڈنگ دکھانے کے لیے
                    response = model.generate_content(f"Explain this in simple Urdu with examples: {user_text}")
                    st.success("جواب:")
                    st.write(response.text)
            else:
                st.warning("پہلے کچھ لکھیں تو سہی!")
    except Exception as e:
        # ایرر کو واضح دکھانے کے لیے
        st.error(f"تکنیکی مسئلہ: {e}")
else:
    st.info("براہ کرم بائیں طرف (Sidebar) میں اپنی API Key ڈالیں۔")
