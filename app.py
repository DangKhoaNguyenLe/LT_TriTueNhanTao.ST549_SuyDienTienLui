import re
from flask import Flask, render_template, request
import loadFileJson as loadJson
import suyDienLui as suyDienLui
import suyDienTien as suyDienTien
import XuLyText as chuyenDoi
import GeminiAPI as GeminiAPI
app = Flask(__name__, template_folder='view')



def suyLuan(text):
    RULE_FILE = "rules.json"
    rules = loadJson.loadFile(RULE_FILE) 
    DuKien, Dich = chuyenDoi.chuyenDoi(text)
    DuKienBanDau = list(DuKien) 
    if not DuKien and not Dich:
        return "Hệ thống: Xin lỗi, tôi không hiểu ý bạn."
            
    if Dich:
        result = suyDienLui.suyDienLui(Dich, DuKienBanDau, rules)
        
        if result:
            return f"ĐÚNG. Dựa trên các triệu chứng, bạn {Dich.replace('_', ' ')}."
        
        else:
            return f"KHÔNG. Tôi không thể chứng minh '{Dich.replace('_', ' ')}' từ các triệu chứng bạn cung cấp."

    elif DuKien:
        dsDieuKien = suyDienTien.suyDienTien(DuKienBanDau, rules)
        dieuKienMoi = dsDieuKien - set(DuKienBanDau)
        
        if dieuKienMoi:
            kl = "Kết quả:\n"
            for dkm in dieuKienMoi:
                kl += f"{dkm},\n" 
            return kl.strip()
        else:
            return "Không có trong tập luật"
        

@app.route("/")
def home():
    ten = "khoa"
    return render_template('index.html', name = ten)

@app.route('/chat', methods=['POST'])
def submit():   
    data = request.get_json()
    text = data.get("data", "")
    kq = suyLuan(text)
    g = f"Câu hỏi của người dùng la {text} và câu trả lời của hệ thống {kq}.chuyển câu trả lời làm sao cho mạch lạc hơn giữ nguyên ý nghĩa câu trả lời hệ thống"
    gemini = GeminiAPI.gemini_model.generate_content(g)
    if kq is not None: 
        return f"{gemini.text}"
    return f"Câu của bạn không có trong tập luật"


if __name__ == "__main__":
    app.run(debug=True)
