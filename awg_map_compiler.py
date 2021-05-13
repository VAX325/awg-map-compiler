from os.path import getsize
from zlib import compress
from sys import argv

# Defines
COMPILER_VERSION = "0.1A"
DEBUG = False

# Map
map_buffer = bytes(''.encode('utf-8'))
map_compressed = None


def compile_map(raw_name, end_name):
    global map_buffer, map_compressed
    with open(raw_name) as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        for element in content:
            element_list = element.split()
            
            if element_list[0][0] != '#':
                # ID:     0
                # TYPE:   1
                # GROUP:  2
                # POS_X:  3
                # POX_Y:  4
                # SIZE_W: 5
                # SIZE_H: 6
                if DEBUG and element_list[0][0] != '[':
                    print("DEBUG: |ID: {0}|TYPE: {1}|GROUP: {2}|POSITION: x={3} y={4}| SIZE: width={5} height={6}|".format(
                        element_list[0], element_list[1], element_list[2], element_list[3],
                        element_list[4], element_list[5], element_list[6]
                    )
                    )
                elem_encoded = element.encode('utf-8') + "\n".encode('utf-8')
                map_buffer = map_buffer + elem_encoded
        map_compressed = compress(map_buffer, level=-1)
        out = open(end_name, 'wb')
        out.write(map_compressed)
        out.close()
        print('Complete: file size: {0} bytes'.format(getsize(end_name)))


def verify_map(file):
    print("Start verifying {0}".format(file))


if __name__ == '__main__':
    print("VAX AWG Map Compiler {0}.".format(COMPILER_VERSION))
    argc = len(argv)
    if argc <= 1:
        print("Use: awg_map_compiler.py [Required parameters] [Optional parameters] map_name output_name ")
        print("\n[Required parameters]:")
        print("-c - compile raw map file into map file. Example: -c my_map my_map_out")
        print("map_name - name of raw file without extension. Example: my_map")
        print("output_name - name of compiled file without extension. Example: my_map_out")
        print("-v - verify the raw map file or map file. Example: -v my_map.lvl")
        print("\n[Optional parameters]:")
        print("-cxt - custom files extension. Warning: game can't find map file without '.lvl' extension")
        print("\nIn future version functional can change!")
    else:
        if argv[1] == "-c":
            print("Start compiling {0}.lvl".format(argv[3]))
            compile_map(argv[2] + ".rlvl", argv[3] + ".lvl")
        elif argv[1] == "-v":
            print("Verifying {0} file".format(argv[2]))
            verify_map(argv[2])
        else:
            print("Error. Check your command line.")
