
import random
import streamlit as st

st.set_page_config(
    page_title="Math Challenge",
    page_icon="🧮",
    layout="centered"
)

st.title("🧮 MATH CHALLENGE")
st.write("Chinh phục thử thách Toán học qua 3 cấp độ!")

LEVELS = [
    "🟢 Cấp 1 - Toán tiểu học",
    "🔵 Cấp 2 - Toán THCS",
    "🔴 Cấp 2 nâng cao"
]

if "game" not in st.session_state:
    st.session_state.game = False


def tao_cau_hoi(level):
    # CẤP 1: TOÁN TIỂU HỌC
    if level == LEVELS[0]:
        dang = random.choice(["cong", "tru", "nhan", "chia"])

        if dang == "cong":
            a = random.randint(10, 999)
            b = random.randint(10, 999)
            return f"{a} + {b} = ?", a + b

        if dang == "tru":
            a = random.randint(100, 999)
            b = random.randint(10, a)
            return f"{a} - {b} = ?", a - b

        if dang == "nhan":
            a = random.randint(2, 99)
            b = random.randint(2, 12)
            return f"{a} × {b} = ?", a * b

        b = random.randint(2, 12)
        kq = random.randint(2, 100)
        return f"{b * kq} ÷ {b} = ?", kq

    # CẤP 2: TOÁN THCS
    elif level == LEVELS[1]:
        dang = random.choice([
            "phuong_trinh",
            "luy_thua",
            "can_bac_hai",
            "phan_so",
            "hang_dang_thuc"
        ])

        if dang == "phuong_trinh":
            x = random.randint(-10, 10)
            a = random.randint(2, 9)
            b = random.randint(-20, 20)
            c = a * x + b
            return f"Giải: {a}x + ({b}) = {c}. Tìm x", x

        if dang == "luy_thua":
            a = random.randint(2, 10)
            b = random.randint(2, 4)
            return f"Tính {a}^{b}", a ** b

        if dang == "can_bac_hai":
            a = random.randint(1, 20)
            return f"Tính √{a*a}", a

        if dang == "phan_so":
            a = random.randint(1, 10)
            b = random.randint(2, 10)
            c = random.randint(1, 10)
            d = random.randint(2, 10)
            return (
                f"Tính {a}/{b} + {c}/{d} (làm tròn 2 chữ số)",
                round(a / b + c / d, 2)
            )

        a = random.randint(2, 12)
        return f"Tính ({a} + 3)² - {a}²", 6 * a + 9

    # CẤP 2 NÂNG CAO
    else:
        dang = random.choice([
            "he_phuong_trinh",
            "phuong_trinh_bac_hai",
            "phan_tich",
            "can_thuc",
            "ham_so"
        ])

        if dang == "he_phuong_trinh":
            x = random.randint(-5, 5)
            y = random.randint(-5, 5)
            a = x + y
            b = x - y
            return (
                f"Hệ: x + y = {a}; x - y = {b}. Tính x",
                x
            )

        if dang == "phuong_trinh_bac_hai":
            x = random.randint(-10, 10)
            r = random.randint(-10, 10)
            # Nghiệm của x² + bx + c = 0 gồm x và r
            b = -(x + r)
            c = x * r
            return (
                f"Tìm nghiệm lớn hơn hoặc bằng nghiệm kia của "
                f"t² + ({b})t + ({c}) = 0 (nhập nghiệm lớn hơn)",
                max(x, r)
            )

        if dang == "phan_tich":
            a = random.randint(2, 12)
            return f"Giải: x² - {a*a} = 0. Nhập nghiệm dương x", a

        if dang == "can_thuc":
            a = random.randint(2, 15)
            return f"Tính √({a*a} + {2*a + 1})", a + 1

        a = random.randint(2, 10)
        return f"Cho y = 2x + 3. Tính y khi x = {a}", 2 * a + 3


def bat_dau(level):
    st.session_state.level = level
    st.session_state.questions = [
        tao_cau_hoi(level) for _ in range(10)
    ]
    st.session_state.index = 0
    st.session_state.score = 0
    st.session_state.game = True
    st.session_state.done = False
    st.session_state.feedback = None


if not st.session_state.game:
    st.subheader("🎯 Chọn cấp độ")

    level = st.radio(
        "Bạn muốn thử sức với:",
        LEVELS
    )

    st.markdown("""
    **🟢 Cấp 1:** Cộng, trừ, nhân, chia và tính toán cơ bản.

    **🔵 Cấp 2:** Phương trình, lũy thừa, căn bậc hai,
    phân số và hằng đẳng thức.

    **🔴 Cấp 2 nâng cao:** Hệ phương trình, phương trình
    bậc hai, phân tích đa thức và hàm số.
    """)

    if st.button("🚀 BẮT ĐẦU", type="primary"):
        bat_dau(level)
        st.rerun()

elif not st.session_state.done:
    i = st.session_state.index
    cau, dap_an = st.session_state.questions[i]

    st.subheader(st.session_state.level)
    st.progress(i / 10)
    st.write(f"Câu {i + 1}/10")
    st.write(f"🏆 Điểm: {st.session_state.score}/100")
    st.markdown(f"### {cau}")

    with st.form(f"answer_{i}"):
        tra_loi = st.number_input(
            "Nhập đáp án:",
            value=0.0,
            step=1.0
        )
        gui = st.form_submit_button("Kiểm tra đáp án")

    if gui:
        dung = abs(float(tra_loi) - float(dap_an)) < 0.011

        if dung:
            st.session_state.score += 10
            st.session_state.feedback = "correct"
        else:
            st.session_state.feedback = f"wrong:{dap_an}"

        st.session_state.index += 1

        if st.session_state.index == 10:
            st.session_state.done = True

        st.rerun()

else:
    st.balloons()
    st.header("🎉 KẾT QUẢ")
    st.metric("Điểm của bạn", f"{st.session_state.score}/100")
    st.write(f"Cấp độ: {st.session_state.level}")
    st.write(f"Số câu đúng: {st.session_state.score // 10}/10")

    if st.session_state.score == 100:
        st.success("Xuất sắc! Bạn đã hoàn thành hoàn hảo!")
    elif st.session_state.score >= 70:
        st.success("Làm tốt lắm! Hãy tiếp tục cố gắng.")
    else:
        st.info("Hãy luyện tập thêm và thử lại nhé!")

    if st.button("🔄 CHƠI LẠI"):
        st.session_state.game = False
        st.session_state.done = False
        st.rerun()
