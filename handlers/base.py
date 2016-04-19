import tornado.web


class BaseHandler(tornado.web.RequestHandler):

	def data_received(self, chunk):
		pass

	def get_current_user(self):
		return self.get_secure_cookie("user")


