import os

baseDir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'dataBase.db'
DATABASE_PATH = os.path.join(baseDir, DATABASE)
USERNAME = 'David'
PASSWORD = '123'
SECRET_KEY = '\xefM\x1aE\x99Qs\xc1\xa6j\xbd\xc3\x9cc\xeef\x81\xed\x15!X\x93\xd7$'
WTF_CSRF_ENABLED = True