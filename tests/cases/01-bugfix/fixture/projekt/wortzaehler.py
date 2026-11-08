import sys

def zaehle(pfad):
    with open(pfad, encoding="ascii") as f:
        text = f.read()
    woerter = text.split(" ")
    return len(woerter)

if __name__ == "__main__":
    print(zaehle(sys.argv[1]))
