import streamlit as st
import google.generativeai as genai


genai.configure(api_key=st.secrets["gemini_apikey"])

model = genai.GenerativeModel("gemini-pro")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a dietician who will give a complete diet based on height weight age and activity and need and you will do this divided on breakfast luch dinner with portion sizes"}
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

max_messages = 20
if len(st.session_state.messages) >= max_messages:
    st.info("You've hit the 20-message limit. Want more? Deploy your own Gemini-powered chatbot!")
else:
    if prompt := st.chat_input("Say something in rhyme..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            message_placeholder = st.empty()

            history = [
                {"role": m["role"], "parts": [m["content"]]}
                for m in st.session_state.messages
                if m["role"] != "system"
            ]
            system_instruction = st.session_state.messages[0]["content"]

            response = model.generate_content(
                history + [{"role": "user", "parts": [prompt]}],
                generation_config={"temperature": 0.7},
                safety_settings={"HARASSMENT": "block_none"}
            )

            output = response.text.strip()
            message_placeholder.markdown(output)

            st.session_state.messages.append({"role": "assistant", "content": output})
