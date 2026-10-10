
import random
import streamlit as st

st.set_page_config(
    page_title="Math Challenge",
    page_icon="🧮",
    layout="centered"
)

st.title("🧮 MATH CHALLENGE")
st.write("Vượt qua thử thách toán học!")

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #101827, #1b3150);
}
div.stButton > button {
    width: 100%;
    border-radius: 12px;
    font-weight: bold;
    min-height: 45px;
}
</style>
""", unsafe_allow_html=True)

LEVELS = ["Dễ", "Vừa", "Khó"]


def tao_cau_hoi(level):
    # DỄ: Toán cơ bản
    if level == "Dễ":
        dang = random.choice(["+", "-", "*", "/"])

        if dang == "+":
            a, b = random.randint(10, 999), random.randint(10, 999)
            return f"{a} + {b} = ?", a + b

        if dang == "-":
            a, b = random.randint(10, 999), random.randint(1, 999)
            a, b = max(a, b), min(a, b)
            return f"{a} - {b} = ?", a - b

        if dang == "*":
            a, b = random.randint(2, 99), random.randint(2, 12)
            return f"{a} × {b} = ?", a * b

        b = random.randint(2, 12)
        kq = random.randint(2, 100)
        return f"{b * kq} ÷ {b} = ?", kq

    # VỪA: Đại số THCS
    if level == "Vừa":
        dang = random.choice(["pt", "luy_thua", "can", "phan_so", "bieuthuc"])

        if dang == "pt":
            x = random.randint(-20, 20)
            a = random.randint(2, 12)
            b = random.randint(-30, 30)
            return f"Giải {a}x + ({b}) = {a*x+b}. Tìm x", x

        if dang == "luy_thua":
            a = random.randint(2, 12)
            b = random.randint(2, 4)
            return f"Tính {a}^{b}", a**b

        if dang == "can":
            a = random.randint(2, 30)
            return f"Tính √{a*a}", a

        if dang == "phan_so":
            a, b = random.randint(1, 10), random.randint(2, 10)
            c, d = random.randint(1, 10), random.randint(2, 10)
            result = round(a / b + c / d, 2)
            return f"Tính {a}/{b} + {c}/{d} (làm tròn 2 chữ số)", result

        a = random.randint(2, 15)
        return f"Khai triển (x + {a})², hệ số của x là bao nhiêu?", 2*a

    # KHÓ: Toán nâng cao
    dang = random.choice(["he", "bac_hai", "hang_dang_thuc", "ham_so", "can_thuc"])

    if dang == "he":
        x, y = random.randint(-10, 10), random.randint(-10, 10)
        return f"Hệ x + y = {x+y}; x - y = {x-y}. Tìm x", x

    if dang == "bac_hai":
        r1, r2 = random.randint(-10, 10), random.randint(-10, 10)
        b, c = -(r1+r2), r1*r2
        return f"Tìm nghiệm lớn nhất của x² + ({b})x + ({c}) = 0", max(r1, r2)

    if dang == "hang_dang_thuc":
        a = random.randint(2, 20)
        return f"Tính ({a}+1)² - ({a}-1)²", 4*a

    if dang == "ham_so":
        a = random.randint(2, 20)
        return f"Cho y = 2x² - 3. Tính y khi x = {a}", 2*a*a-3

    a = random.randint(2, 20)
    return f"Rút gọn √({a*a} × 4)", 2*a


def bat_dau(level):
    st.session_state.level = level
    st.session_state.questions = [tao_cau_hoi(level) for _ in range(10)]
    st.session_state.index = 0
    st.session_state.score = 0
    st.session_state.game = True
    st.session_state.done = False
    st.session_state.answered = False
    st.session_state.feedback = None


if "game" not in st.session_state:
    st.session_state.game = False

if "done" not in st.session_state:
    st.session_state.done = False

if not st.session_state.game:
    st.subheader("🎯 Chọn độ khó")

    level = st.radio(
        "Mức độ",
        LEVELS,
        horizontal=True
    )

    if level == "Dễ":
        st.caption("Cộng, trừ, nhân, chia và tính toán cơ bản.")
    elif level == "Vừa":
        st.caption("Phương trình bậc nhất, lũy thừa, căn bậc hai, phân số.")
    else:
        st.caption("Hệ phương trình, phương trình bậc hai, hàm số và biểu thức nâng cao.")

    st.info("10 câu hỏi • Mỗi câu đúng được 10 điểm.")

    if st.button("🚀 BẮT ĐẦU", type="primary"):
        bat_dau(level)
        st.rerun()

elif not st.session_state.done:
    i = st.session_state.index
    cau, dap_an = st.session_state.questions[i]

    st.subheader(f"Độ khó: {st.session_state.level}")
    st.progress(i / 10)
    st.write(f"Câu {i+1}/10 | Điểm: {st.session_state.score}/100")
    st.markdown(f"## {cau}")

    if st.session_state.feedback is not None:
        if st.session_state.feedback[0]:
            st.success("Chính xác! +10 điểm")
        else:
            st.error(f"Sai rồi! Đáp án: {st.session_state.feedback[1]}")

    with st.form(f"form_{i}"):
        tra_loi = st.number_input("Nhập đáp án:", value=0.0, step=1.0)
        gui = st.form_submit_button("Kiểm tra", type="primary")

    if gui:
        dung = abs(float(tra_loi) - float(dap_an)) < 0.011

        if dung:
            st.session_state.score += 10

        st.session_state.feedback = (dung, dap_an)
        st.session_state.index += 1

        if st.session_state.index >= 10:
            st.session_state.done = True

        st.rerun()

else:
    st.balloons()
    st.header("🏆 KẾT QUẢ")
    st.metric("Điểm số", f"{st.session_state.score}/100")
    st.write(f"Độ khó: {st.session_state.level}")
    st.write(f"Số câu đúng: {st.session_state.score // 10}/10")

    if st.session_state.score == 100:
        st.success("Xuất sắc! Bạn đã đạt điểm tuyệt đối!")
    elif st.session_state.score >= 70:
        st.success("Rất tốt! Tiếp tục phát huy nhé!")
    else:
        st.info("Cố gắng luyện tập để đạt điểm cao hơn!")

    if st.button("🔄 Chơi lại", type="primary"):
        st.session_state.game = False
        st.session_state.done = False
        st.rerun()
