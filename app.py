import streamlit as st
import google.generativeai as genai

# صفحے کی سیٹنگ اور اردو ڈیزائن (RTL Support)
st.set_page_config(page_title="Asan Urdu Bot", layout="centered")

# اردو کو دائیں طرف کرنے کے لیے CSS
st.markdown("""
    <style>
    .stTextArea textarea {
        direction: rtl;
        text-align: right;
    }
    .stMarkdown p, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        direction: rtl;
        text-align: right;
    }
    div[data-testid="stExpander"] p {
        direction: rtl;
        text-align: right;
    }
    </style>
    """, unsafe_allow_index=True)

st.title("📚 آسان اردو بوٹ")
st.subheader("مشکل باتوں کو سادہ مثالوں سے سمجھیں")

# سائیڈ بار میں API Key کا ڈبہ
api_key = st.sidebar.text_input("اپنی Gemini API Key یہاں ڈالیں:", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        # ہم یہاں 'gemini-1.5-flash' استعمال کر رہے ہیں جو سب سے زیادہ مستحکم ہے
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        user_text = st.text_area("وہ پیراگراف یا سوال یہاں لکھیں جو سمجھ نہیں آ رہا:", height=150)

        if st.button("اردو میں سمجھاؤ"):
            if user_text:
                with st.spinner('استاد جی سوچ رہے ہیں...'):
                    prompt = f"تم ایک ماہر استاد ہو۔ اس متن کو ایک عام انسان کے لیے بالکل سادہ اردو میں روزمرہ کی مثالوں کے ساتھ سمجھاؤ: {user_text}"
                    response = model.generate_content(prompt)
                    
                    st.markdown("---")
                    st.markdown("### 💡 آسان وضاحت:")
                    st.write(response.text)
            else:
                st.warning("براہ کرم پہلے کچھ تحریر تو لکھیں۔")
    except Exception as e:
        st.error(f"اوہ! ایک مسئلہ آ گیا ہے: {e}")
        st.info("مشورہ: اپنی API Key دوبارہ چیک کریں یا تھوڑی دیر بعد کوشش کریں۔")
else:
    st.info("براہ کرم بائیں طرف اپنی API Key درج کریں تاکہ بوٹ کام شروع کر سکے۔")
