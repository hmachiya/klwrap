import pya
from shapes import *

class cPya:
  def __init__(self,layout):
    self.layout=layout

  def getDPoint(self,p):
    return pya.DPoint(p.x,p.y)

  def getPoint(self,p):
    return pya.Point.from_dpoint(self.getDPoint(p))

  def getPointArray(self,shape):
    pts=shape.getCorners()
    pp=[]
    for p in pts:
      pp.append(self.getPoint(p))
    return pp 

  def openCell(self,cellname):
    cell = self.layout.cell(cellname)
    if cell:
      return cell
    else:
      return self.layout.create_cell(cellname)
    return null

  def makePolygon(self,shape):
    pts=self.getPointArray(shape)
    return pya.Polygon(pts)

  def openPolygonCell(self,shape,layer):
    cell = self.layout.cell(shape.toString())
    if cell:
      return cell
    else:
      cell=self.layout.create_cell(shape.toString())
      layerindex=self.layout.layer(layer,0)
      polygon=self.makePolygon(shape)
      cell.shapes(layerindex).insert(polygon)
      return cell
    return null

  def placeCell(self,cell,source,p):
    idx=source.cell_index()
    trans=pya.CplxTrans(p.x,p.y)
    cell_instance=pya.CellInstArray(idx,trans)
    return cell.insert(cell_instance)
  def openShapesCell(self,name,shapes):
    cell = self.layout.cell(name)
    if cell:
      return cell
    cell = self.layout.create_cell(name)
    for s in shapes:
      pos=s[0]
      shape=s[1]
      layer=s[1].l
      polycell=self.openPolygonCell(shape,layer)
      self.placeCell(cell,polycell,pos)
    return cell