class Stack(object):
	__stack = []
	__top = -1
	__base = 0

	def __init__(self):
		pass

	def is_empty(self):
		if (self.__top == -1):
			return True

		return False

	def push(self, value):

		if (value not in self.__stack):
			self.__stack.append(value)
			self.__top+=1

		self.__stack.remove(value)
		self.__stack.append(value)
		self.__top+=1

	def pop(self,value):
		if (value not in self.__stack):
			return

		self.__stack.remove(value)

	def take_base(self):
		value = self.__stack[self.__base]

		return value

	def print_stack(self):

		print(self.__stack)

