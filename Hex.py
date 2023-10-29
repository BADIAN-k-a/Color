import re

def is_valid_hex_color(color):
    pattern = r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$'
    return bool(re.match(pattern,color))
#Коммит
color1="#AAbc19"
color2="#3f3"
#33ff33
color3="#Zad43a"

print(is_valid_hex_color(color2))