from subprocess import *


if __name__ == '__main__':

    port = input('请输入Tomcat服务的端口： ')
    try:
        result = Popen('netstat -ano | findstr ' + str(port), shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        orgin_str = str(result.stdout.read()).split('\\r')[0]
        second = orgin_str.split('      ')
        pid = second[-1].strip()
        print(pid)
        Popen('taskkill -PID ' + str(pid) + ' -F', shell=True)

        print("关闭tomcat成功")
    except Exception:
        print("关闭tomcat失败,请手动关闭")
