import os
from django.core.mail import send_mail

os.environ['DJANGO_SETTINGS_MODULE'] = 'liujiang.settings'

if __name__ == '__main__':

    send_mail(
        '来自寒沙老师的测试邮件',
        'hello world',
        '1069916147@qq.com',
        ['xxx@qq.com'],
    )