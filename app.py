import streamlit as st
import random
import base64

st.set_page_config(page_title="Game Giải Toán Cấp 2", page_icon="📐", layout="centered")

# --- NẠP HÌNH NỀN VÀ TỐI ƯU GIAO DIỆN CỰC DỄ ĐỌC ---
def load_media():
    # 1. Cấu hình hình nền OIP.jpg và khung chứa màu tối
    try:
        with open("OIP.jpg", "rb") as img_file:
            img_b64 = base64.b64encode(img_file.read()).decode()
            st.markdown(
                f"""
                <style>
                .stApp {{
                    background-image: url("data:image/jpeg;base64,{img_b64}");
                    background-size: cover;
                    background-position: center;
                    background-attachment: fixed;
                }}
                /* Tạo phông nền tối đục để chữ màu trắng nổi bật hoàn toàn */
                .stMainBlockContainer {{
                    background-color: rgba(15, 23, 42, 0.92) !important;
                    padding: 2.5rem !important;
                    border-radius: 20px !important;
                    margin-top: 2rem !important;
                    border: 2px solid rgba(255, 255, 255, 0.1);
                    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
                }}
                /* Ép toàn bộ chữ thường, tiêu đề, label sang màu trắng rõ nét */
                h1, h2, h3, p, span, label {{
                    color: #FFFFFF !important;
                }}
                /* Chỉnh màu cho câu hỏi nổi bật */
                .stSubheader h3 {{
                    color: #38BDF8 !important;
                    font-weight: 700;
                }}
                </style>
                """,
                unsafe_allow_html=True
            )
    except FileNotFoundError:
        pass

    # 2. Cấu hình nhạc nền xương rồng (intro).mp3
    try:
        with open("xương rồng (intro).mp3", "rb") as audio_file:
            audio_b64 = base64.b64encode(audio_file.read()).decode()
            audio_html = f"""
                <audio autoplay loop style="display:none;">
                    <source src="data:audio/mp3;base64,{audio_b64}" type="audio/mp3">
                </audio>
            """
            st.markdown(audio_html, unsafe_allow_html=True)
    except FileNotFoundError:
        pass

# Gọi hàm nạp giao diện
load_media()

# --- NỘI DUNG GAME GIẢI TOÁN CẤP 2 ---
st.title("📐 GAME GIẢI TOÁN CẤP 2 📐")
st.write("Thử thách tư duy với Căn bậc hai, Phương trình, Định lý Pythagoras và Lũy thừa!")

# Khởi tạo trạng thái game
if "score" not in st.session_state:
    st.session_state.score = 0
if "streak" not in st.session_state:
    st.session_state.streak = 0

def generate_cap2_question():
    q_type = random.choice(["can_bac_hai", "phuong_trinh", "pitago", "luy_thua"])
    
    if q_type == "can_bac_hai":
        b = random.randint(3, 12)
        a = random.randint(1, 20)
        ans = b**2 - a
        question_text = f"Tìm x biết: √(x + {a}) = {b}"
        hint = f"Bình phương 2 vế: x + {a} = {b}² = {b**2} ➔ x = {b**2} - {a}"
        
    elif q_type == "phuong_trinh":
        x1 = random.randint(2, 9)
        x2 = random.randint(2, 9)
        S = x1 + x2
        P = x1 * x2
        ans = max(x1, x2)
        question_text = f"Cho phương trình: x² - {S}x + {P} = 0. Tìm nghiệm LỚN NHẤT của x:"
        hint = f"Phân tích thành nhân tử: (x - {x1})(x - {x2}) = 0 ➔ Các nghiệm là {x1} và {x2}"
        
    elif q_type == "pitago":
        triples = [(3, 4, 5), (6, 8, 10), (5, 12, 13), (9, 12, 15), (8, 15, 17), (12, 16, 20)]
        a, b, c = random.choice(triples)
        ans = c
        question_text = f"Cho tam giác vuông có 2 cạnh góc vuông a = {a} cm, b = {b} cm. Tính cạnh huyền c (cm):"
        hint = f"Định lý Pitago: c² = a² + b² = {a}² + {b}² = {a**2 + b**2} ➔ c = √({a**2 + b**2})"
        
    else:
        base = random.randint(2, 5)
        exp = random.randint(2, 4)
        add = random.randint(10, 50)
        ans = (base ** exp) + add
        question_text = f"Tính giá trị biểu thức: {base}^{exp} + {add}"
        hint = f"Tính lũy thừa trước: {base}^{exp} = {base**exp}, sau đó cộng với {add}"
        
    return question_text, ans, hint

