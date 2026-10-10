
import random
import streamlit as st

st.set_page_config(
    page_title="Math Challenge",
    page_icon="🧮",
    layout="centered"
)

# ==================== GIAO DIỆN ====================

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #101827, #182b46);
    color: white;
}
h1, h2, h3, p, label {
    color: white !important;
}
div.stButton > button {
    width: 100%;
    border-radius: 12px;
    min-height: 45px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

st.title("🧮 MATH CHALLENGE")
st.write("Thử sức với những câu hỏi toán học!")

st.divider()

# ==================== CẤU HÌNH ====================

LEVELS = {
    "🟢 Dễ": {
        "min": 1,
        "max": 20,
        "operations": ["+", "-"]
    },
    "🟡 Vừa": {
        "min": 1,
        "max": 100,
        "operations": ["+", "-", "*", "/"]
    },
    "🔴 Khó": {
        "min": 10,
        "max": 500,
        "operations": ["+", "-", "*", "/"]
    }
}

TOTAL_QUESTIONS = 10


def create_question(level):
    settings = LEVELS[level]
    low = settings["min"]
    high = settings["max"]
    operation = random.choice(settings["operations"])

    if operation == "+":
        a = random.randint(low, high)
        b = random.randint(low, high)
        return f"{a} + {b}", a + b

    elif operation == "-":
        a = random.randint(low, high)
        b = random.randint(low, high)
        if a < b:
            a, b = b, a
        return f"{a} - {b}", a - b

    elif operation == "*":
        if level == "🔴 Khó":
            a = random.randint(10, 50)
            b = random.randint(10, 30)
        else:
            a = random.randint(2, high)
            b = random.randint(2, 12)
        return f"{a} × {b}", a * b

    else:
        # Tạo phép chia có kết quả nguyên
        b = random.randint(2, 12 if level == "🟡 Vừa" else 30)
        answer = random.randint(2, high)
        a = b * answer
        return f"{a} ÷ {b}", answer


def start_game(level):
    st.session_state.level = level
    st.session_state.questions = [
        create_question(level)
        for _ in range(TOTAL_QUESTIONS)
    ]
    st.session_state.index = 0
    st.session_state.score = 0
    st.session_state.started = True
    st.session_state.finished = False
    st.session_state.feedback = None


# ==================== KHỞI TẠO ====================

if "started" not in st.session_state:
    st.session_state.started = False

if "finished" not in st.session_state:
    st.session_state.finished = False

if "feedback" not in st.session_state:
    st.session_state.feedback = None

# ==================== CHỌN CẤP ĐỘ ====================

if not st.session_state.started:
    st.subheader("🎯 Chọn cấp độ")

    level = st.radio(
        "Bạn muốn chơi ở mức nào?",
        list(LEVELS.keys()),
        index=0
    )

    st.markdown("""
    - 🟢 **Dễ:** Cộng và trừ số nhỏ.
    - 🟡 **Vừa:** Cộng, trừ, nhân và chia.
    - 🔴 **Khó:** Số lớn và phép tính thử thách hơn.
    """)

    st.info("Mỗi lượt có 10 câu hỏi. Mỗi câu đúng được 10 điểm.")

    if st.button("🚀 BẮT ĐẦU CHƠI", type="primary"):
        start_game(level)
        st.rerun()

# ==================== ĐANG CHƠI ====================

elif not st.session_state.finished:
    index = st.session_state.index
    questions = st.session_state.questions
    score = st.session_state.score

    st.subheader(st.session_state.level)

    st.progress(index / TOTAL_QUESTIONS)

    st.write(
        f"**Câu {index + 1}/{TOTAL_QUESTIONS}**"
    )
    st.write(f"🏆 Điểm hiện tại: **{score}**")

    # Hiển thị phản hồi câu trước
    if st.session_state.feedback is not None:
        correct, correct_answer = st.session_state.feedback

        if correct:
            st.success("🎉 Chính xác! Bạn làm tốt lắm!")
        else:
            st.error(
                f"❌ Chưa đúng! Đáp án là {correct_answer}."
            )

    expression, answer = questions[index]

    st.markdown(
        f"<h1 style='text-align:center;'>{expression} = ?</h1>",
        unsafe_allow_html=True
    )

    with st.form(key=f"form_{index}"):
        user_answer = st.number_input(
            "Nhập đáp án của bạn:",
            step=1,
            value=0
        )

        submitted = st.form_submit_button(
            "✅ KIỂM TRA ĐÁP ÁN",
            type="primary"
        )

    if submitted:
        correct = int(user_answer) == answer

        if correct:
            st.session_state.score += 10

        st.session_state.feedback = (correct, answer)
        st.session_state.index += 1

        if st.session_state.index >= TOTAL_QUESTIONS:
            st.session_state.finished = True

        st.rerun()

# ==================== KẾT QUẢ ====================

else:
    score = st.session_state.score
    level = st.session_state.level

    st.balloons()
    st.header("🎉 HOÀN THÀNH!")

    st.metric("Tổng điểm", f"{score}/100")

    if score == 100:
        st.success("Xuất sắc! Bạn đã trả lời đúng tất cả!")
    elif score >= 70:
        st.success("Rất tốt! Hãy tiếp tục phát huy!")
    elif score >= 40:
        st.info("Khá tốt! Luyện tập thêm để đạt điểm cao hơn.")
    else:
        st.warning("Đừng nản chí! Thử lại để tiến bộ hơn nhé.")

    st.write(f"📚 Cấp độ: **{level}**")
    st.write(
        f"✅ Số câu đúng: **{score // 10}/{TOTAL_QUESTIONS}**"
    )

    if st.button("🔄 CHƠI LẠI", type="primary"):
        st.session_state.started = False
        st.session_state.finished = False
        st.session_state.feedback = None
        st.rerun()
