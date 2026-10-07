import streamlit as st
import random

st.set_page_config(page_title="Game Giải Toán Cấp 2 - Khôi Khoa L", page_icon="📐", layout="centered")

st.title("📐 GAME GIẢI TOÁN CẤP 2 - KHÔI KHOA L 📐")
st.write("Thử thách tư duy với Căn bậc hai, Phương trình, Định lý Pythagoras và Lũy thừa!")

# Khởi tạo trạng thái game
if "score" not in st.session_state:
    st.session_state.score = 0
if "streak" not in st.session_state:
    st.session_state.streak = 0

def generate_cap2_question():
    q_type = random.choice(["can_bac_hai", "phuong_trinh", "pitago", "luy_thua"])
    
    if q_type == "can_bac_hai":
        # Tìm x biết sqrt(x + a) = b => x = b^2 - a
        b = random.randint(3, 12)
        a = random.randint(1, 20)
        ans = b**2 - a
        question_text = f"Tìm x biết:  √(x + {a}) = {b}"
        hint = f"Bình phương 2 vế ta được: x + {a} = {b}² = {b**2}  ➔  x = {b**2} - {a}"
        
    elif q_type == "phuong_trinh":
        # Phương trình bậc hai dạng x² - Sx + P = 0
        x1 = random.randint(2, 9)
        x2 = random.randint(2, 9)
        S = x1 + x2
        P = x1 * x2
        ans = max(x1, x2)
        question_text = f"Cho phương trình: x² - {S}x + {P} = 0. Tìm nghiệm LỚN NHẤT của x:"
        hint = f"Phân tích thành nhân tử: (x - {x1})(x - {x2}) = 0 ➔ Các nghiệm là {x1} và {x2}"
        
    elif q_type == "pitago":
        # Bộ ba số Pitago nguyên
        triples = [(3, 4, 5), (6, 8, 10), (5, 12, 13), (9, 12, 15), (8, 15, 17), (12, 16, 20)]
        a, b, c = random.choice(triples)
        ans = c
        question_text = f"Cho tam giác vuông có 2 cạnh góc vuông a = {a} cm, b = {b} cm. Tính độ dài cạnh huyền c (cm):"
        hint = f"Định lý Pitago: c² = a² + b² = {a}² + {b}² = {a**2 + b**2} ➔ c = √({a**2 + b**2})"
        
    else:  # Lũy thừa & giá trị biểu thức
        base = random.randint(2, 5)
        exp = random.randint(2, 4)
        add = random.randint(10, 50)
        ans = (base ** exp) + add
        question_text = f"Tính giá trị biểu thức: {base}^{exp} + {add}"
        hint = f"Tính lũy thừa trước: {base}^{exp} = {base**exp}, sau đó cộng với {add}"
        
    return question_text, ans, hint

# Khởi tạo câu hỏi đầu tiên
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

# Bảng điểm & Chuỗi thắng
col1, col2 = st.columns(2)
with col1:
    st.metric("🏆 Tổng điểm", f"{st.session_state.score} điểm")
with col2:
    st.metric("🔥 Chuỗi đúng liên tiếp", f"{st.session_state.streak}")

st.divider()

# Khối hiển thị câu hỏi
st.subheader("❓ " + st.session_state.q_text)

# Nút mở gợi ý
with st.expander("💡 Xem gợi ý cách giải"):
    st.write(st.session_state.hint)

# Ô nhập kết quả
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
