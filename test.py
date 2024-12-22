import google.generativeai as palm

# Khởi tạo với API Key của bạn
palm.configure(api_key="AIzaSyDjI-t8qy06KGh2d46TmHTen3S24hB35jE")

def tao_phan_hoi(prompt, ngu_canh=""):
    """
    Tạo phản hồi từ chatbot sử dụng Google Generative AI.

    Args:
        prompt: Câu hỏi hoặc yêu cầu của người dùng.
        ngu_canh: Thông tin ngữ cảnh bổ sung (tuỳ chọn).

    Returns:
        Câu trả lời của chatbot.
    """

    try:
        # Kết hợp ngữ cảnh (nếu có) với prompt
        prompt_day_du = f"{ngu_canh} {prompt}" if ngu_canh else prompt

        # Gọi API để tạo phản hồi
        phan_hoi = palm.generate_text(
            prompt=prompt_day_du,
            temperature=0.7  # Điều chỉnh độ ngẫu nhiên (0.0 - 1.0)
        )

        # Trả về kết quả nếu có
        if phan_hoi and phan_hoi.result:
            return phan_hoi.result
        else:
            return "Xin lỗi, tôi không thể trả lời lúc này."

    except Exception as loi:
        return f"Đã xảy ra lỗi: {loi}"

def main():
    """
    Hàm chính cho chatbot.
    """

    ngu_canh_hien_tai = ""  # Lưu trữ ngữ cảnh của cuộc trò chuyện

    print("Chào mừng bạn đến với chatbot! Nhập 'thoát' để kết thúc.")

    while True:
        cau_hoi = input("Bạn: ")
        if cau_hoi.lower() == "thoát":
            break

        # Tạo phản hồi, bao gồm cả ngữ cảnh hiện tại
        cau_tra_loi = tao_phan_hoi(cau_hoi, ngu_canh=ngu_canh_hien_tai)

        # In câu trả lời của chatbot
        print("Chatbot:", cau_tra_loi)

        # Cập nhật ngữ cảnh cho câu hỏi tiếp theo (tuỳ chọn)
        ngu_canh_hien_tai = f"{ngu_canh_hien_tai} {cau_hoi} {cau_tra_loi}"

# Chạy hàm main nếu đây là chương trình chính
if __name__ == "__main__":
    main()
