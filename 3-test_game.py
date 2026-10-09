import unittest
from aquavyrrix import Race
class Tests(unittest.TestCase):
 def test_progress(self):
  g=Race();g.step(.1);self.assertGreater(g.distance,0)
 def test_jump(self):
  g=Race();g.step(.1,jump=True);self.assertGreater(g.jump,0);self.assertGreater(g.cooldown,0)
 def test_fall(self):
  g=Race();g.x=2;g.step(.1);self.assertEqual(g.falls,1);self.assertEqual(g.x,0)
 def test_finish(self):
  g=Race();g.distance=999;g.step(.1);self.assertTrue(g.done)
 def test_rivals(self):
  g=Race();before=g.rivals[:];g.step(.1);self.assertTrue(all(a>b for a,b in zip(g.rivals,before)))
 def test_place(self):
  g=Race();g.rivals=[1,2,3];self.assertEqual(g.place,4)
if __name__=='__main__':unittest.main()
