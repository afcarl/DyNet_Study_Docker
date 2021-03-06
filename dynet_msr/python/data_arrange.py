#!/usr/bin/env python

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "."))
from os import path
APP_ROOT = path.dirname( path.abspath( __file__ ) )

class DataArrange():
    """
    """

    def __init__(self, file_name, out_putfile_name):
        self.file_name = file_name
        self.out_put_file_name = out_putfile_name
        self.concept_data = {}

    def interface_data_arrange(self):
        self.__read_document()

    def __read_document(self):
        with open(self.file_name, 'r') as f:
            data_list = f.read().split("\n")
            self.__data_arrange(data_list)

    def __data_arrange(self, data_list):
        for data in data_list:
            split_data = data.split("\t")
            if split_data[0] not in self.concept_data and len(split_data) >= 2:
                value_list = []
                value_list.append(split_data[1])
                self.concept_data.update({split_data[0]:value_list})
            elif len(split_data) >= 2:
                value_list = []
                value_list = self.concept_data[split_data[0]]
                value_list.append(split_data[1])
                self.concept_data.update({split_data[0]:value_list})
        self.__output_file()

    def __output_file(self):
        with open(self.out_put_file_name, 'w') as f:
            for key, value_list in self.concept_data.items():
                for value in value_list:
                    f.write(value + " ||| " + key)
                    f.write("\n")
