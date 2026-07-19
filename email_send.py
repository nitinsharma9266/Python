import smtplib

my_email="nitinsharma926614@gmail.com"
password="boxv tmie vsrn vota"

connection=smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login(user=my_email,password=password)

connection.sendmail(
    from_addr=my_email,
    to_addrs="recipientemail@gmail.com",
    msg="Subject:Test Email\n\nHello World"
)
print("Email sent successfully!")
connection.close()
