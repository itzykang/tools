import smtplib
from email.mime.text import MIMEText

def send_email_notification(subject, message, to_addr):
    from_addr = 'itzykang@163.com'  # 替换为你的邮箱地址
    password = 'NXFHmJnSWgDrPiBi'      # 替换为你的邮箱密码
    
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr
    
    try:
        with smtplib.SMTP_SSL('smtp.163.com', 465) as server:  # 根据你的邮箱服务商调整
            server.login(from_addr, password)
            server.sendmail(from_addr, [to_addr], msg.as_string())
            print("邮件发送成功")
    except Exception as e:
        print(f"邮件发送失败: {e}")

# 使用例子
send_email_notification('页面发生变化', '考试页面有新的通知了！', '2715089171@qq.com')
