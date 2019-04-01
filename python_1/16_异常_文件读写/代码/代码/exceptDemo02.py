#二、try-except-finally的使用

#1.
try:
    print(10 / 5)
except ZeroDivisionError as e:
    print(e)

finally:
    print("finally被执行")


#2.特殊情况
#注意：当在try或者except中出现return语句，finally语句仍然会被执行
def show():
    try:
        print(10 / 4)
        return
    except ZeroDivisionError as e:
        print(e)

    finally:
        print("finally被执行~~~~")

show()