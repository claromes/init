import py5
import pymunk as pm

space = pm.Space()
shapes = []

def settings():
    py5.size(500, 500)

def setup():
    space.gravity = (0, 600)
    
    seg = pm.Segment(space.static_body, (100, 400), (400, 400), 3)
    seg.elasticity = 0.8    
    
    shapes.append(seg)
    space.add(seg)
    
def draw():
    py5.background(222)
    
    mass = 5
    moi = pm.moment_for_circle(mass, 0, 5)
    
    body = pm.Body(mass, moi)
    body.position = (py5.random(100, 400), 200)
    
    shp = pm.Circle(body, 5, (0, 0)) 
    shp.friction = 0.8
    shp.elasticity = 1
    
    shapes.append(shp)
    space.add(body, shp)
    
    for shp in shapes:
        if isinstance(shp, pm.Segment):
            py5.line(100, 400, 400, 400)
        elif isinstance(shp, pm.Circle):
            x, y = shp.body.position
            py5.circle(x, y, 8)
    
    space.step(0.01)

py5.run_sketch()