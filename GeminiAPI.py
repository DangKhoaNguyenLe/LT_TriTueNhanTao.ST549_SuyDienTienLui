import os
import google.generativeai as gemini



# CẢNH BÁO: Không an toàn nếu bạn chia sẻ code này
gemini.configure(api_key="AIzaSyDQJ4wrDxlTx602ys9gfm3NWlaAIyJQa0g")

# Sử dụng tên model chính xác
gemini_model = gemini.GenerativeModel('gemini-2.0-flash')

print("Đã cấu hình model thành công!")