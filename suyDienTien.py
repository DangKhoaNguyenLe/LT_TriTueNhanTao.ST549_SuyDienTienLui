
def suyDienTien(DuKien, rules):
    ds_DuKien = list(DuKien)  
    luatDaSuDung = set()             
    chechLuatMoi = True

    while chechLuatMoi:
        chechLuatMoi = False
        for i, rule in enumerate(rules):
            if i in luatDaSuDung:
                continue
            if check_DieuKien(rule["if"], ds_DuKien):
                if rule["then"] not in ds_DuKien:
                    ds_DuKien.append(rule["then"])  
                    chechLuatMoi = True
                luatDaSuDung.add(i)
    return ds_DuKien

def check_DieuKien(DieuKien, ds_DuKien):
    ds_lower = [d.lower() if isinstance(d, str) else d for d in ds_DuKien]

    if isinstance(DieuKien, str):
        return DieuKien.lower() in ds_lower

    if isinstance(DieuKien, dict):
        if "and" in DieuKien:
            return all(c.lower() in ds_lower for c in DieuKien["and"])
        if "or" in DieuKien:
            return any(c.lower() in ds_lower for c in DieuKien["or"])
            
    return False

