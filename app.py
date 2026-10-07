import streamlit as st
import random

st.set_page_config(page_title="Game Giải Toán Nhanh", page_icon="🧮")

st.title("🧮 Game Giải Toán Nhanh")
st.write("Hãy tính nhẩm và nhập kết quả chính xác để tích lũy điểm!")

# Khởi tạo trạng thái trò chơi
if "score" not in st.session_state:
    st.session_state.score = 0
if "num1" not in st.session_state:
    st.session_state.num1 = random.randint(1, 20)
    st.session_state.num2 = random.randint(1, 20)
    st.session_state.op = random.choice(["+", "-", "*"])

def next_question():
    st.session_state.num1 = random.randint(1, 20)
    st.session_state.num2 = random.randint(1, 20)
    st.session_state.op = random.choice(["+", "-", "*"])

def check_answer():
    user_ans = st.session_state.user_input
    num1, num2, op = st.session_state.num1, st.session_state.num2, st.session_state.op
    correct = eval(f"{num1} {op} {num2}")
    
    if user_ans == correct:
        st.session_state.score += 10
        st.toast("Chính xác! +10 điểm 🎉", icon="✅")
    else:
        st.toast(f"Chưa đúng! Đáp án đúng là {correct}", icon="❌")
    
    next_question()

# Hiển thị điểm số
st.metric(label="Điểm số hiện tại", value=st.session_state.score)

# Hiển thị phép toán
op_symbol = "×" if st.session_state.op == "*" else st.session_state.op
st.subheader(f"Tính: {st.session_state.num1} {op_symbol} {st.session_state.num2} = ?")

# Ô nhập kết quả
st.number_input(
    "Nhập đáp án của bạn và ấn Enter:", 
    key="user_input", 
    step=1, 
    value=None,
    on_change=check_answer
)

if st.button("Đổi câu hỏi khác"):
    next_question()
    st.rerun()
import base64

# Đọc file nhạc
audio_file = "xương rồng (intro).mp3"

try:
    with open(audio_file, "rb") as f:
        audio_bytes = f.read()
        audio_base64 = base64.b64encode(audio_bytes).decode()
        
        # Sử dụng HTML để nhúng nhạc, tự động phát và lặp lại
        audio_html = f"""
            <audio autoplay loop>
                <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
            </audio>
        """
        st.markdown(audio_html, unsafe_allow_html=True)
except FileNotFoundError:
    st.write("Không tìm thấy file nhạc nền.")
import streamlit as st
import base64

# Hàm để đặt hình nền
def set_bg_from_local(image_file):
    with open(image_file, "rb") as f:
        encoded_string = base64.b64encode(f.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded_string.decode()}");
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

# Gọi hàm và truyền tên file ảnh bạn đã tải lên GitHub (ví dụ: 'background.png')
# Đảm bảo file ảnh nằm cùng thư mục với file app.py
try:
    set_bg_from_local('background.png') # Thay 'background.png' bằng tên file thật của bạn
except FileNotFoundError:
    st.warning("Không tìm thấy file hình nền. Hãy đảm bảo bạn đã tải ảnh lên GitHub đúng thư mục.")

