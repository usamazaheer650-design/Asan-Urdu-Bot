import streamlit as st
import google.generativeai as genai

# ٹائٹل اور ڈیزائن
st.set_page_config(page_title="Asan Urdu Bot")
st.title("📚 آسان اردو بوٹ")
st.subheader("مشکل کتابوں کو سادہ مثالوں سے سمجھیں")

# یوزر سے API Key لینا (سیکیورٹی کے لیے)
api_key = st.sidebar.text_input("اپنی Gemini API Key یہاں ڈالیں:", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')

    user_text = st.text_area("وہ پیراگراف یا سوال یہاں لکھیں جو سمجھ نہیں آ رہا:")

    if st.button("اردو میں سمجھاؤ"):
        if user_text:
            prompt = f"تم ایک ماہر اور ہمدرد استاد ہو۔ اس مشکل متن کو ایک 10 سال کے بچے کے لیے بالکل سادہ اردو میں روزمرہ کی مثالوں کے ساتھ سمجھاؤ: {user_text}"
            response = model.generate_content(prompt)
            st.markdown("### 💡 آسان وضاحت:")
            st.write(response.text)
        else:
            st.warning("براہ کرم پہلے کچھ تحریر لکھیں۔")
else:
    st.info("براہ کرم بائیں طرف (Sidebar) اپنی API Key درج کریں تاکہ بوٹ کام کر سکے۔")
  
