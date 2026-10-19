            "options": ["72", "78", "84", "90"],
            "answer": "84",
            "explain": "Nửa chu vi p = 21. Theo Heron: S = √[21(21-13)(21-14)(21-15)] = √7056 = 84.",
        },
    ],
}

# =========================================================
# TRẠNG THÁI GAME
# =========================================================
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
if "last_correct" not in st.session_state:
    st.session_state.last_correct = False

# =========================================================
# TIÊU ĐỀ VÀ CHỌN CẤP ĐỘ
# =========================================================
st.title("🎮 GAME THỬ THÁCH TOÁN HỌC")
st.markdown("### Chọn đáp án đúng để tích lũy điểm số!")

levels = ["Dễ", "Vừa", "Khó"]
level = st.selectbox(
    "🎯 CHỌN CẤP ĐỘ",
    levels,
    index=levels.index(st.session_state.level),
)

if level != st.session_state.level:
    st.session_state.level = level
    st.session_state.questions = random.sample(
        QUESTIONS[level], min(5, len(QUESTIONS[level]))
    )
    st.session_state.index = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.finished = False
    st.session_state.last_correct = False
    st.rerun()

st.divider()

# =========================================================
# HIỂN THỊ CÂU HỎI
# =========================================================
if not st.session_state.finished:
    questions = st.session_state.questions
    index = st.session_state.index
    total_questions = len(questions)
    current_question = questions[index]

    st.progress((index + 1) / total_questions)
    st.markdown(f"### 📘 CÂU {index + 1}/{total_questions}")
    st.markdown(f"## {current_question['q']}")

    choice = st.radio(
        "👇 CHỌN ĐÁP ÁN CỦA BẠN:",
        current_question["options"],
        key=f"choice_{st.session_state.level}_{index}",
        disabled=st.session_state.answered,
    )

    if not st.session_state.answered:
        if st.button("✅ KIỂM TRA ĐÁP ÁN", use_container_width=True):
            is_correct = choice == current_question["answer"]
            st.session_state.answered = True
            st.session_state.last_correct = is_correct
            if is_correct:
                st.session_state.score += 1
            st.rerun()

    if st.session_state.answered:
        if st.session_state.last_correct:
            st.success("🎉 CHÍNH XÁC! Bạn được cộng 1 điểm.")
        else:
            st.error("❌ Chưa chính xác! Đừng nản chí, hãy xem lời giải nhé.")

        st.info(
            f"**ĐÁP ÁN ĐÚNG:** {current_question['answer']}\n\n"
            f"**GIẢI THÍCH:** {current_question['explain']}"
        )

        if index + 1 < total_questions:
            if st.button("➡️ CÂU TIẾP THEO", use_container_width=True):
                st.session_state.index += 1
                st.session_state.answered = False
                st.session_state.last_correct = False
                st.rerun()
        else:
            if st.button("🏆 XEM KẾT QUẢ", use_container_width=True):
                st.session_state.finished = True
                st.rerun()

# =========================================================
# MÀN HÌNH KẾT QUẢ
# =========================================================
else:
    total = len(st.session_state.questions)
    score = st.session_state.score

    st.balloons()
    st.title("🏆 KẾT QUẢ CỦA BẠN")
    st.metric("🎯 SỐ CÂU TRẢ LỜI ĐÚNG", f"{score}/{total}")
    st.markdown(f"### 📚 CẤP ĐỘ: {st.session_state.level}")

    if score == total:
        st.success("🌟 XUẤT SẮC! Bạn đã trả lời đúng tất cả câu hỏi!")
    elif score >= total * 0.6:
        st.info("👏 Làm tốt lắm! Hãy tiếp tục luyện tập nhé.")
    else:
        st.warning("💪 Bạn hãy xem lại lời giải rồi thử sức thêm lần nữa nhé.")

    if st.button("🔄 CHƠI LẠI", use_container_width=True):
        st.session_state.questions = random.sample(
            QUESTIONS[st.session_state.level],
            min(5, len(QUESTIONS[st.session_state.level])),
        )
        st.session_state.index = 0
        st.session_state.score = 0
        st.session_state.answered = False
        st.session_state.finished = False
        st.session_state.last_correct = False
        st.rerun()

st.divider()

# =========================================================
# TRÌNH PHÁT NHẠC NỀN
# Đặt các file nhạc cạnh app.py:
# nhac_nen.m4a, nhac1.m4a, nhac2.m4a, nhac3.m4a
# =========================================================
MUSIC_FILES = ["nhac_nen.m4a", "nhac1.m4a", "nhac2.m4a", "nhac3.m4a"]
playlist = []

for filename in MUSIC_FILES:
    file_path = BASE_DIR / filename
    if file_path.is_file():
        try:
            audio_base64 = base64.b64encode(file_path.read_bytes()).decode("utf-8")
            playlist.append(
                {
                    "name": filename,
                    "src": "data:audio/mp4;base64," + audio_base64,
                }
            )
        except OSError:
            st.warning(f"Không đọc được file nhạc: {filename}")

st.markdown("## 🎵 TRÌNH PHÁT NHẠC")
if playlist:
