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
        return "Xin lỗi, tôi không hiểu ý bạn."
            
    if Dich:
        result = suyDienLui.suyDienLui(Dich, DuKienBanDau, rules)
        
        if result:
            return f"Đúng rồi. {DuKien[0]} {Dich}."
        
        else:
            t = ""
            for i in DuKien:
                if len(DuKien) > 1 and t != "": t += ", "
                t += i
            return f"{t} không do {Dich}."

    elif DuKien:
        kqSuyDien = suyDienTien.suyDienTien(DuKienBanDau, rules)
        kqSuyDien = kqSuyDien[1:] if len(kqSuyDien) > 1 else []
        if kqSuyDien:
            kl = ""
            for dkm in kqSuyDien:
                # if len(kqSuyDien) > 1 and kl != "": kl += "."
                kl += f"{dkm}\n" 
            return kl
        else:
            return "Không thể suy luận ra được"
        
def dinhDang(text):
    search_string = "* "
    replace_string = "<br>"
    regex_pattern = r'\*\*([^\*]+)\*\*'
    replacement_string = r'<b>\1</b>'
    text = text.replace(search_string, replace_string)
    return re.sub(regex_pattern, replacement_string, text)

@app.route("/")
def home():
    ten = "khoa"
    return render_template('index.html', name = ten)

@app.route('/chat', methods=['POST'])
def submit():   
    data = request.get_json()
    text = data.get("data", "")
    kq = suyLuan(text)
<<<<<<< HEAD
    #g = f"Câu hỏi của người dùng la {text} và câu trả lời của hệ thống {kq}.chuyển câu trả lời làm sao cho mạch lạc hơn giữ nguyên ý nghĩa câu trả lời của hệ thống. Không thêm cái gì cả"
   # gemini = GeminiAPI.gemini_model.generate_content(g)
=======
    g = f"Câu hỏi của người dùng la {text} và câu trả lời của hệ thống {kq}.chuyển câu trả lời làm sao cho mạch lạc hơn giữ nguyên ý nghĩa câu trả lời của hệ thống. Không thêm cái gì cả"
    gemini = GeminiAPI.gemini_model.generate_content(g)
>>>>>>> 0805f202729ff6056e6ee02b563102ebffece1f4
    if kq is not None: 
        return f"{kq}"
    return f"Câu của bạn không có trong tập luật"


if __name__ == "__main__":
    app.run(debug=True)
