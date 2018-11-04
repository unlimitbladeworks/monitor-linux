monitor-linux(监控linux)
===

设计需求：一到周末，公司总是会让我们人肉监控服务器状态(因为技术还没到互联网层公司的技术,没有自动化---例如工具Ansible之类的，ε=(´ο｀*)))唉)
所以，我觉得这种东西如果可以实现一个远程自动化的监控工具是再好不过了，周末可以省下大把时间去浪:smile:~


Environment(环境)
---
本项目为python编写的项目。

- python3.6+

用到的库:

- paramiko      (linux ssh库)
- smtplib       (邮件库)
- APScheduler   (定时任务库)

项目目录结构
---
monitor-linux(:smiling_imp:)

    |--config
        |--gol.py               (全局变量字典)
        |--init_configs.py      (读取ini初始化配置)
        |--linux_config.ini     (linux服务器配置文件)
        |--mail_settings.ini    (邮箱设置配置文件)
        |--time_config.ini      (cron定时设置配置文件)
    |--mail
        |--send_mails.py        (发送邮件)
    |--monitor
        |--monitor.py           (监控linux模块,连接linux服务器)
    |--utils
        |--util.py              (工具类)
    |--run.py                   (程序入口)

相关文章链接
---
慕课网首发手记:http://www.imooc.com/article/251463

自带BGM的博客:https://blog.csdn.net/s740556472/article/details/82890586

初学者有学python的可以关注公众号哟！

![migezatan](https://img-blog.csdnimg.cn/20181104164256754.png)
