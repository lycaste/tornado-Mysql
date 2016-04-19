# coding=utf-8

import sys
from handlers.index import IndexHandler
from handlers.user import UserHandler
url = [
	(r'/', IndexHandler),
	(r'/user',UserHandler)
]
