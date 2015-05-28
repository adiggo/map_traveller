__author__ = 'xiaopingli'

from flask import Flask
from flaskext.mysql import MySQL
import sys
import MySQLdb
import logging

# access to user table 
class user:
    confirm_user_in_db = """ select userid from Users.user where fid = %s"""
    def get_fb_user(self, fid):
        try:
            conn = MySQLdb.connect(host = "127.0.0.1", port = 3306, user = "luss", passwd = "root", db="Users")
            cursor = conn.cursor()
            cursor.execute(self.confirm_user_in_db, fid)
            userid = cursor.fetchone()
            if userid is None:
                return None
            else:
                return userid
        except:
            e = sys.exc_info()[0]
            print "Error %s" % e
            logging.error("failed to validate user")
        return None

