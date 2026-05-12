def clean(fname):
    with open(fname, 'r') as f:
        output = []
        for line in f.readlines():
            line = line.strip().split(":")
            for l in line:
                sec = l.split("billion")
                print(sec)
            output.append((line[0], sec[0]))
        
    return output






if __name__ == "__main__":
    file = "file.txt"
    c = (clean(file))
    # for i in c:
    #     print(i)
    # write = open("Trade partners.csv", 'w')
    # for i in c:
    #     write.write(f"{i[0]},{i[1]}\n")
    # write.close()




