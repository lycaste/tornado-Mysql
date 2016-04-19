# coding=utf-8

import tornado.ioloop
import tornado.options
import tornado.httpserver

from application import application
from tornado.options import define, options

define("port", default=8000, help="run on the given port", type=int)


def main():
	tornado.options.parse_command_line()
	http_server = tornado.httpserver.HTTPServer(application)
	http_server.listen(options.port)

	print('server is running at 127.0.0.1:%s' % options.port)

	tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
	main()
