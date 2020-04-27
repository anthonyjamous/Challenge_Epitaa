PATH = 'C:/Users/antho/PycharmProjects/'


def readfile(names):
    # hashmap to store all paintings by characteristic
    characteristics = {}

    for name in names:
        f = open(PATH + name, 'r')
        id = 0
        for line in f:
            id += 1
            if id == 1:
                numberofpaintings = int(line)
            else:
                paintingstr = line.rstrip().split(' ')
                type = paintingstr[0]
                nbofcharacteristics = paintingstr[1]
                p = Painting(type, id)
                print(p.id)
                for x in range(2, int(nbofcharacteristics) + 2):

                    if paintingstr[x] in characteristics:
                        characteristics[paintingstr[x]].append(p)

                        "Key exists, so we append the painting"
                    else:
                        "Key doesn't exist, so we start a new list with the painting"
                        characteristics[paintingstr[x]] = [p]


    for chara in characteristics.values(): #we already know that they have something in common so that is where we should start
        portrait=[]
        for i in range(len(chara)):
            if chara[i].type == 'L':
                frameglassLand=FrameGlass([chara[i]])
                #save them to an output file
            else:
                portrait.append(chara[i])
        #add them in frameglass by couples of 2:
        for i in range(0, len(portrait)-2, 2):
            frameglassPort=FrameGlass([portrait[i], portrait[i+1]])
            # save them to an output file









class Painting:
    def __init__(self, type, id):
        self.type = type
        self.id = id


class FrameGlass:
    def __init__(self, paintings):
        self.paintings = []


# smile = [p1, p2, p3]
# blue = [p4, p1, p5]
# green = [p2, p5, p4]


# EXECUTION
filenames = ['1_binary_landscapes.txt', '10_computable_moments.txt', '11_randomizing_paintings',
             '110_oily_portraits.txt', '0_example.txt']
filenamesExample = ['0_example.txt']
readfile(filenamesExample)
