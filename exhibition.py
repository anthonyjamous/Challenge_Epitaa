PATH = 'C:/Users/antho/PycharmProjects/'


def readfile(names):
    # hashmap to store all paintings by characteristic
    characteristics = {}
    paintingId = []
    for name in names:
        f = open(PATH + name, 'r')
        id = 0
        for line in f:

            if id == 0:
                numberofpaintings = int(line)
            else:
                paintingstr = line.rstrip().split(' ')
                type = paintingstr[0]
                nbofcharacteristics = paintingstr[1]
                p = Painting(type, id-1)
                paintingId.append(p.id)
                print(p.id)
                for x in range(2, int(nbofcharacteristics) + 2):

                    if paintingstr[x] in characteristics:
                        characteristics[paintingstr[x]].append(p)

                        "Key exists, so we append the painting"
                    else:
                        "Key doesn't exist, so we start a new list with the painting"
                        characteristics[paintingstr[x]] = [p]
            id += 1

        f2 = open('out-'+name, "a")
        portrait = []
        for chara in characteristics.values(): #we already know that they have something in common so that is where we should start

            for i in range(len(chara)):
                if chara[i].id in paintingId:
                    if chara[i].type == 'L':
                        frameglassLand = FrameGlass([chara[i]])
                        # save them to an output file
                        f2.write(str(chara[i].id))
                        f2.write("\n")
                        paintingId.remove(chara[i].id) # wen need to remove them from the id list , so when we come across them again, we don't re add them in a frameglass
                    else:
                        portrait.append(chara[i])


            # add them in frameglass by couples of 2:
            for i in range(0, len(portrait) - 4, 2):
                frameglassPort = FrameGlass([portrait[i], portrait[i + 1]])
                # save them to an output file
                f2.write(str(chara[i].id) + " " + str(chara[i + 1]) + "\n")
                paintingId.remove(chara[i].id)
                paintingId.remove(chara[i + 1].id)
        f2.close()










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
