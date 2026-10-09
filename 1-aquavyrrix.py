#!/usr/bin/env python3
"""Original offline water-slide racing against computer rivals."""
import curses,math,random,time
from ui import put,run
VERSION='1.0.0'
class Race:
 def __init__(self,seed=0):self.rng=random.Random(seed);self.x=0.;self.distance=0.;self.speed=25.;self.rivals=[-8.,-15.,-22.];self.rival_speeds=[24,25,26];self.time=0.;self.jump=0.;self.cooldown=0.;self.falls=0;self.done=False
 def step(self,dt,steer=0,jump=False):
  if self.done:return
  dt=max(0,min(.1,dt));self.time+=dt;self.cooldown=max(0,self.cooldown-dt)
  if jump and not self.cooldown:self.jump=.8;self.cooldown=4
  airborne=self.jump>0;self.jump=max(0,self.jump-dt);self.x+=steer*1.8*dt
  curve=math.sin(self.distance/70)*.35;self.x-=curve*dt
  if abs(self.x)>1.05 and not airborne:self.falls+=1;self.x=0;self.speed=10
  else:self.speed=min(34,self.speed+5*dt)
  # Jumping cuts curved sections but risks drifting off the slide on landing.
  self.distance+=(self.speed+(8 if airborne else 0))*dt
  for i,v in enumerate(self.rival_speeds):self.rivals[i]+=v*dt
  self.done=self.distance>=1000
 @property
 def place(self):return 1+sum(d>self.distance for d in self.rivals)
def loop(s):
 s.timeout(40);g=Race();paused=True;last=time.monotonic()
 while True:
  h,w=s.getmaxyx();key=s.getch();now=time.monotonic();dt=now-last;last=now
  if key in (27,ord('q')):return
  if key==ord('r'):g=Race();paused=True
  if key in (ord('p'),ord(' ')):paused=not paused
  steer=-1 if key in (ord('a'),curses.KEY_LEFT) else 1 if key in (ord('d'),curses.KEY_RIGHT) else 0
  if steer:paused=False
  if w>=50 and h>=20 and not paused:g.step(dt,steer,key==ord('j'))
  s.erase();put(s,0,1,f'AQUAVYRRIX  {int(g.distance)}/1000  place {g.place}/4  falls {g.falls}',curses.A_BOLD);put(s,1,1,f'Jump cooldown {g.cooldown:.1f}s  time {g.time:.1f}s')
  if w<50 or h<20:put(s,3,1,'Resize to50x20. Paused.')
  else:
   road=max(18,w//2);center=w//2;playerrow=h-5
   for row in range(3,h-3):
    ahead=(playerrow-row)*6;bend=int(math.sin((g.distance+ahead)/70)*w/8);left=center-road//2+bend
    put(s,row,left,'█');put(s,row,left+1,'≈'*(road-1));put(s,row,left+road,'█')
   for i,d in enumerate(g.rivals):
    row=playerrow-int((d-g.distance)/6)
    if 3<=row<h-3:
     bend=int(math.sin(d/70)*w/8);put(s,row,center+bend+(-1+i)*road//4,'['+str(i+1)+']',curses.A_BOLD)
   bend=int(math.sin(g.distance/70)*w/8);put(s,playerrow,center+bend+int(g.x*road/2),'^P^' if g.jump else '[P]',curses.A_REVERSE)
   if g.done:put(s,h//2,max(1,w//2-13),f'FINISH - place {g.place}/4! R retry',curses.A_REVERSE)
   elif paused:put(s,h//2,max(1,w//2-10),'Space or steer starts',curses.A_REVERSE)
  put(s,h-1,1,'A/D arrows steer | J jump shortcut | Space/P pause | R retry | Esc/q exit');s.refresh()
if __name__=='__main__':
 import sys
 if '--version' in sys.argv:print(VERSION)
 else:raise SystemExit(run(loop))
