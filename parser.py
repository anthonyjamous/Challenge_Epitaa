import argparse
import random

class Parser():

    def __init__(self,input_file,sub_file):
        self.paintings_L = {}
        self.paintings_P = {}
        self.frameglass = {}
        self.sub = open(sub_file, "w")
        self.nb_lines = ""

        f = open(input_file, "r")
        for count, i in enumerate(f.readlines()[1:]):
            temp = i.split()
            if temp[0] == "L":
                self.paintings_L[count] = temp[1:]
            elif temp[0] == "P":
                self.paintings_P[count] = temp[1:]
            else:
                print("ERROR WITH THE FILE FORMAT")
        self.create_frameglass()

    def create_frameglass(self):
        for i in self.paintings_L:
            self.frameglass[str(i)] = self.paintings_L[i]
        duo = []
        for i in self.paintings_P:
            if duo == []:
                duo += [i]
            else:
                new_val = list(set(self.paintings_P[i][1:]+self.paintings_P[duo[0]][1:]))
                new_val.insert(0,str(len(new_val)))
                self.frameglass[str(duo[0])+" "+str(i)] = new_val
                duo = []
        self.nb_lines = str(len(self.frameglass))+"\n"

    def easy_output(self):
        self.sub.write(self.nb_lines)
        for i in self.frameglass:
            self.sub.write(i+"\n")
        self.sub.close()

    def sized_output(self):
        self.sub.write(self.nb_lines)
        size_dic = {}
        for i in self.frameglass:
            if self.frameglass[i][0] in size_dic.keys():
                size_dic[self.frameglass[i][0]].append(i)
            else:
                size_dic[self.frameglass[i][0]] = [i]

        size_list = map(int,size_dic.keys())
        size_list.sort()
        size_list = map(str, size_list)
        for i in size_list:
            for j in size_dic[i]:
                self.sub.write(str(j)+"\n")
        self.sub.close()

    def random_output(self):
        self.sub.write(self.nb_lines)

        list_paints = []
        for i in self.frameglass:
            list_paints += [i]

        random.seed(42)

        random.shuffle(list_paints)

        for i in list_paints:
            self.sub.write(i + "\n")
        self.sub.close()

def main():
    parser = argparse.ArgumentParser(description="Script to parse the input file and give a submission file")
    parser.add_argument("input", type=str, help="The path to the input file")
    parser.add_argument("submit", type=str, help="The path to the submitted file")
    parser.add_argument("--opt", type=str, default="easy", help="Selection of the optimization")

    args = parser.parse_args()

    parse = Parser(args.input, args.submit)
    if args.opt == "easy":
        parse.easy_output()
    elif args.opt == "size":
        parse.sized_output()
    elif args.opt == "rand":
        parse.random_output()

if __name__ == "__main__":
    main()