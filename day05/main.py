import unittest

if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover('./')
    runner = unittest.TextTestRunner()
    runner.run(suite)