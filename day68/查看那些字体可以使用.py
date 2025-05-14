import matplotlib.font_manager as fm

# 获取所有可用字体
fonts = fm.findSystemFonts()

# 筛选可能的中文字体（根据字体文件名或路径判断）
chinese_fonts = []
for font_path in fonts:
    try:
        font_name = fm.FontProperties(fname=font_path).get_name()
        # 检查字体名或路径是否包含中文字体相关关键词
        if "hei" in font_path.lower() or "song" in font_path.lower() or "kai" in font_path.lower():
            chinese_fonts.append((font_name, font_path))
    except:
        continue

# 打印可用的中文字体
print("可用的中文字体：")
for name, path in chinese_fonts:
    print(f"- 名称: {name}, 路径: {path}")