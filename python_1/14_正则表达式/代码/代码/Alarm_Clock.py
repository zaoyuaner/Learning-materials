import winsound  #导入winsound模块，实现播放闹钟铃声的功能
import time

 # 提示用户输入闹钟响的时间
my_hour = input("请设置时：")
my_minute = input("请设置分：")

flag = True
while flag:
    #获取当前时间的元组
    t = time.localtime()

    #格式化时间元组，得到一个字符串
    t_str = time.strftime("%H:%M",t)
    #切分得到的时间字符串，得到一个时间list
    now_time = t_str.split(":")

    #获得当前时间的时和分
    now_hour = now_time[0]
    now_minute = now_time[1]

    if my_hour == now_hour and my_minute == now_minute:
        music = "E:\寂寞猎人-张国荣.wav"

        #调用winsound中的PlaySound函数播放音乐，music为铃声资源，SND_ALIAS参数是未找到music就播放系统声音
        winsound.PlaySound(music,winsound.SND_ALIAS)
        flag = False


