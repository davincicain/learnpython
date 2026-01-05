# """
# pyEmail: send email
# """
#
# import smtplib #smtp protocol package
# from email.mime.text import MIMEText #used to construct email content
#
# def main():
#
#     #email information
#     msg_from = "18017726883@163.com"
#     msg_password = "JEhBm36GVSGLkD4P"
#     msg_to = "18017726883@163.com"
#
#     #construct email content
#     subject = "python test 20260105"
#     content = "test succeeded"
#     msg = MIMEText(content)
#     msg['Subject'] = subject
#     msg['From'] = msg_from
#     msg['To'] = msg_to
#
#     #send email
#     smtpObj = smtplib.SMTP_SSL("smtp.163.com", 465)
#     smtpObj.login(msg_from, msg_password)
#     smtpObj.sendmail(msg_from, msg_to, msg.as_string())
#     print("Successfully sent email")
#     smtpObj.quit()
#
# if __name__ == '__main__':
#     main()