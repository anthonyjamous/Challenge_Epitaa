import argparse
import random

class Parser():

    def __init__(self,input_file,sub_file,seed,iter):
        self.paintings_L = {}
        self.paintings_P = {}
        self.frameglass = {}
        self.sub = open(sub_file, "w")
        self.nb_lines = ""
        self.seed = seed
        self.iter = iter
        self.histo = {}

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
        self.histogram()
        print(self.frameglass)
        print(self.histo)

    def histogram(self):
        for i in self.frameglass:
            for j in self.frameglass[i][1:]:
                if j in self.histo.keys():
                    self.histo[j] += 1
                else:
                    self.histo[j] = 1

    def create_frameglass(self):
        for i in self.paintings_L:
            self.frameglass[str(i)] = self.paintings_L[i]
        P_list = []
        for i in self.paintings_P:
            P_list += [self.paintings_P[i]+[i]]
        for i in P_list:
            i[0] = int(i[0])
        P_list.sort()
        frame_P_list = []
        while len(P_list)>1:
            maxi = P_list.pop()
            for count, i in enumerate(P_list):
                for j in maxi[1:-1]:
                    if j in i:
                        flag = False
                        break
                    else:
                        flag = True
                if flag:
                    mini = P_list.pop(count)
                    break
            if not flag:
                mini = P_list.pop(0)
            temp = list(set(mini[1:-1]+maxi[1:-1]))+[str(mini[-1])+" "+str(maxi[-1])]
            frame_P_list += [[str(len(temp)-1)]+temp]
        for i in frame_P_list:
            self.frameglass[i[-1]] = i[:-1]
        self.nb_lines = len(self.frameglass)


    def easy_output(self):
        self.sub.write(str(self.nb_lines)+"\n")
        for i in self.frameglass:
            self.sub.write(i+"\n")
        self.sub.close()

    def sized_output(self):
        self.sub.write(str(self.nb_lines) + "\n")
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
        self.sub.write(str(self.nb_lines) + "\n")

        list_paints = []
        for i in self.frameglass:
            list_paints += [i]

        random.seed(self.seed)

        random.shuffle(list_paints)

        for i in list_paints:
            self.sub.write(i + "\n")
        self.sub.close()

    def shaker_output(self):
        self.sub.write(str(self.nb_lines) + "\n")
        shake_dic = {}
        for i in self.frameglass:
            if self.frameglass[i][0] in shake_dic.keys():
                shake_dic[self.frameglass[i][0]].append(i)
            else:
                shake_dic[self.frameglass[i][0]] = [i]

        shake_list = map(int, shake_dic.keys())
        shake_list.sort()
        swap_list = []
        for i in shake_list:
            swap_list += shake_dic[str(i)]

        random.seed(self.seed)

        count = 0
        while count < self.iter:
            int1 = random.randint(0,self.nb_lines-1)
            int2 = random.randint(0,self.nb_lines-1)
            while int1 == int2:
                int2 = random.randint(0, self.nb_lines - 1)
            if self.test_swap(swap_list,int1,int2) > 0:
                self.swap(swap_list,int1,int2)
            count += 1

        for id in swap_list:
            self.sub.write(id + "\n")

    def test_swap(self,swap_list,val1,val2):
        if val1 == 0 and val2 == self.nb_lines-1:
            delta = self.score(swap_list[val2],swap_list[val1+1]) + self.score(swap_list[val2-1],swap_list[val1]) - (self.score(swap_list[val1],swap_list[val1+1]) + self.score(swap_list[val2-1],swap_list[val2]))
            return delta
        elif val1 == self.nb_lines-1 and val2 == 0:
            delta = self.score(swap_list[val1],swap_list[val2+1]) + self.score(swap_list[val1-1],swap_list[val2]) - (self.score(swap_list[val2],swap_list[val2+1]) + self.score(swap_list[val1-1],swap_list[val1]))
            return delta
        elif val1 == 0:
            delta = self.score(swap_list[val2],swap_list[val1+1]) + self.score(swap_list[val2-1],swap_list[val1]) + self.score(swap_list[val1],swap_list[val2+1]) \
                    - (self.score(swap_list[val1],swap_list[val1+1]) + self.score(swap_list[val2-1],swap_list[val2]) + self.score(swap_list[val2],swap_list[val2+1]))
            return delta
        elif val2 == 0:
            delta = self.score(swap_list[val1],swap_list[val2+1]) + self.score(swap_list[val1-1],swap_list[val2]) + self.score(swap_list[val2],swap_list[val1+1]) \
                    - (self.score(swap_list[val2],swap_list[val2+1]) + self.score(swap_list[val1-1],swap_list[val1]) + self.score(swap_list[val1],swap_list[val1+1]))
            return delta
        elif val2 == self.nb_lines-1:
            delta = self.score(swap_list[val1-1], swap_list[val2]) + self.score(swap_list[val2], swap_list[val1 + 1]) + self.score(swap_list[val2 - 1], swap_list[val1]) \
                    - (self.score(swap_list[val1-1], swap_list[val1]) + self.score(swap_list[val1], swap_list[val1 + 1]) + self.score(swap_list[val2 - 1], swap_list[val2]))
            return delta
        elif val1 == self.nb_lines-1:
            delta = self.score(swap_list[val2-1], swap_list[val1]) + self.score(swap_list[val1], swap_list[val2 + 1]) + self.score(swap_list[val1 - 1], swap_list[val2]) \
                    - (self.score(swap_list[val2-1], swap_list[val2]) + self.score(swap_list[val2], swap_list[val2 + 1]) + self.score(swap_list[val1 - 1], swap_list[val1]))
            return delta
        else:
            delta = self.score(swap_list[val1 - 1], swap_list[val2]) + self.score(swap_list[val2], swap_list[val1 + 1]) + self.score(swap_list[val2 - 1], swap_list[val1]) + self.score(swap_list[val1],swap_list[val2+1]) \
                    - (self.score(swap_list[val1 - 1], swap_list[val1]) + self.score(swap_list[val1], swap_list[val1 + 1]) + self.score(swap_list[val2 - 1], swap_list[val2]) + self.score(swap_list[val2],swap_list[val2+1]))
            return delta

    def swap(self,swap_list, frame1, frame2):

        swap_list[frame1], swap_list[frame2] = swap_list[frame2], swap_list[frame1]

    def score(self,frame1,frame2):
        if frame1 == frame2:
            return 0
        intersection = list(set(self.frameglass[frame1][1:]).intersection(self.frameglass[frame2][1:]))
        val1 = len(intersection)
        val2 = len(frame1) - len(intersection)
        val3 = len(frame2) - len(intersection)
        return min(val1, val2, val3)

def main():
    parser = argparse.ArgumentParser(description="Script to parse the input file and give a submission file")
    parser.add_argument("input", type=str, help="The path to the input file")
    parser.add_argument("submit", type=str, help="The path to the submitted file")
    parser.add_argument("--opt", type=str, default="easy", help="Selection of the optimization")
    parser.add_argument("--seed", type=int, default=42, help="Selection of a specific value for the seed for randomized optimizations")
    parser.add_argument("--iter", type=int, default=10000, help="Max number of iterations")

    args = parser.parse_args()

    parse = Parser(args.input, args.submit,args.seed,args.iter)
    if args.opt == "easy":
        parse.easy_output()
    elif args.opt == "size":
        parse.sized_output()
    elif args.opt == "rand":
        parse.random_output()
    elif args.opt == "shake":
        parse.shaker_output()

if __name__ == "__main__":
    main()