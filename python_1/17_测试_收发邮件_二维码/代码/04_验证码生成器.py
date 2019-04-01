import datetime
import hashlib

from PIL import ImageFont,ImageDraw,Image
from random import randint

class VerifyCode:
	def __init__(self,width=100,height=40,size=4):
		"""

		:param width: 验证码的宽度
		:param height: 验证码的高度
		:param size: 验证码的长度
		"""
		self.width = width if width > 0 else 100
		self.height = height if height > 0 else 40
		self.size = size if size > 0 else 4
		self.pen = None   # 画笔
		self.code = ""  # 保存验证码字符串

	# @property
	# def code(self):
	# 	return self.__code
	# @code.setter
	# def code(self,code):
	# 	self.__code = code

	def generate(self):
		# 1.生成画布   # 越靠近255的颜色越浅
		im = Image.new("RGB",(self.width,self.height),self.randColor(160,255))
		# 2.生成画笔
		self.pen = ImageDraw.Draw(im)
		# 3.生成随机字符串
		self.randString()
		# 4.画字符串
		self.__drawCode()
		# 5.画干扰点
		self.__drawPoint()
		# 6.画干扰线
		self.__drawLine()
		# 7.保存图片
		im.save("vc.jpg")
	def __drawLine(self):
		"""
		画干扰线
		:return:
		"""
		for i in range(6):
			start = (randint(1,self.width-1),randint(1,self.height-1))
			end = (randint(1,self.width-1),randint(1,self.height-1))
			self.pen.line([start,end],fill=self.randColor(50,150),width = 1)

	def __drawPoint(self):
		"""
		画干扰点
		:return:
		"""
		for i in range(200):
			x = randint(1,self.width-1)
			y = randint(1,self.height-1)
			self.pen.point((x,y),fill= self.randColor(30,100))
	def __drawCode(self):
		"""
		画字符串
		:return:
		"""
		myFont = ImageFont.truetype("MSYH.TTF",size=20,encoding="UTF-8")
		for i in range(self.size):
			x = 15 + i*(self.width - 20)/self.size    # 为每个字符均匀分配位置
			y = randint(5,10)  # 随机高度
			self.pen.text((x,y),self.code[i],fill = self.randColor(0,60),font = myFont)

	def randString(self):
		"""
		产生随机整数字符串
		:return:
		"""
		result = ""
		for i in range(self.size):
			result += str(randint(0,9))
		self.code = result

	def randColor(self,low,high):    # 随机背景颜色
		return randint(low,high),randint(low,high),randint(low,high)

# class StrCode(VerifyCode):
# 	def randString(self):
# 		s1 =hashlib.md5(b"2314").hexdigest()
# 		print(s1)
# 		self.code = s1[:self.size]
if __name__ == "__main__":
	vc = VerifyCode()
	# vc = StrCode()
	vc.generate()
	print(vc.code)
