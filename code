import streamlit as st
import random

st.set_page_config(page_title="Bé Giỏi Toán", page_icon="🎈", layout="centered")
st.title("🎈 BÉ GIỎI TOÁN CẤP 1 🎈")

# Chọn phân loại lớp học
grade = st.selectbox(
    "Chọn lớp học của bé:",
    ["Lớp 1 (Cộng/Trừ dưới 10)", "Lớp 2-3 (Cộng/Trừ/Nhân dưới 100)", "Lớp 4-5 (Phép tính tổng hợp)"]
)

# Khởi tạo điểm số và sao thưởng
if "score" not in st.session_state: st.session_state.score = 0
if "stars" not in st.session_state: st.session_state.stars = 0

def generate_question(grade_choice):
    if "Lớp 1" in grade_choice:
        n1 = random.randint(1, 9)
        n2 = random.randint(1, 10 - n1)
        op = random.choice(["+", "-"])
        if op == "-" and n1 < n2: n1, n2 = n2, n1
    elif "Lớp 2-3" in grade_choice:
        op = random.choice(["+", "-", "*"])
        if op == "*": n1, n2 = random.randint(2, 9), random.randint(2, 9)
        else:
            n1, n2 = random.randint(10, 99), random.randint(10, 99)
            if op == "-" and n1 < n2: n1, n2 = n2, n1
    else:
        op = random.choice(["+", "-", "*", "/"])
        if op == "/":
            n2 = random.randint(2, 9)
            ans = random.randint(2, 10)
            n1 = n2 * ans
        elif op == "*": n1, n2 = random.randint(5, 15), random.randint(2, 10)
        else:
            n1, n2 = random.randint(20, 200), random.randint(20, 200)
            if op == "-" and n1 < n2: n1, n2 = n2, n1
    return n1, n2, op

if "q_num1" not in st.session_state:
    st.session_state.q_num1, st.session_state.q_num2, st.session_state.q_op = generate_question(grade)

def next_question():
    st.session_state.q_num1, st.session_state.q_num2, st.session_state.q_op = generate_question(grade)

def check_answer():
    ans = st.session_state.ans_input
    n1, n2, op = st.session_state.q_num1, st.session_state.q_num2, st.session_state.q_op
    
    correct = n1 + n2 if op == "+" else n1 - n2 if op == "-" else n1 * n2 if op == "*" else n1 // n2
    
    if ans == correct:
        st.session_state.score += 10
        st.session_state.stars += 1
        st.toast("🎉 Giỏi lắm! +10 điểm và 1 ⭐!", icon="🌟")
        st.balloons()
    else:
        st.toast(f"😅 Chưa đúng! Đáp án là {correct}", icon="💡")
    next_question()

col1, col2 = st.columns(2)
with col1: st.metric("🏆 Điểm số", f"{st.session_state.score} điểm")
with col2: st.metric("⭐ Sao thưởng", f"{st.session_state.stars} ⭐")
st.divider()

n1, n2, op = st.session_state.q_num1, st.session_state.q_num2, st.session_state.q_op
op_symbol = " + " if op == "+" else " - " if op == "-" else " × " if op == "*" else " ÷ "
st.subheader(f"❓ Câu hỏi: {n1} {op_symbol} {n2} = ?")

if "Lớp 1" in grade and op in ["+", "-"]:
    st.write("**Minh họa cho bé:**")
    if op == "+": st.write("🍎 " * n1 + "  ➕  " + "🍎 " * n2)
    elif op == "-": st.write("🎈 " * n1 + f"  *(bớt {n2} bóng)*")

st.number_input("Nhập đáp án rồi bấm Enter:", key="ans_input", step=1, value=None, on_change=check_answer)
if st.button("🔄 Đổi câu hỏi"):
    next_question()
    st.rerun()
