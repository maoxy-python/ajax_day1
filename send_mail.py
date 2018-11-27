import os
from django.core.mail import send_mail, EmailMultiAlternatives
os.environ['DJANGO_SETTINGS_MODULE'] = 'ajax_day1.settings'

if __name__ == "__main__":
    # send_mail(
    #     'AI137第一封测试邮件',
    #     'AI137不会发送邮件',
    #     '18500230996@sina.cn',
    #     ['maoxinyu925@163.com'],
    # )
    subject, from_email, to = 'AI137第二封测试邮件', '18500230996@sina.cn', 'maoxinyu925@163.com'
    text_content = '欢迎访问www.baidu.com，祝贺你收到了我的邮件，有幸收到我的邮件说明你及其幸运'
    html_content = '<p>感谢注册<a href="http://{0}/confirm/?code={1}"target = blank > www.baidu.com < / a >，\欢迎你来验证你的邮箱，验证结束你就可以登录了！ < / p > '
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
