import random
import time
import importlib
import argparse
import gzip

## Create a file with a random array
def create_example(filename, compress=False):
    empty_list = []
    empty_list.append([])
    empty_list.append([])
    empty_list[0].append([])
    empty_list[0].append([])
    empty_list[1].append([])
    empty_list[1].append([])
    
    for i in range(0, 5):
        empty_list[0][0].append(random.randint(0, 255))
    
    for i in range(0, 5):
        empty_list[0][1].append(random.randint(0, 255))
    
    for i in range(0, 5):
        empty_list[1][0].append(random.randint(0, 255))
    
    for i in range(0, 5):
        empty_list[1][1].append(random.randint(0, 255))
    
    if compress == False:    
        with open(f"{filename}.py", "w") as f:
            current_time = int(time.time())
            f.write(f"time_created = {current_time}\ndata = {empty_list}")
            f.close()
    else:
        with gzip.open(f"{filename}.gz", "wt") as f:
            current_time = int(time.time())
            f.write(f"date = {current_time}\ndata = {empty_list}")
            f.close()


## Create a file with a custom array
def user_input(array, filename, compress=False):
    if compress == False:
        with open(filename, "w") as f:
            current_time = int(time.time())
            f.write(f"time_created = {current_time}\ndata = {array}")
            f.close()
    else:
        with gzip.open(f"{filename}.gz", "wt") as f:
            current_time = int(time.time())
            f.write(f"date = {current_time}\ndata = {array}")
            f.close()


## Read a file
def read_file(filename, compress=False):
    if compress == False:
        try:
            filename = filename.replace(".py", "")
            data = importlib.import_module(filename)
            print(data.data)
        except:
            print("File not found")
            exit(1)
    else:
        try:
            with gzip.open(f"{filename}", "rt") as f:
                filename = filename.replace(".gz", "")
                with open(f"{filename}", "w") as f2:
                    f2.write(f.read())
                    f2.close()
                f.close()
            filename = filename.replace(".py", "")
            data = importlib.import_module(filename)
            print(data.data)
        except ModuleNotFoundError:
            print("File not found")
            exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filename", help="Filename. Note: file must end in .py", type=str, required=True)
    parser.add_argument("-example", "--generate_example", help="Generate an example file", action="store_true", required=False)
    parser.add_argument("-array", "--array_input", help='Use custom array input e.g. "[[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]"', type=str, required=False)
    parser.add_argument("-r", "--read", help="Read file", action="store_true", required=False)
    parser.add_argument("-shrink", "--compress", help="Compress the output file", action="store_true", required=False)
    parser.add_argument("-grow", "--uncompress", help="Uncompress the output file", action="store_true", required=False)
    args = parser.parse_args()
    
    if args.generate_example:
        create_example(args.filename, compress=args.compress)
    
    if args.array_input:
        user_input(args.array_input, args.filename)

    if args.read:
        read_file(args.filename, compress=args.uncompress)