if "q_text" not in st.session_state:
    st.session_state.q_text, st.session_state.ans, st.session_state.hint = generate_cap2_question()

def next_question():
    st.session_state.q_text, st.session_state.ans, st.session_state.hint = generate_cap2_question()

def check_answer():
    user_ans = st.session_state.user_input
    correct = st.session_state.ans
    
    if user_ans == correct:
        st.session_state.score += 20
        st.session_state.streak += 1
        st.toast(f"🎉 Chính xác! +20 điểm (Chuỗi đúng: {st.session_state.streak})", icon="🔥")
        if st.session_state.streak % 3 == 0:
            st.balloons()
    else:
        st.session_state.streak = 0
        st.toast(f"❌ Chưa đúng! Đáp án chính xác là {correct}", icon="💡")
    
    next_question()

col1, col2 = st.columns(2)
with col1:
    st.metric("🏆 Tổng điểm", f"{st.session_state.score} điểm")
with col2:
    st.metric("🔥 Chuỗi đúng liên tiếp", f"{st.session_state.streak}")

st.divider()

st.subheader("❓ " + st.session_state.q_text)

with st.expander("💡 Xem gợi ý cách giải"):
    st.write(st.session_state.hint)

st.number_input(
    "Nhập kết quả (số nguyên) rồi ấn Enter:",
    key="user_input",
    step=1,
    value=None,
    on_change=check_answer
)

if st.button("🔄 Bỏ qua / Đổi câu hỏi khác"):
    next_question()
    st.rerun()
import base64
import streamlit as st
import random
import base64

st.set_page_config(page_title="Game Giải Toán Cấp 2", page_icon="📐", layout="centered")

