import streamlit as st
import random

st.set_page_config(
    page_title="Math Challenge",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 MATH CHALLENGE")
st.subheader("Thử thách Toán học")
st.write("Chọn cấp độ và chinh phục các câu hỏi!")

# =========================
# NGÂN HÀNG CÂU HỎI
# =========================

QUESTIONS = {
    "Dễ": [
        {
            "q": "Giải phương trình: 3x - 7 = 11.",
            "options": ["4", "5", "6", "7"],
            "answer": "6",
            "explain": "3x = 18 nên x = 6."
        },
        {
            "q": "Tính: √144 + √25.",
            "options": ["15", "17", "19", "21"],
            "answer": "17",
            "explain": "√144 = 12, √25 = 5. Tổng bằng 17."
        },
        {
            "q": "Phân tích x² - 9 thành nhân tử.",
            "options": [
                "(x - 3)(x + 3)",
                "(x - 9)(x + 1)",
                "(x - 3)²",
                "(x + 9)(x - 1)"
            ],
            "answer": "(x - 3)(x + 3)",
            "explain": "Dùng hằng đẳng thức a² - b² = (a - b)(a + b)."
        },
        {
            "q": "Nghiệm của phương trình x² = 49 là gì?",
            "options": ["7", "-7", "±7", "49"],
            "answer": "±7",
            "explain": "x² = 49 nên x = 7 hoặc x = -7."
        },
        {
            "q": "Một tam giác có hai góc 50° và 60°. Góc còn lại bằng bao nhiêu?",
            "options": ["60°", "70°", "80°", "90°"],
            "answer": "70°",
            "explain": "Tổng ba góc trong tam giác bằng 180°."
        }
    ],

    "Vừa": [
        {
            "q": "Giải phương trình: x² - 5x + 6 = 0.",
            "options": [
                "x = 1 hoặc 6",
                "x = 2 hoặc 3",
                "x = -2 hoặc -3",
                "x = 0 hoặc 5"
            ],
            "answer": "x = 2 hoặc 3",
            "explain": "Ta có x² - 5x + 6 = (x - 2)(x - 3) = 0."
        },
        {
            "q": "Hai nghiệm của x² - 7x + 10 = 0 có tổng bằng bao nhiêu?",
            "options": ["5", "7", "10", "-7"],
            "answer": "7",
            "explain": "Theo Viète, tổng hai nghiệm bằng -b/a = 7."
        },
        {
            "q": "Tìm m để đường thẳng y = (m - 1)x + 2 song song với y = 3x - 4.",
            "options": ["m = 2", "m = 3", "m = 4", "m = -2"],
            "answer": "m = 4",
            "explain": "Hai đường thẳng song song có hệ số góc bằng nhau: m - 1 = 3."
        },
        {
            "q": "Giải hệ: x + y = 7 và x - y = 1.",
            "options": [
                "(x, y) = (3, 4)",
                "(x, y) = (4, 3)",
                "(x, y) = (5, 2)",
                "(x, y) = (2, 5)"
            ],
            "answer": "(x, y) = (4, 3)",
            "explain": "Cộng hai phương trình được 2x = 8, suy ra x = 4, y = 3."
        },
        {
            "q": "Một tam giác vuông có hai cạnh góc vuông dài 6 và 8. Cạnh huyền bằng bao nhiêu?",
            "options": ["9", "10", "12", "14"],
            "answer": "10",
            "explain": "Theo định lý Pythagore: c² = 6² + 8² = 100 nên c = 10."
        }
    ],

    "Khó": [
        {
            "q": "Tìm giá trị nhỏ nhất của A = x² + 4/x² với x ≠ 0.",
            "options": ["2", "4", "6", "8"],
            "answer": "4",
            "explain": "Theo AM-GM: x² + 4/x² ≥ 2√(x² · 4/x²) = 4. Dấu bằng xảy ra khi x² = 2."
        },
        {
            "q": "Phương trình x² - 2mx + m + 2 = 0 có hai nghiệm thực phân biệt khi nào?",
            "options": [
                "m < -1 hoặc m > 2",
                "-1 < m < 2",
                "m ≤ -1 hoặc m ≥ 2",
                "Mọi m ∈ ℝ"
            ],
            "answer": "m < -1 hoặc m > 2",
            "explain": "Δ' = m² - m - 2 = (m - 2)(m + 1). Hai nghiệm phân biệt khi Δ' > 0, tức m < -1 hoặc m > 2."
        },
        {
            "q": "Cho a + b + c = 0. Biểu thức a³ + b³ + c³ bằng gì?",
            "options": [
                "0 trong mọi trường hợp",
                "abc",
                "3abc",
                "-3abc"
            ],
            "answer": "3abc",
            "explain": "Dùng hằng đẳng thức a³ + b³ + c³ - 3abc = (a + b + c)(a² + b² + c² - ab - bc - ca). Vì a + b + c = 0 nên tổng lập phương bằng 3abc."
        },
        {
            "q": "Có bao nhiêu cặp số nguyên dương có thứ tự (x, y) thỏa mãn 1/x + 1/y = 1/6?",
            "options": ["6", "8", "9", "12"],
            "answer": "9",
            "explain": "Biến đổi được (x - 6)(y - 6) = 36. Vì x, y > 6, số cặp tương ứng với số cặp ước dương có thứ tự của 36. Có 9 cặp."
        },
        {
            "q": "Phương trình x⁴ - 5x² + 4 = 0 có bao nhiêu nghiệm thực phân biệt?",
            "options": ["1", "2", "3", "4"],
            "answer": "4",
            "explain": "Đặt t = x² ≥ 0. Ta có t² - 5t + 4 = 0, suy ra t = 1 hoặc 4. Do đó x = ±1 hoặc ±2, có 4 nghiệm."
        },
        {
            "q": "Với mọi số thực a, b, c thỏa mãn a + b + c = 0, mệnh đề nào luôn đúng?",
            "options": [
                "a² + b² + c² = 0",
                "a² + b² + c² = ab + bc + ca",
                "a² + b² + c² = -2(ab + bc + ca)",
                "ab + bc + ca luôn dương"
            ],
            "answer": "a² + b² + c² = -2(ab + bc + ca)",
            "explain": "Bình phương a + b + c = 0 được a² + b² + c² + 2(ab + bc + ca) = 0."
        },
        {
            "q": "Cho x, y > 0 và xy = 1. Giá trị nhỏ nhất của P = (x + 1)(y + 1) là bao nhiêu?",
            "options": ["2", "3", "4", "5"],
            "answer": "4",
            "explain": "P = xy + x + y + 1 = x + y + 2. Vì xy = 1 nên x + y ≥ 2. Do đó P ≥ 4, đạt được khi x = y = 1."
        },
        {
            "q": "Một tam giác có ba cạnh 13, 14, 15. Diện tích tam giác bằng bao nhiêu?",
            "options": ["72", "78", "84", "90"],
            "answer": "84",
            "explain": "Nửa chu vi p = 21. Theo công thức Heron: S = √[21(21-13)(21-14)(21-15)] = √(21·8·7·6) = 84."
        }
    ]
}

# =========================
# TRẠNG THÁI GAME
# =========================

if "level" not in st.session_state:
    st.session_state.level = "Dễ"

if "questions" not in st.session_state:
    st.session_state.questions = random.sample(QUESTIONS["Dễ"], 5)

if "index" not in st.session_state:
    st.session_state.index = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "answered" not in st.session_state:
    st.session_state.answered = False

if "finished" not in st.session_state:
    st.session_state.finished = False

# =========================
# CHỌN CẤP ĐỘ
# =========================

level = st.selectbox(
    "🎯 Chọn cấp độ",
    ["Dễ", "Vừa", "Khó"],
    index=["Dễ", "Vừa", "Khó"].index(st.session_state.level)
)

if level != st.session_state.level:
    st.session_state.level = level
    st.session_state.questions = random.sample(
        QUESTIONS[level],
        min(5, len(QUESTIONS[level]))
    )
    st.session_state.index = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.finished = False
    st.rerun()

# =========================
# HIỂN THỊ CÂU HỎI
# =========================

if not st.session_state.finished:
    questions = st.session_state.questions
    i = st.session_state.index

    st.progress(i / len(questions))
    st.write(f"**Câu {i + 1}/{len(questions)}**")
    st.write(questions[i]["q"])

    choice = st.radio(
        "Chọn đáp án:",
        questions[i]["options"],
        key=f"choice_{st.session_state.level}_{i}"
    )

    if st.button("Kiểm tra đáp án", disabled=st.session_state.answered):
        st.session_state.answered = True

        if choice == questions[i]["answer"]:
            st.session_state.score += 1
            st.success("🎉 Chính xác! +1 điểm")
        else:
            st.error("❌ Chưa đúng!")

        st.info(
            "**Đáp án:** " + questions[i]["answer"]
            + "\n\n**Giải thích:** " + questions[i]["explain"]
        )

    if st.session_state.answered:
        if i + 1 < len(questions):
            if st.button("Câu tiếp theo ➜"):
                st.session_state.index += 1
                st.session_state.answered = False
                st.rerun()
        else:
            if st.button("Xem kết quả 🏆"):
                st.session_state.finished = True
                st.rerun()

# =========================
# KẾT QUẢ
# =========================

else:
    total = len(st.session_state.questions)
    score = st.session_state.score

    st.balloons()
    st.title("🏆 KẾT QUẢ")
    st.metric("Số câu đúng", f"{score}/{total}")
    st.write(f"**Cấp độ:** {st.session_state.level}")

    if score == total:
        st.success("Xuất sắc! Bạn đã trả lời đúng tất cả câu hỏi.")
    elif score >= total * 0.6:
        st.info("Làm tốt lắm! Hãy tiếp tục luyện tập.")
    else:
        st.warning("Bạn nên xem lại lời giải và thử sức lần nữa.")

    if st.button("🔄 Chơi lại"):
        st.session_state.questions = random.sample(
            QUESTIONS[st.session_state.level],
            min(5, len(QUESTIONS[st.session_state.level]))
        )
        st.session_state.index = 0
        st.session_state.score = 0
        st.session_state.answered = False
        st.session_state.finished = False
        st.rerun()
