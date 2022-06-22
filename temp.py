import arabic_reshaper

text1 = "mohab"

text2 = "مهاب"

if '\u0600' <= text1[int(len(text1)/2)] <= '\u06FF':
    text1 = arabic_reshaper.reshape(text1)[::-1]

if '\u0600' <= text2[int(len(text1)/2)] <= '\u06FF':
    text2 = arabic_reshaper.reshape(text2)[::-1]

print("--------------------")
print(text1)
print(text2)
print("--------------------")
