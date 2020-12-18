from equation import Parser

if __name__ == "__main__":
    p = Parser("(2*(3 +2))")
    print(p.parse({'x': 5}))
