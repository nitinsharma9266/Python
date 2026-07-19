import smtplib
import random

otp = random.randint(1000, 9999)

my_email = "nitinsharma926614@gmail.com"
password = "boxv tmie vsrn vota"

connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(my_email, password)

connection.sendmail(
    from_addr=my_email,
    to_addrs="uk9169832@gmail.com",
    msg=f"Subject:OTP Verification\n\nYour OTP is {otp}"
)

connection.close()

print("OTP sent:", otp)