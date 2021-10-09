import smtplib, ssl
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import loginInfo

#! HTML versiyon
yazi_html = """
<html>
  <body>
    <p>
        Python ile mail gönderme.
        HTML düzeninde mail gönderme testi.
        <a href="https://twitter.com/alpcusta">Twitter hesabıma git</a>
        <a href="https://www.instagram.com/alpcusta">Instagram hesabıma git</a>
    </p>
  </body>
</html>
"""

port = 465  #! SSL için port numarası
smtp_server = "smtp.gmail.com"

baslik = "SMTP ve email.mime ile Gönderildi"
gonderen_email = loginInfo.email    #loginInfo adında dosya oluşturuldu ve içinde email adlı değişken tanımlandı. Gönderici e-posta bu değişkene eklenmeli
gonderen_sifre= loginInfo.sifre     #loginInfo adında dosya oluşturuldu ve içinde sifre adlı değişken tanımlandı. Gönderici e-postasının şifresi bu değişkene eklenmeli
alici_email = "alici@gmail.com"     #alıcının e-postası

#! MIMEMultipart objesi oluşturuyoruz - Mail'in kendisini temsil ediyor ?
mesaj = MIMEMultipart()

#! oluşturuan objeye ekleme yapıyoruz
mesaj["Subject"] = baslik
mesaj["From"] = gonderen_email
mesaj["To"] = alici_email

#! mail'i MIMEText objesine dönüştürüyoruz
mailIcerik = MIMEText(yazi_html,"html")

#! MIMEText objesini Multipart objesine ekliyoruz
mesaj.attach(mailIcerik)

#! SSL bağlamı oluşturuyoruz
ssl_context = ssl.create_default_context()

#! güvenli bağlantı ile sunucuya bağlanıyoruz ve mail'i gönderiyoruz
try:
    with smtplib.SMTP_SSL(smtp_server, port, context=ssl_context) as email_server:
        email_server.login(gonderen_email, gonderen_sifre)
        email_server.sendmail(gonderen_email,alici_email,mesaj.as_string())
    print("Mail gönderme başarılı")
except:
    print("Bir sorun oluştu")

#? Dosya yüklemek için 
#! part = MIMEBase("application", octet-stream)
#! part.set_payload(open(c:/Dosya_Yolu/dosyaAdi.pdf))
#! part.add_header("Content-Disposition", "attachment", filename="dosyaAdi.pdf")
#! mesaj.attach(part)