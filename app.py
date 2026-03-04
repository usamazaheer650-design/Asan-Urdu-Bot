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
    """, unsafe_allow_html=True)
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
