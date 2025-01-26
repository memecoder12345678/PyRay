from color import Color
from light import Light
from material import Material, ChequeredMaterial
from point import Point
from sphere import BallSphere, BoxRectangle
from vector import Vector

WIDTH = 960
HEIGHT = 540
RENDERED_IMG = "test_box.ppm"
CAMERA = Vector(0, 0, -2)
OBJECTS = [
    BallSphere(
        Point(0, 10000.5, 1),
        10000.0,
        ChequeredMaterial(
            color1=Color.from_hex("#808080"),
            color2=Color.from_hex("#606060"),
            ambient=0.2,
            reflection=0.2,
            diffuse=0.4
        ),
    ),
    BoxRectangle(
        Point(-1, 0.2, 2),
        width=0.8,
        height=0.8,
        depth=0.8,
        material=Material(
            Color.from_hex("#CC3333"),
            ambient=0.1,
            diffuse=0.7,
            specular=1.0,
            reflection=0.3
        )
    ),
    BoxRectangle(
        Point(1, 0, 2),
        width=0.6,
        height=1.0,
        depth=0.6,
        material=Material(
            Color.from_hex("#3333CC"),
            ambient=0.1,
            diffuse=0.7,
            specular=1.0,
            reflection=0.3
        )
    ),
]
LIGHTS = [
    Light(
        Point(2.0, -0.5, -10),
        Color.from_hex("#FFFFFF")
    ),
    Light(
        Point(-2.0, -0.5, -5),
        Color.from_hex("#FFE5B4")
    ),
    Light(
        Point(0, -10.5, 0),
        Color.from_hex("#E6E6E6")
    ),
]
