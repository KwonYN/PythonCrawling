import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders


# 보내는 사람 정보
me = "myemail@gmail.com"
my_password = ""

# 로그인하기
s = smtplib.SMTP_SSL('smtp.gmail.com')
s.login(me, my_password)

# 받는 사람 정보
emails = ["email1@naver.com", "email2@naver.com", "email3@gmail.com"]

for you in emails:
    # 메일 기본 정보 설정
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "[] 추석 관련 기사 공유"
    msg['From'] = me
    msg['To'] = you

    # 메일 내용 쓰기
    content = "한가위, 무엇을 하고 계신가요!?!?"
    part2 = MIMEText(content, 'plain')
    msg.attach(part2)

    # 파일 첨부
    part = MIMEBase('application', "octet-stream")
    with open("articles.xlsx", 'rb') as file:
        part.set_payload(file.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment", filename="추석기사.xlsx")
    msg.attach(part)

    # 메일 보내고 서버 끄기
    s.sendmail(me, you, msg.as_string())
s.quit()