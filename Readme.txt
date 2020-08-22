This program makes use of the Shutting yard algorithm.

to install do pip install -e git+https://github.com/DBC201/equation-parser#egg=equation

Example usage:

from equation import Parser
p = Parser("x^2")

here p.parse({'x': 2}) would return 4

you can also pass in equations to the parse method directly as well.