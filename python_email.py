'''
date: 2020-10-27
author: jtx
descreption: python给自己发email，用于检测自己的程序是否在运行
'''
import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import logging
from logging.handlers import RotatingFileHandler
import time
import datetime

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
dir_path = os.path.dirname(__file__)
kbp_path = os.path.dirname(dir_path)
config_path = os.path.join(kbp_path,"config.ini")

def set_log():
    logging.basicConfig(level=logging.INFO)
    file_log_handler = RotatingFileHandler(os.path.join(dir_path,"python_weixin_email_log.txt"), maxBytes=1024 * 1024 * 300, backupCount=10)
    formatter = logging.Formatter('%(asctime)s - %(filename)s - %(lineno)s - %(levelname)s - %(message)s')
    file_log_handler.setFormatter(formatter)
    logging.getLogger().addHandler(file_log_handler)

set_log()
logger = logging.getLogger(__name__)


while True:
    # 查看linux中微信进程是否在运行
    process_name_list = ['weixin_processive_second_time02.py', 'weixin_processive_second_time.py']
    list_pid=os.popen('ps -ef | grep  weixin').readlines()
    flag_stop = 0
    for key_name in process_name_list:
        if key_name in str(list_pid):
            flag_stop = 1




    def em(message, send_email):
        '''
        :param message:   发送的信息
        :param send_email:  接收人
        :return:
        '''
        msg = MIMEText(message, 'plain', 'utf-8')
        msg['From'] = Header("2682573216@qq.com", 'utf-8')  # 发送者
        msg['To'] = Header("17826808634@126.com", 'utf-8')  # 接收者
        # 标题
        subject = 'Python SMTP 邮件测试'
        msg['Subject'] = Header(subject, 'utf-8')

        from_addr = "2682573216@qq.com"  # 发送人
        password = "ppyghdwyyzjzecbj"  # 发送人密码
        smtp_server = "smtp.qq.com"  # 邮箱的smtp服务器
        # 网易邮箱SMTP smtp.163.com
        # qq邮箱SMTP smtp.qq.com
        to_addr = send_email  # 接收人
        server = smtplib.SMTP(smtp_server, 25)
        server.set_debuglevel(1)
        server.login(from_addr, password)
        server.sendmail(from_addr, [to_addr], msg.as_string())
        server.quit()

    if flag_stop == 0:
        logger.info('pid_list: {}'.format(list_pid))
        print(flag_stop)
        str_date_time = str(datetime.datetime.now())[:19]
        send_email = em('微信资讯采集程序停止了, 去服务器上看下'+'\n'+ str_date_time, '17826808634@126.com')
        logger.info('发送成功')
    time.sleep(3600)