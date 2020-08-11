from OpenAPI.Lib.MyHead import *
from OpenAPI.Config.email_config import *


def send_mail():
    sender = email_sender
    password = email_password
    receiver = email_receiver
    subject = '云丁OpenAPI自动化测试报告'
    content_report = open(report_path, 'r', encoding='UTF-8').read()
    content_log = open(log_path+'http.log', 'r').read()
    msg = MIMEMultipart()
    msg.attach(MIMEText(content_report, 'html', 'utf-8'))
    msg['From'] = formataddr([sender, sender])
    msg['To'] = ','.join(receiver)
    msg['Subject'] = Header(subject, 'utf-8')
    att_report = MIMEText(content_report)
    att_report["Content-Type"] = 'application/octet-stream'
    att_report["Content-Disposition"] = 'attachment; filename=' + "Report.html"
    att_log = MIMEText(content_log)
    att_log["Content-Type"] = 'application/octet-stream'
    att_log["Content-Disposition"] = 'attachment; filename=' + "http.log"
    msg.attach(att_report)
    msg.attach(att_log)
    server = smtplib.SMTP(email_smtpserver, 80)
    # server.set_debuglevel(1)
    server.login(sender, password)
    server.sendmail(msg['From'], msg['To'].split(','), msg.as_string())
    server.quit()
    return


# send_mail()
