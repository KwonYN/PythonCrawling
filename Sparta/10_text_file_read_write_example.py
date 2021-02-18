f = open("test.txt", "w", encoding="utf-8")
f.write("안녕, 스파르타!\n")
f.write("안녕, 스파르타!\n")
f.write("안녕, 스파르타!\n")
f.write("안녕, 스파르타!\n")
for i in range(5):
    f.write(f'{i+1} : 안녕, 스파르타!\n')
f.close()

texts = ''
with open("test.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        texts += line
        # print(line)
        # print() : 프린트를 하면 원래 개행이 찍혀서 나오게 됨! 그래서 한 줄씩 더 엔터가 있는 상태로 찍히는 것!
print(texts)