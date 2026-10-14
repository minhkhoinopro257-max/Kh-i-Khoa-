import streamlit as st
import random
import time

# ===== CSS LÀM CHỮ NỔI BẬT, DỄ ĐỌC =====
st.markdown("""
<style>

/* Nền và chữ toàn trang */
.stApp {
    color: #FFFFFF;
}

/* Tiêu đề nổi bật */
h1, h2, h3 {
    color: #FFFFFF !important;
    font-weight: 900 !important;
    text-shadow:
        2px 2px 4px #000000,
        0 0 10px rgba(0, 0, 0, 0.9) !important;
}

/* Chữ nội dung */
.stMarkdown p,
.stMarkdown li,
.stCaption {
    color: #FFFFFF !important;
    font-weight: 600 !important;
    text-shadow: 1px 1px 4px #000000;
}

/* Nhãn và câu hỏi */
[data-testid="stWidgetLabel"],
[data-testid="stWidgetLabel"] p {
    color: #FFFFFF !important;
    font-weight: 800 !important;
    text-shadow: 1px 1px 4px #000000 !important;
}

/* Đáp án trắc nghiệm */
[data-testid="stRadio"] label,
[data-testid="stRadio"] label p {
    color: #FFFFFF !important;
    font-weight: 700 !important;
    text-shadow: 1px 1px 3px #000000;
}

/* Khung chọn đáp án */
[data-testid="stRadio"] > div {
    background: rgba(10, 15, 30, 0.82);
    border: 1px solid rgba(96, 165, 250, 0.65);
    border-radius: 12px;
    padding: 12px 16px;
}

/* Ô chọn */
[data-testid="stSelectbox"] > div > div {
    background-color: #111827 !important;
    color: #FFFFFF !important;
    border: 1px solid #60A5FA !important;
    border-radius: 10px !important;
}

/* Nút bấm */
.stButton > button {
    background: linear-gradient(135deg, #2563EB, #7C3AED) !important;
    color: #FFFFFF !important;
    font-weight: 800 !important;
    border: 1px solid #93C5FD !important;
    border-radius: 12px !important;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5);
    transition: all 0.2s ease;
}

/* Hiệu ứng khi di chuột */
.stButton > button:hover {
    background: linear-gradient(135deg, #0891B2, #7C3AED) !important;
    border: 1px solid #FFFFFF !important;
    transform: translateY(-2px);
}

/* Thanh tiến trình */
[data-testid="stProgressBar"] > div > div > div {
    background: #38BDF8 !important;
}

/* Ô nhập văn bản */
.stTextInput input {
    background-color: rgba(15, 23, 42, 0.95) !important;
    color: #FFFFFF !important;
    border: 1px solid #60A5FA !important;
    border-radius: 10px !important;
}

/* Thông báo */
[data-testid="stAlert"] {
    background-color: rgba(15, 23, 42, 0.95) !important;
    color: #FFFFFF !important;
    border-radius: 12px !important;
}

/* Chữ trong sidebar */
[data-testid="stSidebar"] {
    background-color: rgba(10, 15, 30, 0.96);
}

[data-testid="stSidebar"] * {
    color: #FFFFFF;
}

/* Làm chữ dễ đọc hơn trên nền anime */
[data-testid="stAppViewContainer"] {
    color: #FFFFFF;
}

</style>
""", unsafe_allow_html=True)

