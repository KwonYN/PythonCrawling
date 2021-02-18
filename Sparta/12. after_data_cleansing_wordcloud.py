from wordcloud import WordCloud

from PIL import Image
import numpy as np

# import matplotlib.font_manager as fm
#
# # 이용 가능한 폰트 중 '고딕'만 선별
# for font in fm.fontManager.ttflist:
#     if 'Gothic' in font.name:
#         print(font.name, font.fname)

texts = ''
with open("kakaotalk.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        # print(line)
        if '] [' in line:
            texts += line.split('] ')[2].replace('이모티콘\n', '').replace('사진\n', '').replace('ㅋ', '').replace('ㅎ', '').replace('ㅠ', '').replace('ㅜ', '').replace('삭제된 메시지입니다', '')
            # 1. if '] [' in line:
            # 1-1) -----xxxx년 xx월 xx일-----
            # 1-2) ~~님이 입장했습니다.
            # 1-3) [대화명] [오전/후 시간] 대화내용~~
            # 위의 내용들(즉, 대와 내용 자체와 크게 상관이 없는 것들)을 제외하고 뽑고
            # 2. texts += line.split('] ')[2]
            # "[대화명] [오전/후 시간] 대화내용~~"에서 '] '를 기준으로 스플릿 후, 세 번째 있는 "대화내용~~"만을 뽑고 싶다!!
            # 3. .replace('없앨 것들', '')
            # 불필요한 대화내용을 제거!
# print(texts)

# wc = WordCloud(font_path='C:/WINDOWS/Fonts/malgunbd.ttf', background_color="white", width=600, height=400)
# wc.generate(texts)
# wc.to_file("result.png")

mask = np.array(Image.open('cloud.png'))
wc = WordCloud(font_path='C:/WINDOWS/Fonts/malgunbd.ttf', background_color="white", mask=mask)
wc.generate(texts)
wc.to_file("kakao_result_masked.png")