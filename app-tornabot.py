#imports
import tornado
from tornado import template
from pyjade.ext.tornado import patch_tornado

patch_tornado()

class IndexHandler(tornado.web.RequestHandler):
	def get(self):
		render('index.jade')

if __name__ == '__main__':
	main()