#!/usr/bin/env python3
import sys

def Hours(sec):
    try:
        s = int(sec)
        if s < 0:
            raise ValueError("请输入整数做为参数！")
        h = s // 60
        s = s % 60
        print("{} H, {} M".format(h,s))
    except:
        print("Parameter Error")

Hours(sys.argv[1])
