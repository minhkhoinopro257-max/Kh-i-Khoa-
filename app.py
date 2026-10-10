
import random
import math
import streamlit as st

st.set_page_config(
    page_title="Math Challenge - Thi vào 10",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 MATH CHALLENGE")
st.caption("Toán Học mathematics ")

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #101827, #20395c);
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


# ==================== TẠO CÂU HỎI ====================

def tao_cau_hoi(level):
    dang = random.choice(
        ["ham_so", "phuong_trinh", "viet", "hinh_hoc",
         "thuc_te", "bieu_thuc", "xac_suat"]
    )

    # MỨC DỄ: cơ bản
    if level == "Dễ":

        if dang == "ham_so":
            a = random.randint(1, 5)
            x = random.randint(-5, 5)
            return f"Cho y = {a}x. Tính y khi x = {x}", a*x

        if dang == "phuong_trinh":
            x = random.randint(-10, 10)
            a = random.randint(2, 8)
            b = random.randint(-10, 10)
            return f"Giải phương trình {a}x + ({b}) = {a*x+b}. Tìm x", x

        if dang == "viet":
            x1 = random.randint(-8, 8)
            x2 = random.randint(-8, 8)
            b = -(x1+x2)
            c = x1*x2
            return f"Tính tổng hai nghiệm của x² + ({b})x + ({c}) = 0", x1+x2

        if dang == "hinh_hoc":
            a = random.randint(3, 12)
            b = random.randint(3, 12)
            return f"Hình chữ nhật có chiều dài {a} cm, rộng {b} cm. Tính diện tích (cm²)", a*b

        if dang == "thuc_te":
            a = random.randint(10, 50)
            return f"Một món hàng giá {a*1000} đồng, giảm 10%. Số tiền giảm là bao nhiêu nghìn đồng?", a/10

        if dang == "bieu_thuc":
            a = random.randint(2, 15)
            return f"Tính √{a*a} + {a}", 2*a

        a = random.randint(1, 5)
        return f"Gieo xúc xắc cân đối. Có bao nhiêu kết quả thuận lợi để xuất hiện số {a}?", 1

    # MỨC VỪA: trung bình 
    if level == "Vừa":

        if dang == "ham_so":
            a = random.randint(1, 5)
            b = random.randint(1, 10)
            return f"Cho y = {a}x + {b}. Tìm x khi y = {a*3+b}", 3

        if dang == "phuong_trinh":
            x = random.randint(-8, 8)
            r = random.randint(-8, 8)
            return f"Tìm nghiệm lớn hơn của x² - ({x+r})x + ({x*r}) = 0", max(x, r)

        if dang == "viet":
            s = random.randint(-10, 10)
            p = random.randint(-10, 10)
            # Tạo hai nghiệm nguyên có tổng s và tích p
            pairs = [
                (a, b) for a in range(-10, 11)
                for b in range(-10, 11)
                if a+b == s and a*b == p
            ]
            if pairs:
                a, b = random.choice(pairs)
                return f"Phương trình có hai nghiệm {a} và {b}. Tính x₁² + x₂²", a*a+b*b
            return "Giải phương trình x² - 5x + 6 = 0. Tính tổng hai nghiệm", 5

        if dang == "hinh_hoc":
            r = random.randint(2, 10)
            return f"Hình tròn bán kính {r} cm. Tính diện tích chia cho π (cm²)", r*r

        if dang == "thuc_te":
            a = random.randint(2, 10)
            return f"Một xe đi {a*12} km trong {a} giờ. Tính vận tốc (km/h)", 12

        if dang == "bieu_thuc":
            a = random.randint(2, 12)
            return f"Tính (√{a*a})² - {a}² + 3", 3

        a = random.randint(1, 6)
        return f"Hộp có 6 thẻ đánh số từ 1 đến 6. Xác suất rút được thẻ số {a} là 1/x. Tìm x", 6

    # MỨC KHÓ: hơi bị khó 
    if dang == "ham_so":
        a = random.randint(1, 5)
        x = random.randint(-5, 5)
        y = a*x*x
        return f"Cho y = {a}x². Tính y khi x = {x}", y

    if dang == "phuong_trinh":
        a = random.randint(1, 5)
        x1 = random.randint(-8, 8)
        x2 = random.randint(-8, 8)
        b = -(x1+x2)
        c = x1*x2
        return f"Tìm tổng bình phương hai nghiệm của x² + ({b})x + ({c}) = 0", x1*x1+x2*x2

    if dang == "viet":
        x1 = random.randint(-8, 8)
        x2 = random.randint(-8, 8)
        b = -(x1+x2)
        c = x1*x2
        return f"Với hai nghiệm x₁, x₂ của x² + ({b})x + ({c}) = 0, tính 1/x₁ + 1/x₂", round((x1+x2)/(x1*x2), 2) if x1*x2 else 0

    if dang == "hinh_hoc":
        a = random.randint(3, 12)
        b = random.randint(3, 12)
        return f"Tam giác vuông có hai cạnh góc vuông {a} và {b}. Tính bình phương cạnh huyền", a*a+b*b

    if dang == "thuc_te":
        x = random.randint(2, 10)
        return f"Một hình chữ nhật có chiều rộng {x} cm, dài hơn chiều rộng 3 cm. Tính diện tích (cm²)", x*(x+3)

    if dang == "bieu_thuc":
        a = random.randint(2, 12)
        return f"Tính (√{a*a} + 1)(√{a*a} - 1)", a*a-1

    a = random.randint(1, 6)
    return f"Gieo xúc xắc cân đối. Xác suất ra số {a} bằng mấy phần sáu? Nhập tử số", 1


# ==================== TRẠNG THÁI GAME ====================

if "game" not in st.session_state:
    st.session_state.game = False
if "done" not in st.session_state:
    st.session_state.done = False


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


# ==================== MÀN HÌNH CHÍNH ====================

if not st.session_state.game:

    st.subheader("🎯 Chọn độ khó")

    level = st.radio(
        "Mức độ",
        LEVELS,
        horizontal=True
    )

    if level == "Dễ":
        st.info("Co bản.")
    elif level == "Vừa":
        st.info("cũng vừa .")
    else:
        st.warning("hơi khó .")

    st.write("📌 10 câu hỏi • Mỗi câu đúng 10 điểm.")

    if st.button("🚀 BẮT ĐẦU THI", type="primary"):
        bat_dau(level)
        st.rerun()

elif not st.session_state.done:

    i = st.session_state.index
    cau, dap_an = st.session_state.questions[i]

    st.subheader(f"Độ khó: {st.session_state.level}")
    st.progress(i / 10)
    st.write(f"Câu {i+1}/10")
    st.write(f"🏆 Điểm: {st.session_state.score}/100")
    st.markdown(f"### {cau}")

    if st.session_state.feedback is not None:
        dung, da = st.session_state.feedback
        if dung:
            st.success("Chính xác! +10 điểm")
        else:
            st.error(f"Chưa đúng. Đáp án: {da}")

    with st.form(f"answer_{i}"):
        tra_loi = st.number_input(
            "Nhập đáp án (có thể nhập số thập phân):",
            value=0.0,
            step=1.0
        )
        gui = st.form_submit_button("Kiểm tra đáp án")

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
    st.header("🏁 KẾT QUẢ BÀI THI")
    st.metric("Tổng điểm", f"{st.session_state.score}/100")
    st.write(f"Độ khó: {st.session_state.level}")
    st.write(f"Số câu đúng: {st.session_state.score // 10}/10")

    if st.session_state.score >= 90:
        st.success("Xuất sắc! Bạn làm bài rất tốt!")
    elif st.session_state.score >= 70:
        st.success("Khá tốt! Hãy tiếp tục luyện tập.")
    else:
        st.warning("Hãy xem lại kiến thức và thử lại nhé!")

    if st.button("🔄 Thi lại", type="primary"):
        st.session_state.game = False
        st.session_state.done = False
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
