from dotenv import load_dotenv
import os

# .envファイルを読み込む
load_dotenv()

# APIキーを取得して表示
api_key = os.getenv("OPENAI_API_KEY")
print(f"読み込んだAPIキー：{api_key}")
import streamlit as st
from dotenv import load_dotenv
import os
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

# .envからAPIキーを読み込む
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# LLM初期化
chat = ChatOpenAI(openai_api_key=api_key, model_name="gpt-3.5-turbo")

# 専門家の設定（自由に変えてOK）
roles = {
    "医療の専門家": "あなたは信頼できる医療の専門家です。やさしく丁寧にアドバイスをしてください。",
    "キャリアの専門家": "あなたは経験豊富なキャリアコンサルタントです。親身な提案をしてください。"
}

# Streamlit UI
st.title("LLM専門家チャットアプリ")
st.write("下の入力欄に相談内容を入力し、専門家を選んで送信してください。")

# ラジオボタンで専門家選択
selected_role = st.radio("相談したい専門家を選んでください", list(roles.keys()))

# テキスト入力欄
user_input = st.text_input("相談内容を入力してください")

# LLMへ質問する関数
def ask_llm(role, text):
    messages = [
        SystemMessage(content=roles[role]),
        HumanMessage(content=text)
    ]
    response = chat(messages)
    return response.content

# 実行ボタン
if st.button("送信"):
    if user_input:
        result = ask_llm(selected_role, user_input)
        st.success("AIの回答:")
        st.write(result)
    else:
        st.error("相談内容を入力してください。")
