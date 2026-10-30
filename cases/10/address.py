def normalize_zip(zip_code):
    """郵便番号を「123-4567」の形にそろえる。"""
    digits = zip_code.replace("-", "").replace("〒", "")
    return digits[:3] + "-" + digits[3:]
