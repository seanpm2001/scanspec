# ![logo][] scanspec

[![CI](https://github.com/dls-controls/scanspec/actions/workflows/code.yml/badge.svg)](https://github.com/dls-controls/scanspec/actions/workflows/code.yml)
[![Coverage](https://codecov.io/gh/dls-controls/scanspec/branch/master/graph/badge.svg)](https://codecov.io/gh/dls-controls/scanspec)
[![PyPI](https://img.shields.io/pypi/v/scanspec.svg)](https://pypi.org/project/scanspec)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Specify step and flyscan Paths using combinations of:

- Specs like Line or Spiral
- Optionally Snaking
- Zip, Product and Concat to compose
- Masks with multiple Regions to restrict

Serialize the Spec rather than the expanded Path and reconstruct it on the
server. It can them be iterated over like a [cycler][], or a stack of scan Frames
can be produced and expanded Paths created to consume chunk by chunk.

[cycler]: https://matplotlib.org/cycler/

Source          | <https://github.com/dls-controls/scanspec>
---             | ---
PyPI            | `pip install scanspec`
Documentation   | <https://dls-controls.github.io/scanspec>
Releases        | <https://github.com/dls-controls/scanspec/releases>

An example ScanSpec of a 2D snaked grid flyscan inside a circle spending 0.4s at
each point looks like:

```python
from scanspec.specs import Line, fly
from scanspec.regions import Circle

grid = Line(y, 2.1, 3.8, 12) * ~Line(x, 0.5, 1.5, 10)
spec = fly(grid, 0.4) & Circle(x, y, 1.0, 2.8, radius=0.5)
```

![plot][]

You can then either iterate through the scan positions directly for convenience:

```python
for point in spec.midpoints():
    print(point)
# ...
# {'y': 3.1818181818181817, 'x': 0.8333333333333333, 'DURATION': 0.4}
# {'y': 3.1818181818181817, 'x': 0.7222222222222222, 'DURATION': 0.4}
```

or create a Path from the stack of Frames and consume chunks of a given length
from it for performance:

```python
from scanspec.core import Path

stack = spec.calculate()
len(stack[0])  # 44
stack[0].axes()  # ['y', 'x', 'DURATION']

path = Path(stack, start=5, num=30)
chunk = path.consume(10)
chunk.midpoints  # {'x': <ndarray len=10>, 'y': <ndarray len=10>, 'DURATION': <ndarray len=10>}
chunk.upper  # bounds are same dimensionality as positions
```

<!--
Anything below this line is used when viewing README.md and will be replaced
when included in index.md
-->

[plot]: https://raw.githubusercontent.com/dls-controls/scanspec/master/docs/images/plot_spec.png
[logo]: https://raw.githubusercontent.com/dls-controls/scanspec/master/docs/images/scanspec-logo.svg

See https://dls-controls.github.io/scanspec for more detailed documentation.