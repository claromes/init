import py5

def settings():
    py5.size(500, 500)

def draw():
    py5.no_fill()
    py5.stroke(0)
    py5.stroke_weight(1)
    py5.rect(200, 100, 5, 15)

py5.run_sketch()