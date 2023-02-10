import os

target = "C:/Users/user/OneDrive/Desktop/VsCode Quick Start/Test/dataset/target.txt"
path_dataset = "C:/Users/user/OneDrive/Desktop/VsCode Quick Start/Test/dataset/"
search_string = "123"
write_string = ""
counter = 0

l = os.listdir(path_dataset)

print("hello program")

def search_for_ta_error(target, path_dataset, search_string, write_string, counter):
    with open(target, 'r+') as t:
        t.truncate(0)
        for e in l:
            print(e)
            with open(path_dataset + e) as f:
                f = f.readlines()
                for line in f:
                        counter += 1               
                        if(line.find(search_string)!=-1):
                            t.write(line)
                            if(counter == len(f)):
                                t.write("\n")


search_for_ta_error(target, path_dataset, search_string, write_string, counter)