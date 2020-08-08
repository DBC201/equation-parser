from equation import Parser

if __name__ == "__main__":
    p = Parser("(x^2+3x+5)/5")
    print(p.parse({'x': 5}))
