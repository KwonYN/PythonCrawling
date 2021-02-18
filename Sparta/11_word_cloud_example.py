from wordcloud import WordCloud

# import matplotlib.font_manager as fm
#
# # 이용 가능한 폰트 중 '고딕'만 선별
# for font in fm.fontManager.ttflist:
#     if 'Gothic' in font.name:
#         print(font.name, font.fname)

texts = ''
with open("with Areum.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        # print(line)
        texts += line
# print(texts)

wc = WordCloud(font_path='C:/WINDOWS/Fonts/malgunbd.ttf', background_color="white", width=600, height=400)
wc.generate(texts)
wc.to_file("result.png")