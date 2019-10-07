import unittest

from api import app
from app.main import db
from app.main.config import Config


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] == Config.DB_TYPE + "://" + Config.DB_USER + ":" + Config.DB_PASS + "@" + Config.HOST + "/" + Config.DB_NAME
        self.app = app.test_client()

    def tearDown(self):
        db.session.remove()


if __name__ == '__main__':
    unittest.main()
