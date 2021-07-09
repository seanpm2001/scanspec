# Example Spec

from scanspec.plot import plot_spec
from scanspec.specs import Line
from scanspec.regions import Ellipse

grid = Line("y", 3, 8, 10) * ~Line("x", 1 ,8, 10)
spec = grid & Ellipse("x", "y", 5, 5, 2, 3, 75)
plot_spec(spec)