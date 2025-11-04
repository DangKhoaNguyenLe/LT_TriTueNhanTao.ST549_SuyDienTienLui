
def suyDienTien(DuKien, rules):
    ds_DuKien= set(DuKien)
    DuKien_Check = True
    
    while DuKien_Check:
        DuKien_Check = False
        
        for rule in rules:
            if rule["then"] not in ds_DuKien:
                dsDieuKien = rule["if"]   
                if check_DieuKienSDT(dsDieuKien, ds_DuKien):
                    ds_DuKien.add(rule["then"])
                    DuKien_Check = True

    return ds_DuKien

def check_DieuKienSDT(DieuKien, ds_DuKien):
    if isinstance(DieuKien, str):
        return DieuKien in ds_DuKien
    if isinstance(DieuKien, dict):
        if "and" in DieuKien:
            return all(c in ds_DuKien for c in DieuKien["and"])
        if "or" in DieuKien:
            return any(c in ds_DuKien for c in DieuKien["or"])
            
    return False