#需求：去拉萨，乘坐各种交通工具
print("我要去拉萨")

try:
    print("我准备乘飞机过去")
    raise Exception("由于大雾，飞机不能起飞")
    print("到拉萨了，拉萨真漂亮")
except Exception as e:
    print(e)
    try:
        print("我准备乘火车过去")
        raise  Exception("由于大暴雨，铁路断了")
        print("到拉萨了，拉萨真漂亮")
    except Exception as e:
        print(e)
        print("我准备跑过去")
        print("到拉萨了，拉萨真漂亮")