import math

class cShape:
  def __init__(self,name):
    self.name=name
  def getCorners(self):
    return []

class cBox(cShape):
  def __init__(self,d,h,l):
    self.d=round(d)
    self.h=round(h)
    self.l=l;
    self.name=self.toString()
  def toString(self):
    s = "BXD%dH%dL%d" % (self.d, self.h, self.l)
    return s
  def getCorners(self):
    d=self.d
    h=self.h
    p=[]
    p.append(cPosition(-d/2,-h/2))
    p.append(cPosition(d/2,-h/2))
    p.append(cPosition(d/2,h/2))
    p.append(cPosition(-d/2,h/2))
    return p

class cHole(cShape):
  def __init__(self,d,l,cp=True):
    if cp:
      self.d=round(d*1.0/10.0)*10
    else:
      self.d=round(d)
    self.l=l
    self.name=self.toString()
  def toString(self):
    dd=round(self.d/10)
    dd=dd*10
    s = "HoleR%d" % (dd) #For ADVATEST F7000S, change to the appropriate name
    return s
  def getCorners(self,n=8,start=0):
    dt=2*math.pi/n
    ds=start
    de=ds+2*math.pi
    p0=cPosition(self.d,0)
    p=[]
    p.append(p0)
    for i in range(1,n):
      p0=p0.rotate(dt)
      p.append(p0)
    return p

class cHalfHole(cShape):
  def __init__(self,radius,orientation=0):
    self.r=radius
    self.angle=orientation
    self.name=self.toString()
  
  def toString(self):
    return "HHOLER%dT%d"%(self.r,self.angle)
    
  def getCorners(self):
    th0=self.orientation*math.pi/180.0 #in degree
    n=20
    dth=math.pi/n
    p0=cPosition(self.r,0)
    p=[]
    for i in range(0,n+1):
      p.append(p0.rotate(th0+i*dth))
    return p

class cRoundTrench(cShape):
  def __init__(self,ri,ro,th0,th1):
    self.ri=ri
    self.ro=ro
    self.th0=th0*math.pi/180.0
    self.th1=th1*math.pi/180.0
    self.name=self.toString()
 
  def toString(self):
    return "RTRRI%dRO%dTH1%dTH2%d"%(self.ri,self.ro,self.th0,self.th1)
    
  def getCorners(self):
    n=20
    dth=(self.th1-self.th0)/n
    p=[]
    p0=cPosition(self.ro,0)
    for i in range(0,n+1):
      p.append(p0.rotate(self.th0+dth*i))
    p0=cPosition(self.ri,0)
    for i in range(0,n+1):
      p.append(p0.rotate(self.th0+dth*(n-i)))
    return p
    
class cPosition:
  def __init__(self,x,y):
    self.x=x
    self.y=y
  def __add__(self,p):
    return cPosition(self.x+p.x,self.y+p.y)
  def __sub__(self,p):
    return cPosition(self.x-p.x,self.y-p.y)
  def rotate(self,theta):
    s=math.sin(theta)
    c=math.cos(theta)
    p1=cPosition(c*self.x-s*self.y,s*self.x+c*self.y)
    return p1
  def __mul__(self,scalar):
    if isinstance(scalar,int) or isinstance(scalar,double):
      return cPosition(self.x*scalar,self.y*scalar)
    return None
  def __rmul__(self,scalar):
    if isinstance(scalar,int) or isinstance(scalar,double):
      return cPosition(self.x*scalar,self.y*scalar)
    return None
