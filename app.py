import streamlit as st
import random

st.set_page_config(page_title="Game Giải Toán Nhanh", page_icon="🧮")

st.title("🧮 Game Giải Toán Nhanh")
st.write("Hãy tính nhẩm và nhập kết quả chính xác để tích lũy điểm!")

# Khởi tạo trạng thái trò chơi
if "score" not in st.session_state:
    st.session_state.score = 0
if "num1" not in st.session_state:
    st.session_state.num1 = random.randint(1, 20)
    st.session_state.num2 = random.randint(1, 20)
    st.session_state.op = random.choice(["+", "-", "*"])

def next_question():
    st.session_state.num1 = random.randint(1, 20)
    st.session_state.num2 = random.randint(1, 20)
    st.session_state.op = random.choice(["+", "-", "*"])

def check_answer():
    user_ans = st.session_state.user_input
    num1, num2, op = st.session_state.num1, st.session_state.num2, st.session_state.op
    correct = eval(f"{num1} {op} {num2}")
    
    if user_ans == correct:
        st.session_state.score += 10
        st.toast("Chính xác! +10 điểm 🎉", icon="✅")
    else:
        st.toast(f"Chưa đúng! Đáp án đúng là {correct}", icon="❌")
    
    next_question()

# Hiển thị điểm số
st.metric(label="Điểm số hiện tại", value=st.session_state.score)

# Hiển thị phép toán
op_symbol = "×" if st.session_state.op == "*" else st.session_state.op
st.subheader(f"Tính: {st.session_state.num1} {op_symbol} {st.session_state.num2} = ?")

# Ô nhập kết quả
st.number_input(
    "Nhập đáp án của bạn và ấn Enter:", 
    key="user_input", 
    step=1, 
    value=None,
    on_change=check_answer
)

if st.button("Đổi câu hỏi khác"):
    next_question()
    st.rerun()
import base64

# Đọc file nhạc
audio_file = "xương rồng (intro).mp3"

try:
    with open(audio_file, "rb") as f:
        audio_bytes = f.read()
        audio_base64 = base64.b64encode(audio_bytes).decode()
        
        # Sử dụng HTML để nhúng nhạc, tự động phát và lặp lại
        audio_html = f"""
            <audio autoplay loop>
                <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
            </audio>
        """
        st.markdown(audio_html, unsafe_allow_html=True)
except FileNotFoundError:
    st.write("Không tìm thấy file nhạc nền.")
import streamlit as st
import base64
import streamlit as st
import base64

import streamlit as st
import sympy as sp
import base64
import os

# Cấu hình trang giao diện
st.set_page_config(page_title="Math Challenge & Chill", page_icon="🌿", layout="centered")

# ==========================================
# 1. HÀM XỬ LÝ HÌNH NỀN TỪ FILE LOKAL
# ==========================================
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(image_file):
    if os.path.exists(image_file):
        bin_str = get_base64_of_bin_file(image_file)
        page_bg_img = f'''
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{bin_str}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        /* Lớp nền trắng mờ để làm nổi bật chữ và công thức Toán */
        .block-container {{
            background-color: rgba(255, 255, 255, 0.88);
            padding: 3rem;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        }}
        /* Tùy chỉnh nút Bắt đầu */
        .stButton>button {{
            width: 100%;
            border-radius: 50px;
            height: 60px;
            font-size: 24px;
            font-weight: bold;
            background-color: #4CAF50;
            color: white;
            border: none;
            transition: 0.3s;
        }}
        .stButton>button:hover {{
            background-color: #45a049;
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }}
        </style>
        '''
        st.markdown(page_bg_img, unsafe_allow_html=True)
    else:
        st.warning(f"⚠️ Không tìm thấy file hình nền '{image_file}'. Vui lòng đặt file vào cùng thư mục với app.py.")

# Gọi hàm set background (Sử dụng chính xác tên file bạn cung cấp)
set_background('image_2ab06d.jpg')

