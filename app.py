
import streamlit as st
import random

st.set_page_config(
    page_title="Math Challenge",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 MATH CHALLENGE")
st.write("Chinh phục thử thách Toán học qua 3 cấp độ!")

# ==================================================
# NGÂN HÀNG CÂU HỎI
# Mỗi cấp độ có 15 câu; mỗi lượt lấy ngẫu nhiên 15 câu.
# Có thể bổ sung câu hỏi bằng cách thêm dictionary.
# ==================================================

QUESTIONS = {
    "Dễ": [
        {
            "q": "Giải phương trình 3x - 7 = 11.",
            "options": ["x = 4", "x = 5", "x = 6", "x = 7"],
            "answer": "x = 6",
            "explain": "3x = 18 nên x = 6."
        },
        {
            "q": "Tính √144 + √25.",
            "options": ["15", "17", "19", "21"],
            "answer": "17",
            "explain": "√144 = 12 và √25 = 5. Tổng bằng 17."
        },
        {
            "q": "Phân tích x² - 16 thành nhân tử.",
            "options": [
                "(x - 4)(x + 4)",
                "(x - 8)(x + 2)",
                "(x - 4)²",
                "(x + 16)(x - 1)"
            ],
            "answer": "(x - 4)(x + 4)",
            "explain": "Dùng a² - b² = (a - b)(a + b)."
        },
        {
            "q": "Nghiệm của x² = 81 là gì?",
            "options": ["x = 9", "x = -9", "x = ±9", "x = 81"],
            "answer": "x = ±9",
            "explain": "Cả 9² và (-9)² đều bằng 81."
        },
        {
            "q": "Tam giác có hai góc 45° và 65°. Góc còn lại là bao nhiêu?",
            "options": ["60°", "70°", "80°", "90°"],
            "answer": "70°",
            "explain": "180° - 45° - 65° = 70°."
        },
        {
            "q": "Giải phương trình 5x + 2 = 22.",
            "options": ["2", "3", "4", "5"],
            "answer": "4",
            "explain": "5x = 20 nên x = 4."
        },
        {
            "q": "Tính (a + b)².",
            "options": [
                "a² + b²",
                "a² + 2ab + b²",
                "a² - 2ab + b²",
                "a² - b²"
            ],
            "answer": "a² + 2ab + b²",
            "explain": "Đây là hằng đẳng thức bình phương một tổng."
        },
        {
            "q": "Giải phương trình x² - 9 = 0.",
            "options": ["x = 3", "x = -3", "x = ±3", "x = 9"],
            "answer": "x = ±3",
            "explain": "x² = 9 nên x = 3 hoặc x = -3."
        },
        {
            "q": "Tính 2³ × 2².",
            "options": ["16", "24", "32", "64"],
            "answer": "32",
            "explain": "2³ × 2² = 2⁵ = 32."
        },
        {
            "q": "Một tam giác vuông có hai cạnh góc vuông 6 và 8. Cạnh huyền bằng bao nhiêu?",
            "options": ["9", "10", "12", "14"],
            "answer": "10",
            "explain": "Theo Pythagore: c² = 6² + 8² = 100 nên c = 10."
        },
        {
            "q": "Rút gọn 3x + 2x - 7.",
            "options": ["5x - 7", "6x - 7", "5x + 7", "x - 7"],
            "answer": "5x - 7",
            "explain": "Cộng các hạng tử đồng dạng: 3x + 2x = 5x."
        },
        {
            "q": "Tìm x biết x/4 = 3.",
            "options": ["7", "12", "16", "1"],
            "answer": "12",
            "explain": "Nhân hai vế với 4 được x = 12."
        },
        {
            "q": "Phân tích x² + 6x + 9 thành nhân tử.",
            "options": [
                "(x + 3)²",
                "(x - 3)²",
                "(x + 9)(x + 1)",
                "x(x + 6)"
            ],
            "answer": "(x + 3)²",
            "explain": "x² + 6x + 9 = x² + 2·3·x + 3²."
        },
        {
            "q": "Nếu y = 2x + 1 và x = 3 thì y bằng bao nhiêu?",
            "options": ["5", "6", "7", "8"],
            "answer": "7",
            "explain": "Thay x = 3: y = 2·3 + 1 = 7."
        },
        {
            "q": "Tổng hai góc phụ nhau bằng bao nhiêu?",
            "options": ["45°", "90°", "180°", "360°"],
            "answer": "90°",
            "explain": "Hai góc phụ nhau có tổng số đo bằng 90°."
        }
    ],

    "Vừa": [
        {
            "q": "Giải phương trình x² - 5x + 6 = 0.",
            "options": [
                "x = 1 hoặc 6",
                "x = 2 hoặc 3",
                "x = -2 hoặc -3",
                "x = 0 hoặc 5"
            ],
            "answer": "x = 2 hoặc 3",
            "explain": "Phân tích thành (x - 2)(x - 3) = 0."
        },
        {
            "q": "Hai nghiệm của x² - 7x + 10 = 0 có tổng bằng bao nhiêu?",
            "options": ["5", "7", "10", "-7"],
            "answer": "7",
            "explain": "Theo Viète, tổng hai nghiệm bằng 7."
        },
        {
            "q": "Đường thẳng y = (m - 1)x + 2 song song với y = 3x - 4. Tìm m.",
            "options": ["2", "3", "4", "-2"],
            "answer": "4",
            "explain": "Hai đường thẳng song song có hệ số góc bằng nhau: m - 1 = 3."
        },
        {
            "q": "Giải hệ x + y = 7 và x - y = 1.",
            "options": [
                "(3; 4)", "(4; 3)", "(5; 2)", "(2; 5)"
            ],
            "answer": "(4; 3)",
            "explain": "Cộng hai phương trình: 2x = 8 nên x = 4, y = 3."
        },
        {
            "q": "Giải phương trình x² - 4x - 5 = 0.",
            "options": [
                "x = 5 hoặc -1",
                "x = 1 hoặc -5",
                "x = 4 hoặc -5",
                "x = 5 hoặc 1"
            ],
            "answer": "x = 5 hoặc -1",
            "explain": "(x - 5)(x + 1) = 0."
        },
        {
            "q": "Tìm đỉnh của parabol y = x² - 4x + 3.",
            "options": [
                "(2; -1)",
                "(-2; -1)",
                "(2; 1)",
                "(-2; 3)"
            ],
            "answer": "(2; -1)",
            "explain": "Viết y = (x - 2)² - 1 nên đỉnh là (2; -1)."
        },
        {
            "q": "Nếu x₁, x₂ là nghiệm của x² - 3x + 1 = 0, tính x₁² + x₂².",
            "options": ["7", "9", "5", "3"],
            "answer": "7",
            "explain": "x₁ + x₂ = 3, x₁x₂ = 1. Tổng bình phương = 3² - 2·1 = 7."
        },
        {
            "q": "Một đường tròn bán kính 5 có chu vi bằng bao nhiêu?",
            "options": ["5π", "10π", "20π", "25π"],
            "answer": "10π",
            "explain": "Chu vi C = 2πR = 10π."
        },
        {
            "q": "Giải bất phương trình 3x - 2 > 10.",
            "options": ["x > 4", "x < 4", "x > 3", "x < 3"],
            "answer": "x > 4",
            "explain": "3x > 12 nên x > 4."
        },
        {
            "q": "Cho sin A = 3/5 với A là góc nhọn. Tính cos A.",
            "options": ["4/5", "3/4", "5/4", "2/5"],
            "answer": "4/5",
            "explain": "Vì A nhọn, cos A = √(1 - sin²A) = 4/5."
        },
        {
            "q": "Phương trình x² + 2x + m = 0 có nghiệm kép khi m bằng bao nhiêu?",
            "options": ["-1", "0", "1", "2"],
            "answer": "1",
            "explain": "Δ = 4 - 4m = 0 nên m = 1."
        },
        {
            "q": "Tính (√5 + 1)(√5 - 1).",
            "options": ["2", "4", "5", "6"],
            "answer": "4",
            "explain": "Dùng hiệu hai bình phương: 5 - 1 = 4."
        },
        {
            "q": "Tìm nghiệm của phương trình 2x² - 8 = 0.",
            "options": ["x = ±2", "x = ±4", "x = 2", "x = -2"],
            "answer": "x = ±2",
            "explain": "x² = 4 nên x = ±2."
        },
        {
            "q": "Một hình chữ nhật có chu vi 30 cm, chiều dài 9 cm. Chiều rộng bằng bao nhiêu?",
            "options": ["5 cm", "6 cm", "7 cm", "12 cm"],
            "answer": "6 cm",
            "explain": "Dài + rộng = 15, vậy rộng = 15 - 9 = 6 cm."
        },
        {
            "q": "Tìm m để phương trình x² - 2x + m = 0 có hai nghiệm thực.",
            "options": ["m ≤ 1", "m ≥ 1", "m < 0", "Mọi m"],
            "answer": "m ≤ 1",
            "explain": "Δ = 4 - 4m ≥ 0 nên m ≤ 1."
        }
    ],

    "Khó": [
        {
            "q": "Tìm giá trị nhỏ nhất của A = x² + 4/x², với x ≠ 0.",
            "options": ["2", "4", "6", "8"],
            "answer": "4",
            "explain": "Theo AM-GM, x² + 4/x² ≥ 2√4 = 4. Dấu bằng khi x² = 2."
        },
        {
            "q": "Phương trình x² - 2mx + m + 2 = 0 có hai nghiệm thực phân biệt khi nào?",
            "options": [
                "m < -1 hoặc m > 2",
                "-1 < m < 2",
                "m ≤ -1 hoặc m ≥ 2",
                "Mọi m"
            ],
            "answer": "m < -1 hoặc m > 2",
            "explain": "Δ/4 = m² - m - 2 = (m - 2)(m + 1) > 0."
        },
        {
            "q": "Cho a + b + c = 0. Khi đó a³ + b³ + c³ bằng bao nhiêu?",
            "options": ["0", "abc", "3abc", "-3abc"],
            "answer": "3abc",
            "explain": "Dùng a³ + b³ + c³ - 3abc = (a+b+c)(a²+b²+c²-ab-bc-ca)."
        },
        {
            "q": "Phương trình x⁴ - 5x² + 4 = 0 có bao nhiêu nghiệm thực phân biệt?",
            "options": ["1", "2", "3", "4"],
            "answer": "4",
            "explain": "Đặt t = x². Ta có t² - 5t + 4 = 0, t = 1 hoặc 4. Suy ra x = ±1, ±2."
        },
        {
            "q": "Với x, y > 0 và xy = 1, giá trị nhỏ nhất của (x + 1)(y + 1) là bao nhiêu?",
            "options": ["2", "3", "4", "5"],
            "answer": "4",
            "explain": "P = xy + x + y + 1 = x + y + 2 ≥ 4, vì x + y ≥ 2."
        },
        {
            "q": "Tìm số nguyên dương nhỏ nhất n để n chia hết cho 12 và 18.",
            "options": ["24", "30", "36", "72"],
            "answer": "36",
            "explain": "BCNN(12, 18) = 36."
        },
        {
            "q": "Tìm giá trị nhỏ nhất của x² - 6x + 13.",
            "options": ["3", "4", "5", "6"],
            "answer": "4",
            "explain": "x² - 6x + 13 = (x - 3)² + 4 ≥ 4."
        },
        {
            "q": "Cho x + 1/x = 3, x ≠ 0. Tính x² + 1/x².",
            "options": ["5", "7", "9", "11"],
            "answer": "7",
            "explain": "Bình phương: x² + 2 + 1/x² = 9, suy ra kết quả bằng 7."
        },
        {
            "q": "Một tam giác có ba cạnh 13, 14, 15. Diện tích bằng bao nhiêu?",
            "options": ["72", "78", "84", "90"],
            "answer": "84",
            "explain": "Nửa chu vi bằng 21. Công thức Heron cho S = √(21·8·7·6) = 84."
        },
        {
            "q": "Tìm tất cả nghiệm thực của x² - 4x + 4 = 0.",
            "options": ["x = -2", "x = 2", "x = ±2", "x = 4"],
            "answer": "x = 2",
            "explain": "(x - 2)² = 0 nên nghiệm kép x = 2."
        },
        {
            "q": "Tìm giá trị nhỏ nhất của P = x + 9/x với x > 0.",
            "options": ["3", "6", "9", "12"],
            "answer": "6",
            "explain": "Theo AM-GM: x + 9/x ≥ 2√9 = 6, dấu bằng khi x = 3."
        },
        {
            "q": "Nếu x + y = 5 và xy = 3, tính x² + y².",
            "options": ["13", "19", "25", "31"],
            "answer": "19",
            "explain": "x² + y² = (x + y)² - 2xy = 25 - 6 = 19."
        },
        {
            "q": "Tìm m để phương trình x² - (m + 1)x + m = 0 có hai nghiệm bằng nhau.",
            "options": ["m = 0", "m = 1", "m = -1", "Không có m"],
            "answer": "m = 1",
            "explain": "Δ = (m+1)² - 4m = (m-1)². Nghiệm kép khi m = 1."
        },
        {
            "q": "Cho a, b > 0 và a + b = 10. Giá trị lớn nhất của ab là bao nhiêu?",
            "options": ["20", "25", "30", "50"],
            "answer": "25",
            "explain": "Theo (a-b)² ≥ 0, ta có ab ≤ (a+b)²/4 = 25."
        },
        {
            "q": "Có bao nhiêu cách chọn 2 học sinh từ 6 học sinh khác nhau?",
            "options": ["12", "15", "18", "30"],
            "answer": "15",
            "explain": "Số cách là C(6,2) = 6·5/2 = 15."
        }
    ]
}

# ==================================================
# TRẠNG THÁI
# ==================================================

if "game_level" not in st.session_state:
    st.session_state.game_level = "Dễ"

if "game_questions" not in st.session_state:
    st.session_state.game_questions = []

if "game_index" not in st.session_state:
    st.session_state.game_index = 0

if "game_score" not in st.session_state:
    st.session_state.game_score = 0

if "game_answered" not in st.session_state:
    st.session_state.game_answered = False

if "game_finished" not in st.session_state:
    st.session_state.game_finished = False

if "game_started" not in st.session_state:
    st.session_state.game_started = False


def start_game(level):
    pool = QUESTIONS[level]
    count = min(15, len(pool))

    st.session_state.game_level = level
    st.session_state.game_questions = random.sample(pool, count)
    st.session_state.game_index = 0
    st.session_state.game_score = 0
    st.session_state.game_answered = False
    st.session_state.game_finished = False
    st.session_state.game_started = True


# ==================================================
# CHỌN CẤP ĐỘ
# ==================================================

level = st.selectbox(
    "🎯 Chọn cấp độ",
    ["Dễ", "Vừa", "Khó"],
    key="level_picker"
)

if st.button("🚀 Bắt đầu / Đổi cấp độ"):
    start_game(level)
    st.rerun()

# ==================================================
# CHƠI GAME
# ==================================================

if st.session_state.game_started and not st.session_state.game_finished:
    questions = st.session_state.game_questions
    i = st.session_state.game_index
    question = questions[i]

    st.divider()
    st.subheader(f"Cấp độ {st.session_state.game_level}")
    st.progress((i + 1) / len(questions))
    st.write(f"### Câu {i + 1}/{len(questions)}")
    st.write(question["q"])

    # Xáo trộn lựa chọn một lần cho mỗi câu
    order_key = f"order_{st.session_state.game_level}_{i}"
    if order_key not in st.session_state:
        st.session_state[order_key] = random.sample(
            question["options"], len(question["options"])
        )

    choice = st.radio(
        "Chọn đáp án:",
        st.session_state[order_key],
        key=f"answer_{st.session_state.game_level}_{i}"
    )

    if not st.session_state.game_answered:
        if st.button("✅ Kiểm tra", key=f"check_{i}"):
            st.session_state.game_answered = True

            if choice == question["answer"]:
                st.session_state.game_score += 1

            st.rerun()

    else:
        if choice == question["answer"]:
            st.success("🎉 Chính xác!")
        else:
            st.error("❌ Chưa chính xác.")

        st.info(f"**Đáp án:** {question['answer']}")
        st.write(f"**Giải thích:** {question['explain']}")

        if i + 1 < len(questions):
            if st.button("➡️ Câu tiếp theo", key=f"next_{i}"):
                st.session_state.game_index += 1
                st.session_state.game_answered = False
                st.rerun()
        else:
            if st.button("🏆 Xem kết quả", key="finish"):
                st.session_state.game_finished = True
                st.rerun()

# ==================================================
# KẾT QUẢ
# ==================================================

if st.session_state.game_started and st.session_state.game_finished:
    score = st.session_state.game_score
    total = len(st.session_state.game_questions)

    st.divider()
    st.balloons()
    st.title("🏆 KẾT QUẢ")
    st.metric("Điểm số", f"{score}/{total}")

    if score == total:
        st.success("Xuất sắc! Bạn đã trả lời đúng toàn bộ câu hỏi.")
    elif score >= total * 0.7:
        st.success("Rất tốt! Tiếp tục luyện tập để nâng trình.")
    elif score >= total * 0.4:
        st.info("Khá ổn! Hãy xem lại lời giải những câu sai.")
    else:
        st.warning("Đừng nản! Xem lời giải rồi thử lại nhé.")

    if st.button("🔄 Chơi lại bộ câu hỏi mới"):
        start_game(st.session_state.game_level)
        st.rerun()
