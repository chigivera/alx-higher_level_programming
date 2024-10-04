#!/usr/bin/python3\
for i in range(10):
    print("{}".format(", ".join(f"{i}{j}"  for j in range(i + 1, 10))))
