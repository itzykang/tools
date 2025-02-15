import requests
from bs4 import BeautifulSoup
import hashlib
import time
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
        with smtplib.SMTP_SSL('smtp.example.com', 465) as server:  # 根据你的邮箱服务商调整
            server.login(from_addr, password)
            server.sendmail(from_addr, [to_addr], msg.as_string())
            print("邮件发送成功")
    except Exception as e:
        print(f"邮件发送失败: {e}")

def get_page_content_hash(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        # 将页面内容转换为字符串，并计算其哈希值
        page_hash = hashlib.md5(soup.prettify().encode()).hexdigest()
        return page_hash
    except Exception as e:
        print(f"无法获取页面: {e}")
        return None

def monitor(url, interval=60):
    last_hash = None
    while True:
        current_hash = get_page_content_hash(url)
        if last_hash is None:
            last_hash = current_hash
        elif current_hash != last_hash:
            print("页面发生了变化！")
            last_hash = current_hash
            send_email_notification('页面发生变化', '考试页面有新的通知了！', '2715089171@qq.com')
        else:
            print("页面没有变化。")
        time.sleep(interval)  # 等待一段时间再检查

if __name__ == "__main__":
    url = "http://82.157.138.16:8091/CRAC/crac/pages/list_examMsg.html"
    monitor(url, interval=300)  # 设置检查间隔为60秒
