import pymysql
pymysql.version_info = (1, 4, 0, 'final', 0)
pymysql.install_as_MySQLdb()

from .celery import app as celery_app
