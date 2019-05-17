# 需求：使用面向对象的思想描述下面这个情景
# > 王老师让小明，小花，小丽分别做自我介绍
# > 需要介绍姓名，年龄，爱好，来一段才艺展示

# 学生类
class Student():
	name = ""
	age = 0
	hobby = ""

	# 介绍时传入参数
	def introduce(self,name,age,hobby):
		print("大家好,我是%s,年龄%d,爱好%s"%(name,age,hobby))

	def singSong(self):
		print("唱歌")

	def dance(self):
		print("蹦迪")

	def play(self):
		print("上王者")


# 老师类
class Teacher():
	name = ""

	# 让学生自我介绍,传入一个老师名字,一个学生
	def letStudentIntroduce(self,name,stu):
		print( stu.name, "请做自我介绍:")

		# 让学生对象调用自我介绍的方法
		stu.introduce(stu.name,stu.age,stu.hobby)

		if stu.name == "小明":
			stu.singSong()
		elif stu.name == "小花":
			stu.dance()
		else:
			stu.play()

xiaoming = Student()
xiaoming.name = "小明"
xiaoming.age = 18
xiaoming.hobby = "唱歌"

xiaohua = Student()
xiaohua.name = "小花"
xiaohua.age = 16
xiaohua.hobby = "跳舞"


xiaoli = Student()
xiaoli.name = "小丽"
xiaoli.age = 17
xiaoli.hobby = "打游戏"

# 老师
teacher = Teacher()
teacher.name = "王老师"

# 老师对象调用方法     传入自己的名字,传入学生对象
teacher.letStudentIntroduce(teacher.name,xiaoming)
teacher.letStudentIntroduce(teacher.name,xiaohua)
teacher.letStudentIntroduce(teacher.name,xiaoli)