#!/usr/bin/env python3  # 注释行，可以使脚本在不同操作系统之间具有移植性
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r', newline='') as filereader:   # 在语句结束的时候自动关闭文件对象
    with open(output_file, 'w', newline='') as filewriter:
        header = filereader.read()
        header = header.strip()
        header_list = header.split(',')                 # 去掉header中字符串两端的空格、制表符和换行符
        print(header_list)
        filewriter.write(','.join(map(str, header_list)) + '\n')
        for row in filereader:
            row = row.strip()
            row_list = row.split(',')
            print(row_list)
            filewriter.write(','.join(map(str, row_list)) + '\n')

