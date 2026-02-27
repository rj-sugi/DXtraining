import random
import datetime
import streamlit as st

# --- ページ設定 ---
st.set_page_config(
    page_title="Fortune App",
    page_icon="🔮",
    layout="centered",
)

# --- データ ---
FORTUNES = [
    ("大吉", "今日は最高の流れ。小さく始めたことが大きく育ちます。"),
    ("中吉", "良い兆し。無理せず淡々と進めるほど成果が出ます。"),
    ("小吉", "安定の日。整理整頓や準備がツキを呼びます。"),
    ("吉",   "まずまず。丁寧なコミュニケーションが鍵です。"),
    ("末吉", "後半に良いことがありそう。焦らないでOK。"),
    ("凶",   "慎重に。大事な判断は一晩おいてから。"),
]

# --- セッション初期化 ---
if "fortune" not in st.session_state:
    st.session_state.fortune = ("—", "ボタンを押して占ってみよう。")

# --- 見た目（中央配置＆カード） ---
st.markdown(
    """
    <style>
      .stApp {
        background: radial-gradient(1200px 800px at 20% 10%, #1b2a4a 0%, #0b1220 55%);
      }
      .center-wrap {
        min-height: calc(100vh - 120px);
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 24px 0;
      }
      .card {
        width: min(560px, 100%);
        padding: 22px 20px;
        border-radius: 20px;
        border: 1px solid rgba(255,255,255,0.12);
        background: linear-gradient(180deg, rgba(255,255,255,0.06), rgba(255,255,255,0.03));
        box-shadow: 0 20px 60px rgba(0,0,0,0.45);
        backdrop-filter: blur(10px);
      }
      .title {
        display: flex;
        align-items: center;
        gap: 10px;
        font-size: 20px;
        font-weight: 800;
        color: #e8eefc;
        margin: 0 0 6px;
      }
      .subtitle {
        margin: 0 0 14px;
        color: #a9b6d3;
        font-size: 14px;
        line-height: 1.6;
      }
      .result {
        margin: 14px 0 16px;
        padding: 14px 14px;
        border-radius: 14px;
        background: rgba(0,0,0,0.25);
        border: 1px solid rgba(255,255,255,0.10);
      }
      .label {
        color: #a9b6d3;
        font-size: 12px;
        letter-spacing: .08em;
        text-transform: uppercase;
      }
      .value {
        font-size: 22px;
        font-weight: 900;
        color: #e8eefc;
        margin-top: 2px;
      }
      .msg {
        margin: 10px 0 0;
        color: #e8eefc;
        line-height: 1.7;
      }
      /* ボタンを横並びにしやすく */
      div[data-testid="column"] > div {
        padding-top: 0;
      }
      /* ボタンを少し大きめに */
      .stButton > button {
        width: 100%;
        border-radius: 14px;
        padding: 10px 12px;
        font-weight: 700;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- UI ---
today = datetime.date.today().isoformat()
fortune, message = st.session_state.fortune

st.markdown('<div class="center-wrap"><div class="card">', unsafe_allow_html=True)
st.markdown('<div class="title">🔮 Fortune App</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">画面中央で操作できる、Streamlitのサンプルアプリです。</div>', unsafe_allow_html=True)

st.markdown(
    f"""
    <div class="result">
      <div class="label">DATE</div>
      <div class="value">📅 {today}</div>
      <div class="label" style="margin-top:10px;">FORTUNE</div>
      <div class="value">{fortune}</div>
      <div class="msg">💬 {message}</div>
    </div>
    """,
    unsafe_allow_html=True,
)

col1, col2 = st.columns(2)

with col1:
    if st.button("占う", use_container_width=True):
        st.session_state.fortune = random.choice(FORTUNES)
        st.rerun()

with col2:
    if st.button("リセット", use_container_width=True):
        st.session_state.fortune = ("—", "ボタンを押して占ってみよう。")
        st.rerun()

st.markdown(
    '<div class="subtitle">GitHub → Streamlit でそのままデプロイできます。</div>',
    unsafe_allow_html=True
)
st.markdown("</div></div>", unsafe_allow_html=True)
