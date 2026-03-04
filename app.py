import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="آسان اردو بوٹ")
st.title("📚 آسان اردو بوٹ")

# سائیڈ بار
api_key = st.sidebar.text_input("Gemini API Key ڈالیں:", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        # یہاں ہم صرف ماڈل کا نام استعمال کریں گے
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        user_text = st.text_area("جو سمجھ نہیں آ رہا یہاں لکھیں:")

        if st.button("اردو میں سمجھاؤ"):
            if user_text:
                with st.spinner('جواب تیار ہو رہا ہے...'):
                    response = model.generate_content(f"Explain this in simple Urdu: {user_text}")
                    st.success("ترجمہ/وضاحت:")
                    st.write(response.text)
            else:
                st.warning("کچھ تو لکھیں!")
    except Exception as e:
        st.error(f"تکنیکی مسئلہ: {str(e)}")
else:
    st.info("براہ کرم بائیں طرف مینو میں اپنی API Key درج کریں۔")
