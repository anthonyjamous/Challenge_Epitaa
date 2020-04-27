


def readfile(names):
    # hashmap to store all paintings by characteristic
    characteristics = {}
    paintingId = []
    for name in names:
        #f = open(name, 'r')
        with open(name, "r") as f:
            id = 0
            for line in f:

                if id == 0:
                    numberofpaintings = int(line)
                else:
                    paintingstr = line.rstrip().split(' ')
                    type = paintingstr[0]
                    nbofcharacteristics = paintingstr[1]
                    p = Painting(type, id - 1)
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
            
        #f2 = open('out-' + name, "a")
        
        portrait = []
        leftOvers=[]
        output = ""
        numberOfFrameGlass = 0
        # we already know that they have something in common so that is where we should start
        for chara in characteristics.values():  
            for i in range(len(chara)):
                if chara[i].id in paintingId:
                    if chara[i].type == 'L':
                        #frameglassLand = FrameGlass([chara[i]])
                        # save them to an output file
                        output += str(chara[i].id)
                        numberOfFrameGlass += 1
                        output += "\n"
                        ''' wen need to remove them from the id list ,
                            so when we come across them again, 
                            we don't re add them in a frameglass'''
                        paintingId.remove(chara[i].id)  
                    else:
                        portrait.append(chara[i])
                        paintingId.remove(chara[i].id)

                        # add them in frameglass by couples of 2:
            if  len(portrait) % 2 != 0:
                leftOvers.append(chara[len(portrait) - 2])


        for i in range(0, len(portrait)-1):
            # frameglassPort = FrameGlass([portrait[i], portrait[i + 1]])
                # save them to an output file
                if i != len(portrait)-1:
                    output += str(portrait[i].id) + " " + str(portrait[i + 1].id) + "\n"
                    numberOfFrameGlass += 1





        for i in range(0, len(chara)-2 , 2):
            output += leftOvers[i]+ " " + leftOvers[i+1]
            numberOfFrameGlass += 1
        
        with open ('out-' + name, "a") as f2:
            f2.write(str(numberOfFrameGlass) + "\n")
            f2.write(output)
            

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
