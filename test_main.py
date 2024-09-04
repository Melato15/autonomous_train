import unittest

from main import mover_trem

class TestMoverTrem(unittest.TestCase):

  def test_parametro_vazio(self):
    self.assertIsNone(mover_trem)
  
if __name__ == '__main__':
  unittest.main()