#!/usr/local/bin/python
import sys
import os.path
if len(sys.argv) != 2:
    print "usage: replaceKeys [filename]"
elif not os.path.isfile(sys.argv[1]):
    print "unknown file " + sys.argv[1]
else:
    file = open(sys.argv[1], "r")
    for line in file.readlines():
        line = line.replace("1584fe607554b35ce5e7b27a5ca0b12d127b36da", "[Matthieu]")
        line = line.replace("159752626920bd2b851b95e41334063e02e50e6f", "[Milos]")
        line = line.replace("1a35c71c4c83e50095383eedd43d755dca0c9d9f", "[Will]")
        line = line.replace("4ea9341de70afc1a749a2d6abd8459ffe37a59b5", "[Alex]")
        line = line.replace("a8b63bb30cfc7284eac25d8b813894b93f97699c", "[Maxi]")
        line = line.replace("3616ccf5015afa22bfdea3715cef0456ea74fad8", "[Cyrus]")
        line = line.replace("ae5c777beb4e15639809eae5216464061338734b", "[Clays Old Key]")
        line = line.replace("b40474571297fd05ac82fd2994f45c977f3ca77a", "[Max]")
        line = line.replace("d85ec41296935f9656180110f177f02317e3f807", "[Clay]")
        sys.stdout.write(line)

