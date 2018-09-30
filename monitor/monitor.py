# coding = utf-8

"""
@author: sy

@file: monitor.py

@time: 2018/9/22 15:33

@desc: 远程连接linux ssh监控后台日志

"""
import paramiko


class Monitor(object):
    def __init__(self, server_ip, user, pwd):
        """ 初始化ssh客户端 """
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.client = client
            print('------------开始连接服务器(%s)-----------' % server_ip)
            self.client.connect(server_ip, 22, username=user, password=pwd, timeout=4)
            print('------------认证成功!.....-----------')
        except Exception:
            print(f'连接远程linux服务器(ip:{server_ip})发生异常!请检查用户名和密码是否正确!')

    def link_server(self, cmd):
        """连接服务器发送命令"""
        try:
            stdin, stdout, stderr = self.client.exec_command(cmd)
            content = stdout.read().decode('gbk')
            return content
        except Exception as e:
            print('link_server-->返回命令发生异常,内容:', e)
        finally:
            self.client.close()


if __name__ == '__main__':
    pass
