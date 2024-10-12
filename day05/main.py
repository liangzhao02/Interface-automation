import unittest

if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover('./',"test_parmas.py")
    runner = unittest.TextTestRunner()
    runner.run(suite)