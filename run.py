# coding = utf-8

"""
@author: sy

@file: run.py

@time: 2018/9/23 18:11

@desc: 程序入口

"""

import sys, os

BASE_DIR = os.path.dirname((os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from monitor.monitor import Monitor
from mail.send_mails import SendMail
from config.init_configs import init_config, get_linux_config
from apscheduler.schedulers.blocking import BlockingScheduler


def auto_job():
    init_config()  # 初始化配置
    linux_dict = get_linux_config()
    content_list = []
    for ip in linux_dict:
        linux_info = linux_dict[ip].split(',')  # 根据ip获取user和pwd,通过逗号分隔成list(linux_info--> [user,pwd])
        user = linux_info[0]
        pwd = linux_info[1]
        monitor = Monitor(ip, user, pwd)
        # TODO cmd的获取,添加根据ini不同ip实现动态对应linux指令

        content = f'当前服务器ip:{ip},日志内容:\n' + monitor.link_server(cmd) + '\n\n'
        content_list.append(content)
    sendMail = SendMail()
    sendMail.send_mails(''.join(content_list))


def main():
    # 基于quartz的定时任务调度器
    scheduler = BlockingScheduler()
    """ FIELD_NAMES = ('year', 'month', 'day', 'week', 'day_of_week', 'hour', 'minute', 'second') """
    # 没用过quartz的同学去了解下CRON表达式~
    scheduler.add_job(auto_job, 'cron', hour='0/1', id='auto_job_id')
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        scheduler.remove_job('auto_job_id')


if __name__ == '__main__':
    main()