# ===== CODE GAME CỦA BẠN ĐẶT TIẾP Ở DƯỚI =====
```

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
import base64
import streamlit as st

def set_background(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background:
                linear-gradient(
                    rgba(10, 18, 35, 0.72),
                    rgba(10, 18, 35, 0.82)
                ),
                url("data:image/jpeg;base64,{encoded}");

            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_background("OIP.jpg")

import streamlit as st
import streamlit.components.v1 as components
import base64
from pathlib import Path
import json

# ==========================================
# DANH SÁCH NHẠC NỀN
# ==========================================

BASE_DIR = Path(__file__).resolve().parent

MUSIC_FILES = [
    "nhac_nen.m4a",
    "nhac1.m4a",
    "nhac2.m4a",
    "nhac3.m4a",
]

playlist = []

for filename in MUSIC_FILES:
    file_path = BASE_DIR / filename

    if file_path.is_file():
        try:
            with open(file_path, "rb") as f:
                audio_base64 = base64.b64encode(
                    f.read()
                ).decode("utf-8")

            playlist.append({
                "name": filename,
                "src": "data:audio/mp4;base64," + audio_base64
            })
        except OSError:
            st.warning(f"Không đọc được file: {filename}")
    else:
        st.warning(f"Không tìm thấy file nhạc: {filename}")

# ==========================================
# GIAO DIỆN NHẠC NỀN
# ==========================================

if playlist:
    playlist_json = json.dumps(playlist, ensure_ascii=False)

    components.html(
        f"""
        <div style="
            box-sizing: border-box;
            padding: 22px;
            background: #101827;
            color: #ffffff;
            border: 2px solid #60a5fa;
            border-radius: 18px;
            font-family: Arial, sans-serif;
            width: 100%;
        ">
            <h2 style="
                margin: 0 0 18px;
                color: #ffffff;
                font-size: 25px;
                font-weight: 900;
            ">
                🎵 MUSIC PLAYER
            </h2>

            <div id="trackName" style="
                padding: 15px;
                margin-bottom: 16px;
                background: #263449;
                border: 1px solid #64748b;
                border-radius: 12px;
                color: #ffffff;
                font-size: 16px;
                font-weight: bold;
                overflow-wrap: anywhere;
            ">
                Đang tải nhạc...
            </div>

            <audio id="music"
                controls
                preload="metadata"
                style="
                    width: 100%;
                    height: 48px;
                    display: block;
                    margin-bottom: 18px;
                ">
            </audio>

            <div style="
                display: flex;
                gap: 12px;
            ">
                <button id="prevBtn" style="
                    flex: 1;
                    padding: 15px 5px;
                    background: #1d4ed8;
                    color: white;
                    border: 2px solid #93c5fd;
                    border-radius: 12px;
                    font-size: 14px;
                    font-weight: 900;
                    cursor: pointer;
                ">
                    ⏮ BÀI TRƯỚC
                </button>

                <button id="nextBtn" style="
                    flex: 1;
                    padding: 15px 5px;
                    background: #15803d;
                    color: white;
                    border: 2px solid #86efac;
                    border-radius: 12px;
                    font-size: 14px;
                    font-weight: 900;
                    cursor: pointer;
                ">
                    BÀI TIẾP ⏭
                </button>
            </div>

            <p style="
                margin: 16px 0 0;
                color: #e5e7eb;
                font-size: 14px;
                line-height: 1.6;
            ">
                🔁 Danh sách nhạc tự động lặp lại.
                Nhấn Play để bắt đầu phát nhạc.
            </p>
        </div>

        <script>
            const playlist = {playlist_json};
            const audio = document.getElementById("music");
            const trackName = document.getElementById("trackName");

            let currentTrack = 0;

            function loadTrack(index, autoplay = false) {{
                currentTrack =
                    (index + playlist.length) % playlist.length;

                audio.src = playlist[currentTrack].src;

                trackName.textContent =
                    "🎶 Bài " + (currentTrack + 1) +
                    "/" + playlist.length + ": " +
                    playlist[currentTrack].name;

                if (autoplay) {{
                    audio.play().catch(() => {{
                        trackName.textContent =
                            "▶ Hãy nhấn Play: " +
                            playlist[currentTrack].name;
                    }});
                }}
            }}

            document.getElementById("prevBtn")
                .addEventListener("click", () => {{
                    loadTrack(currentTrack - 1, true);
                }});

            document.getElementById("nextBtn")
                .addEventListener("click", () => {{
                    loadTrack(currentTrack + 1, true);
                }});

            audio.addEventListener("ended", () => {{
                loadTrack(currentTrack + 1, true);
            }});

            loadTrack(0);
        </script>
        """,
        height=340,
        scrolling=False
    )
else:
    st.error(
        "Không tìm thấy file nhạc. "
        "Hãy kiểm tra tên file và thư mục chứa app.py."
    )


