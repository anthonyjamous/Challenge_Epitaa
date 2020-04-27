PATH = 'C:/Users/antho/PycharmProjects/'


def readfile(names):
    for f in names:
        f = open(PATH + f, 'r')
        content1 = f.read()
        id = 0
        for line in f:
            id += 1
            if id == 1:
                numberofpaintings = int(line)
            else:
                paintingstr = line.split(' ')
                type = paintingstr[0]
                nbofcharacteristics = paintingstr[1]
                lstcharac = []
                for x in range(2, nbofcharacteristics + 2):
                    lstcharac.append(paintingstr[x])
                p = Painting(type, id, lstcharac)


class Painting:
    def __init__(self, type, id, characteristics):
        self.type = type
        self.id = id
        self.characteristics = []


# smile = [p1, p2, p3]
# blue = [p4, p1, p5]
# green = [p2, p5, p4]


# EXECUTION
filenames = ['1_binary_landscapes.txt', '10_computable_moments.txt', '11_randomizing_paintings',
             '110_oily_portraits.txt', '0_example.txt']
readfile(filenames)