# --- NẠP HÌNH NỀN VÀ NHẠC NỀN ---
def load_media():
    # 1. Cấu hình hình nền OIP.jpg
    try:
        with open("OIP.jpg", "rb") as img_file:
            img_b64 = base64.b64encode(img_file.read()).decode()
            st.markdown(
                f"""
                <style>
                .stApp {{
                    background-image: url("data:image/jpeg;base64,{img_b64}");
                    background-size: cover;
                    background-position: center;
                    background-attachment: fixed;
                }}
                .stMainBlockContainer {{
                    background-color: rgba(15, 23, 42, 0.92) !important;
                    padding: 2.5rem !important;
                    border-radius: 20px !important;
                    margin-top: 2rem !important;
                    border: 2px solid rgba(255, 255, 255, 0.1);
                    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
                }}
                h1, h2, h3, p, span, label {{
                    color: #FFFFFF !important;
                }}
                .stSubheader h3 {{
                    color: #38BDF8 !important;
                    font-weight: 700;
                }}
                </style>
                """,
                unsafe_allow_html=True
            )
    except FileNotFoundError:
        st.warning("⚠️ Không tìm thấy file hình nền 'OIP.jpg' trên GitHub.")

    # 2. Cấu hình nhạc nền nhac.mp3
    try:
        with open("nhac.mp3", "rb") as audio_file:
            audio_b64 = base64.b64encode(audio_file.read()).decode()
            audio_html = f"""
                <audio autoplay loop style="display:none;">
                    <source src="data:audio/mp3;base64,{audio_b64}" type="audio/mp3">
                </audio>
            """
            st.markdown(audio_html, unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning("⚠️ Không tìm thấy file 'nhac.mp3' trên GitHub. Hãy đổi tên file nhạc thành 'nhac.mp3'.")

load_media()

# --- NỘI DUNG GAME GIẢI TOÁN CẤP 2 ---
st.title("📐 GAME GIẢI TOÁN CẤP 2 📐")
st.write("Thử thách tư duy với Căn bậc hai, Phương trình, Định lý Pythagoras và Lũy thừa!")

# Khung phát nhạc dự phòng cho trình duyệt (nếu trình duyệt chặn autoplay)
with st.sidebar:
    st.write("🎵 **Bật/Tắt Nhạc Nền**")
    try:
        st.audio("nhac.mp3", loop=True)
    except:
        pass

# Khởi tạo trạng thái game
if "score" not in st.session_state:
    st.session_state.score = 0
if "streak" not in st.session_state:
    st.session_state.streak = 0

def generate_cap2_question():
    q_type = random.choice(["can_bac_hai", "phuong_trinh", "pitago", "luy_thua"])
    
    if q_type == "can_bac_hai":
        b = random.randint(3, 12)
        a = random.randint(1, 20)
        ans = b**2 - a
        question_text = f"Tìm x biết: √(x + {a}) = {b}"
        hint = f"Bình phương 2 vế: x + {a} = {b}² = {b**2} ➔ x = {b**2} - {a}"
        
    elif q_type == "phuong_trinh":
        x1 = random.randint(2, 9)
        x2 = random.randint(2, 9)
        S = x1 + x2
        P = x1 * x2
        ans = max(x1, x2)
        question_text = f"Cho phương trình: x² - {S}x + {P} = 0. Tìm nghiệm LỚN NHẤT của x:"
        hint = f"Phân tích thành nhân tử: (x - {x1})(x - {x2}) = 0 ➔ Các nghiệm là {x1} và {x2}"
        
    elif q_type == "pitago":
        triples = [(3, 4, 5), (6, 8, 10), (5, 12, 13), (9, 12, 15), (8, 15, 17), (12, 16, 20)]
        a, b, c = random.choice(triples)
        ans = c
        question_text = f"Cho tam giác vuông có 2 cạnh góc vuông a = {a} cm, b = {b} cm. Tính cạnh huyền c (cm):"
        hint = f"Định lý Pitago: c² = a² + b² = {a}² + {b}² = {a**2 + b**2} ➔ c = √({a**2 + b**2})"
        
    else:
        base = random.randint(2, 5)
        exp = random.randint(2, 4)
        add = random.randint(10, 50)
        ans = (base ** exp) + add
        question_text = f"Tính giá trị biểu thức: {base}^{exp} + {add}"
        hint = f"Tính lũy thừa trước: {base}^{exp} = {base**exp}, sau đó cộng với {add}"
        
    return question_text, ans, hint

if "q_text" not in st.session_state:
    st.session_state.q_text, st.session_state.ans, st.session_state.hint = generate_cap2_question()

def next_question():
    st.session_state.q_text, st.session_state.ans, st.session_state.hint = generate_cap2_question()

def check_answer():
    user_ans = st.session_state.user_input
    correct = st.session_state.ans
    
    if user_ans == correct:
        st.session_state.score += 20
        st.session_state.streak += 1
        st.toast(f"🎉 Chính xác! +20 điểm (Chuỗi đúng: {st.session_state.streak})", icon="🔥")
        if st.session_state.streak % 3 == 0:
            st.balloons()
    else:
        st.session_state.streak = 0
        st.toast(f"❌ Chưa đúng! Đáp án chính xác là {correct}", icon="💡")
    
    next_question()

col1, col2 = st.columns(2)
with col1:
    st.metric("🏆 Tổng điểm", f"{st.session_state.score} điểm")
with col2:
    st.metric("🔥 Chuỗi đúng liên tiếp", f"{st.session_state.streak}")

st.divider()

st.subheader("❓ " + st.session_state.q_text)

with st.expander("💡 Xem gợi ý cách giải"):
    st.write(st.session_state.hint)

st.number_input(
    "Nhập kết quả (số nguyên) rồi ấn Enter:",
    key="user_input",
    step=1,
    value=None,
    on_change=check_answer
)

if st.button("🔄 Bỏ qua / Đổi câu hỏi khác"):
    next_question()
    st.rerun()
