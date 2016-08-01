class NameGetter(object):

	def get_name(self):
		self.name = raw_input('enter your name: ')

	def greet(self):
		print 'Hello there' , self.name

	def run(self):
		self.get_name()
		self.greet()

"""added comments here """ 

if __name__ == '__main__':
	m = NameGetter()
	m.run()
