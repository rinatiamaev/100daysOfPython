import smtplib
my_email = "fdff8697@gmail.com"
password = "erfre4f"

connction = smtplib.SMTP("smtp.gmail.com")
connction.starttls()
connction.login(user=my_email, password=password)
connction.sendmail(from_addr=my_email, to_addrs="boratora@gmail.com")
connction.close()
