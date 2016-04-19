import tornado.web
import tornado.escape
from handlers.base import BaseHandler
import methods.readdb as mrd


class UserHandler(BaseHandler):
	def data_received(self, chunk):
		pass

	@tornado.web.authenticated
	def get(self):
		#username = self.get_argument("user")
		username = tornado.escape.json_decode(self.current_user)
		user_infos = mrd.select_table(table="users", column="*", condition="username", value=username)
		self.render("user.html", users=user_infos)
