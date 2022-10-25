#!/usr/bin/python3
""" Add all arguments to a Python list and save them to a file """
import sys
import json

if __name__ == "__main__":
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv
filename = "add_item.json"
with open(filename, 'a+', encoding="utf-8") as f:
    my_list = []
    my_list.extend(args[1:])
    my_list.extend(sys.argv[1:])
    my_list.append(args[1:])
    my_list.append(sys.argv[1:])
    save_to_json_file(my_list, filename)
    load_from_json_file(filename)