# ==========================================
# 2. QUẢN LÝ TRẠNG THÁI (SESSION STATE)
# ==========================================
if 'started' not in st.session_state:
    st.session_state.started = False

# ==========================================
# 3. MÀN HÌNH CHỜ (START SCREEN)
# ==========================================
if not st.session_state.started:
    st.markdown("<h1 style='text-align: center; color: #2E7D32;'>🌿 Math & Chill 🌿</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: #555;'>Vừa giải toán chất lượng cao, vừa nghe rap thả thính</h4>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Chèn nhạc mp3/m4a
    audio_file = 'Bản ghi Mới 10.m4a'
    if os.path.exists(audio_file):
        st.audio(audio_file, format='audio/mp4')
        st.caption("🎧 Bật loa để nghe giai điệu thả thính mượt mà trước khi vào bài nhé!")
    else:
        st.error(f"⚠️ Không tìm thấy file âm thanh '{audio_file}'.")
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Nút bắt đầu
    if st.button("🚀 BẮT ĐẦU GIẢI TOÁN"):
        st.session_state.started = True
        st.rerun()

# ==========================================
# 4. MÀN HÌNH CHÍNH (SAU KHI BẤM BẮT ĐẦU)
# ==========================================
else:
    # Nút quay lại
    if st.sidebar.button("🔙 Quay lại màn hình chính"):
        st.session_state.started = False
        st.rerun()
        
    st.title("🧮 Thử Thách Hệ Phương Trình")
    st.write("Dưới đây là các hệ phương trình được chọn lọc. Hệ thống SymPy sẽ tự động tính toán và hiển thị nghiệm.")

    # Lựa chọn mức độ
    level = st.radio(
        "📌 Chọn mức độ thử thách:",
        ("🟢 Dễ: Hệ phương trình cơ bản", 
         "🟠 Khó: Hệ đối xứng loại 1", 
         "🔴 Cực khó: Hệ hoán vị vòng quanh")
    )

    st.markdown("---")
    
    # Khai báo biến SymPy
    x, y, z = sp.symbols('x y z')

    if level == "🟢 Dễ: Hệ phương trình cơ bản":
        st.subheader("🟢 Cấp độ Dễ")
        st.write("Một hệ phương trình bậc nhất 2 ẩn cơ bản nhưng đẹp mắt.")
        
        # Đề bài
        eq1 = sp.Eq(2*x + 3*y, 12)
        eq2 = sp.Eq(x - y, 1)
        
        st.latex(r"\begin{cases} 2x + 3y = 12 \\ x - y = 1 \end{cases}")
        
        if st.button("Xem đáp án"):
            sol = sp.solve((eq1, eq2), (x, y))
            st.success("✅ Hệ có nghiệm duy nhất:")
            st.latex(f"x = {sp.latex(sol[x])}, \quad y = {sp.latex(sol[y])}")

    elif level == "🟠 Khó: Hệ đối xứng loại 1":
        st.subheader("🟠 Cấp độ Khó (Hệ đối xứng loại 1)")
        st.write("Đặc điểm: Khi đổi chỗ $x$ và $y$ cho nhau, hệ phương trình không thay đổi. Phương pháp giải truyền thống là đặt $S = x+y$ và $P = xy$.")
        
        # Đề bài chất lượng:
        # x + y + xy = 5
        # x^2 + y^2 = 5
        eq1 = sp.Eq(x + y + x*y, 5)
        eq2 = sp.Eq(x**2 + y**2, 5)
        
        st.latex(r"\begin{cases} x + y + xy = 5 \\ x^2 + y^2 = 5 \end{cases}")
        
        if st.button("Xem đáp án chi tiết"):
            with st.spinner("Đang giải hệ đối xứng..."):
                sols = sp.solve((eq1, eq2), (x, y))
                st.success("✅ Các cặp nghiệm $(x, y)$ của hệ là:")
                for i, sol in enumerate(sols):
                    st.write(f"*Nghiệm {i+1}:*")
                    st.latex(f"x = {sp.latex(sol[0])}, \quad y = {sp.latex(sol[1])}")
                st.info("💡 Lưu ý: Hệ đối xứng loại 1 thường có nghiệm hoán vị (ví dụ: nếu (1,2) là nghiệm thì (2,1) cũng là nghiệm) và có thể bao gồm cả nghiệm phức.")

    elif level == "🔴 Cực khó: Hệ hoán vị vòng quanh":
        st.subheader("🔴 Cấp độ Cực Khó (Hệ hoán vị vòng quanh 3 ẩn)")
        st.write("Đặc điểm: Các biến $x, y, z$ xoay vòng cấu trúc cho nhau. Giải thủ công thường phải cộng/trừ các vế và đánh giá tổng bình phương.")
        
        # Đề bài chất lượng (nghiệm đẹp x=1, y=1, z=1):
        # x^2 - 2y = -1
        # y^2 - 2z = -1
        # z^2 - 2x = -1
        eq1 = sp.Eq(x**2 - 2*y, -1)
        eq2 = sp.Eq(y**2 - 2*z, -1)
        eq3 = sp.Eq(z**2 - 2*x, -1)
        
        st.latex(r"\begin{cases} x^2 - 2y = -1 \\ y^2 - 2z = -1 \\ z^2 - 2x = -1 \end{cases}")
        
        if st.button("Xem đáp án cực phẩm"):
            with st.spinner("Siêu máy tính SymPy đang xử lý hệ hoán vị..."):
                sols = sp.solve((eq1, eq2, eq3), (x, y, z))
                st.success("✅ Cặp nghiệm thực tuyệt đẹp của hệ là:")
                # Lọc và hiển thị nghiệm (hệ này có nghiệm thực duy nhất là 1,1,1)
                for i, sol in enumerate(sols):
                    st.write(f"*Bộ nghiệm {i+1}:*")
                    st.latex(f"x = {sp.latex(sol[0])}, \quad y = {sp.latex(sol[1])}, \quad z = {sp.latex(sol[2])}")
                
                st.info("💡 Bật mí cách giải tay: Cộng 3 phương trình lại ta được: $(x^2 - 2x + 1) + (y^2 - 2y + 1) + (z^2 - 2z + 1) = 0 \Leftrightarrow (x-1)^2 + (y-1)^2 + (z-1)^2 = 0$. Từ đó suy ra $x=y=z=1$.")
import streamlit as st
import sympy as sp
import base64
import os

# Cấu hình trang giao diện
st.set_page_config(page_title="Math Challenge & Chill", page_icon="🌿", layout="centered")

# ==========================================
# 1. HÀM XỬ LÝ HÌNH NỀN TỪ FILE LOKAL
# ==========================================
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(image_file):
    if os.path.exists(image_file):
        bin_str = get_base64_of_bin_file(image_file)
        page_bg_img = f'''
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{bin_str}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        .block-container {{
            background-color: rgba(255, 255, 255, 0.92);
            padding: 3rem;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        }}
        .stButton>button {{
            width: 100%;
            border-radius: 10px;
            height: 50px;
            font-size: 18px;
            font-weight: bold;
            transition: 0.3s;
        }}
        .btn-start>button {{
            background-color: #4CAF50;
            color: white;
            border-radius: 50px;
            height: 60px;
            font-size: 24px;
        }}
        </style>
        '''
        st.markdown(page_bg_img, unsafe_allow_html=True)
    else:
        st.warning(f"⚠️ Không tìm thấy file hình nền '{image_file}'.")

set_background('image_2ab06d.jpg')

# ==========================================
# 2. NGÂN HÀNG CÂU HỎI CHẤT LƯỢNG
# ==========================================
# Mọi phương trình đều được chuyển về dạng f(x, y, z) = 0
questions = {
    "Dễ": [
        {"eqs": ["2*x + 3*y - 12", "x - y - 1"], "display": r"\begin{cases} 2x + 3y = 12 \\ x - y = 1 \end{cases}", "vars": "x y", "hint": "Dùng phương pháp thế hoặc cộng đại số."},
        {"eqs": ["3*x - 2*y - 4", "5*x + y - 11"], "display": r"\begin{cases} 3x - 2y = 4 \\ 5x + y = 11 \end{cases}", "vars": "x y", "hint": "Nhân phương trình hai với 2 rồi cộng đại số."},
        {"eqs": ["x + 4*y - 10", "-2*x + 3*y - 2"], "display": r"\begin{cases} x + 4y = 10 \\ -2x + 3y = 2 \end{cases}", "vars": "x y", "hint": "Rút x từ phương trình 1 thế vào phương trình 2."}
    ],
    "Khó": [
        {"eqs": ["x + y + x*y - 5", "x**2 + y**2 - 5"], "display": r"\begin{cases} x + y + xy = 5 \\ x^2 + y^2 = 5 \end{cases}", "vars": "x y", "hint": "Đặt S = x+y, P = xy. Lưu ý: x^2 + y^2 = S^2 - 2P."},
        {"eqs": ["x + y - 3", "x**2 + y**2 - x*y - 3"], "display": r"\begin{cases} x + y = 3 \\ x^2 + y^2 - xy = 3 \end{cases}", "vars": "x y", "hint": "Thế S = 3 vào hệ, phân tích phương trình 2 theo S và P."},
        {"eqs": ["x**2 + y**2 + x + y - 8", "x*y - 2"], "display": r"\begin{cases} x^2 + y^2 + x + y = 8 \\ xy = 2 \end{cases}", "vars": "x y", "hint": "Thế P = 2 vào pt đầu, biến đổi về phương trình bậc 2 theo S."}
    ],
    "Cực khó": [
        {"eqs": ["x**2 - 2*y + 1", "y**2 - 2*z + 1", "z**2 - 2*x + 1"], "display": r"\begin{cases} x^2 - 2y = -1 \\ y^2 - 2z = -1 \\ z^2 - 2x = -1 \end{cases}", "vars": "x y z", "hint": "Cộng vế theo vế 3 pt lại để tạo thành tổng 3 bình phương: (x-1)^2 + (y-1)^2 + (z-1)^2 = 0"},
        {"eqs": ["x**2 + 2*y - 3", "y**2 + 2*z - 3", "z**2 + 2*x - 3"], "display": r"\begin{cases} x^2 + 2y = 3 \\ y^2 + 2z = 3 \\ z^2 + 2x = 3 \end{cases}", "vars": "x y z", "hint": "Trừ từng cặp pt vế theo vế để xuất hiện nhân tử chung (x-y), (y-z), (z-x)."},
        {"eqs": ["x**3 - 3*y + 2", "y**3 - 3*z + 2", "z**3 - 3*x + 2"], "display": r"\begin{cases} x^3 = 3y - 2 \\ y^3 = 3z - 2 \\ z^3 = 3x - 2 \end{cases}", "vars": "x y z", "hint": "Xét tính đơn điệu của hàm số hoặc trừ vế theo vế để phân tích nhân tử."}
    ]
}

# ==========================================
# 3. QUẢN LÝ TRẠNG THÁI (SESSION STATE)
# ==========================================
if 'started' not in st.session_state:
    st.session_state.started = False
if 'idx_De' not in st.session_state:
    st.session_state.idx_De = 0
if 'idx_Kho' not in st.session_state:
    st.session_state.idx_Kho = 0
if 'idx_CucKho' not in st.session_state:
    st.session_state.idx_CucKho = 0
if 'show_answer' not in st.session_state:
    st.session_state.show_answer = False

def next_question(level_key, max_len):
    st.session_state[level_key] = (st.session_state[level_key] + 1) % max_len
    st.session_state.show_answer = False

# ==========================================
# 4. MÀN HÌNH CHỜ (START SCREEN)
# ==========================================
if not st.session_state.started:
    st.markdown("<h1 style='text-align: center; color: #2E7D32;'>🌿 Math & Chill 🌿</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: #555;'>Vừa giải toán chất lượng cao, vừa nghe rap thả thính</h4>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    audio_file = 'Bản ghi Mới 10.m4a'
    if os.path.exists(audio_file):
        st.audio(audio_file, format='audio/mp4')
        st.caption("🎧 Bật loa để nghe giai điệu thả thính trước khi vào bài nhé!")
    else:
        st.error(f"⚠️ Không tìm thấy file âm thanh '{audio_file}'.")
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    st.markdown('<div class="btn-start">', unsafe_allow_html=True)
    if st.button("🚀 BẮT ĐẦU GIẢI TOÁN"):
        st.session_state.started = True
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# 5. MÀN HÌNH CHÍNH (SAU KHI BẮT ĐẦU)
# ==========================================
else:
    col1, col2 = st.columns([1, 4])
    with col1:
        if st.button("🔙 Quay lại"):
            st.session_state.started = False
            st.rerun()
    
    st.title("🧮 Thử Thách Hệ Phương Trình")

    # Lựa chọn mức độ
    level_choice = st.radio(
        "📌 Chọn mức độ thử thách:",
        ("Dễ", "Khó", "Cực khó"),
        horizontal=True
    )
    
    # Map tên session state tương ứng với level
    state_keys = {"Dễ": "idx_De", "Khó": "idx_Kho", "Cực khó": "idx_CucKho"}
    current_key = state_keys[level_choice]
    current_idx = st.session_state[current_key]
    
    # Lấy câu hỏi hiện tại
    q_data = questions[level_choice][current_idx]
    
    st.markdown("---")
    st.subheader(f"Câu hỏi {current_idx + 1} / {len(questions[level_choice])}:")
    
    # Hiển thị đề bài
    st.latex(q_data["display"])
    
    with st.expander("💡 Gợi ý giải tay (Mở để xem)"):
        st.write(q_data["hint"])

    col_ans, col_next = st.columns(2)
    
    with col_ans:
        if st.button("🔑 Xem đáp án"):
            st.session_state.show_answer = True
            
    with col_next:
        if st.button("⏭️ Bài tiếp theo"):
            next_question(current_key, len(questions[level_choice]))
            st.rerun()

    # Xử lý giải toán bằng SymPy khi bấm "Xem đáp án"
    if st.session_state.show_answer:
        with st.spinner("Siêu máy tính SymPy đang xử lý..."):
            # Khai báo biến
            syms = sp.symbols(q_data["vars"])
            
            # Chuyển đổi chuỗi thành biểu thức SymPy
            eqs = [sp.Eq(sp.sympify(e), 0) for e in q_data["eqs"]]
            
            # Giải hệ
            sols = sp.solve(eqs, syms)
            
            st.success("✅ *ĐÁP ÁN:*")
            if isinstance(sols, dict):
                # 1 Nghiệm duy nhất (dictionary)
                latex_str = ", \quad ".join([f"{sp.latex(var)} = {sp.latex(val)}" for var, val in sols.items()])
                st.latex(latex_str)
            elif isinstance(sols, list) and len(sols) > 0:
                # Nhiều nghiệm (list of tuples/dicts)
                for i, sol in enumerate(sols):
                    st.write(f"*Nghiệm {i+1}:*")
                    if isinstance(sol, tuple):
                        latex_str = ", \quad ".join([f"{sp.latex(syms[j])} = {sp.latex(val)}" for j, val in enumerate(sol)])
                        st.latex(latex_str)
                    elif isinstance(sol, dict):
                        latex_str = ", \quad ".join([f"{sp.latex(var)} = {sp.latex(val)}" for var, val in sol.items()])
                        st.latex(latex_str)
            else:
                st.info("Hệ phương trình vô nghiệm hoặc quá phức tạp để hiển thị nghiệm thực đơn giản.")
