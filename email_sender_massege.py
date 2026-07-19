import smtplib
import tkinter as tk
from tkinter import messagebox

# Email send function
def send_email():
    sender = email_entry.get()
    receiver = to_entry.get()
    subject = subject_entry.get()
    message = message_text.get("1.0", tk.END)

    password = "boxv tmie vsrn vota"

    try:
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login(sender, password)

        full_message = f"Subject:{subject}\n\n{message}"

        connection.sendmail(
            from_addr=sender,
            to_addrs=receiver,
            msg=full_message
        )

        connection.close()
        messagebox.showinfo("Success", "Email Sent Successfully!")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# GUI window
window = tk.Tk()
window.title("Email Sender App")
window.geometry("400x400")

# Labels & Entries
tk.Label(window, text="Your Email").pack()
email_entry = tk.Entry(window, width=40)
email_entry.pack()

tk.Label(window, text="To Email").pack()
to_entry = tk.Entry(window, width=40)
to_entry.pack()

tk.Label(window, text="Subject").pack()
subject_entry = tk.Entry(window, width=40)
subject_entry.pack()

tk.Label(window, text="Message").pack()
message_text = tk.Text(window, height=8, width=40)
message_text.pack()

# Button
send_button = tk.Button(window, text="Send Email", command=send_email)
send_button.pack(pady=10)

window.mainloop()

