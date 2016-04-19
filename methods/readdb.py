# coding=utf-8

from methods.db import *


def select_table(table, column, condition, value):
	sql = "select " + column + " from " + table + " where " + condition + "='" + value + "'"
	cursor = conn.cursor()
	cursor.execute(sql)
	lines = cursor.fetchall()
	return lines


def select_columns(table, column):
	sql = "select " + column + " from " + table
	cursor = conn.cursor()
	cursor.execute(sql)
	lines = cursor.fetchall()
	return lines