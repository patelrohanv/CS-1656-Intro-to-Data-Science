#!/usr/bin/python3

import argparse
import collections
import csv
import glob
import itertools
import math 
import os
import pandas
import re
import string
import sys

#main function, takes in input python3 apriori.py input_filename output_filename min_support_percentage min_confidence
def main():
#file that contains market basket data that is the input to your program
#transaction_id, item_1, item_2, item_3,
    input_filename = sys.argv[1]
#should contain the frequent item sets and the association rules that you discovered
#set, support_percentage, item_1, item_2, item_3,
    output_filename = sys.argv[2]
#minimum support percentage for an itemset / association rule to be considered frequent
    min_support_percentage = float(sys.argv[3])
#the minimum confidence for an association rule to be significant
    min_confidence = float(sys.argv[4])

#generate all possible combinations per transaction
    pair_dict = {} #string -> count
    supp_dict = {} #string -> support
    row_count = 0
    input_file = open(input_filename)
    input_csv = csv.reader(input_file)
    for row in input_csv:
        input_list = list(row)
        #remove transaction_id
        input_list.pop(0)
        #convert list of items to single string
        input_list = ''.join(input_list)
        list_len = len(input_list)
        for x in range(1, list_len + 1):
            power_set = list(itertools.combinations(input_list, x))
            for y in power_set:
        #convert each subset into single string
                y = ''.join(y)
                if y not in pair_dict:
                    pair_dict[y] = 1
                else:
                    pair_dict[y] = pair_dict[y] + 1
        row_count = row_count + 1

#calculate each element's support and add to supp_dict
    remove = []
    for element in pair_dict:
        support = pair_dict[element]/row_count
        if support >= min_support_percentage:
            supp_dict[element] = support
        else:
            remove.append(element)
    for element in remove:
        del pair_dict[element]

    supportList = []
    for element in supp_dict:
        elementList = list(element)
        strSupp = supp_dict[element]
        strn = "set," + str(strSupp) + ","
        for c in elementList:
            strn = strn + c + ","
        strn = strn[:-1]
        supportList.append(strn)

#finding rules based on confidence
    confidenceList = []
    for element in pair_dict:
        listElement = list(element)
        #loop from up to the string's length
        if len(listElement) == 2:
            str0 = listElement[0]
            str1 = listElement[1]
            str01 = str0 + str1
            # 0 -> 1
            # 01/0
            if pair_dict[str01]/pair_dict[str0] >= min_confidence:
                strn = "rule," + str(supp_dict[element])
                strn = strn + "," + str(pair_dict[str01]/pair_dict[str0])
                strn = strn + "," + str0 + "\'=>\'" + str1
                if strn not in confidenceList:
                    confidenceList.append(strn)
            # 1 -> 0
            # 01/1
            if pair_dict[str01]/pair_dict[str1] >= min_confidence:
                strn = "rule," + str(supp_dict[element])
                strn = strn + "," + str(pair_dict[str01]/pair_dict[str1])
                strn = strn + "," + str1 + "\'=>\'" + str0
                if strn not in confidenceList:
                    confidenceList.append(strn)

        if len(listElement) == 3:
            str0 = listElement[0]
            str1 = listElement[1]
            str2 = listElement[2]
            str01 = str0 + str1
            str02 = str0 + str2
            str12 = str1 + str2
            str012 = str01 + str2
            # 0 -> 12
            if pair_dict[str012]/pair_dict[str0] >= min_confidence:
                strn = "rule," + str(supp_dict[element])
                strn = strn + "," + str(pair_dict[str012]/pair_dict[str0])
                strn = strn + "," + str0 + "\'=>\'" + str12
                if strn not in confidenceList:
                    confidenceList.append(strn)
            # 1 -> 02
            if pair_dict[str012]/pair_dict[str1] >= min_confidence:
                strn = "rule," + str(supp_dict[element])
                strn = strn + "," + str(pair_dict[str012]/pair_dict[str1])
                strn = strn + "," + str1 + "\'=>\'" + str02
                if strn not in confidenceList:
                    confidenceList.append(strn)
            # 2 -> 01
            if pair_dict[str012]/pair_dict[str2] >= min_confidence:
                strn = "rule," + str(supp_dict[element])
                strn = strn + "," + str(pair_dict[str012]/pair_dict[str2])
                strn = strn + "," + str2 + "\'=>\'" + str01
                if strn not in confidenceList:
                    confidenceList.append(strn)
            # 12 -> 0
            if pair_dict[str012]/pair_dict[str12] >= min_confidence:
                strn = "rule," + str(supp_dict[element])
                strn = strn + "," + str(pair_dict[str012]/pair_dict[str12])
                strn = strn + "," + str12 + "\'=>\'" + str0
                if strn not in confidenceList:
                    confidenceList.append(strn)
            # 02 -> 1
            if pair_dict[str012]/pair_dict[str02] >= min_confidence:
                strn = "rule," + str(supp_dict[element])
                strn = strn + "," + str(pair_dict[str012]/pair_dict[str02])
                strn = strn + "," + str02 + "\'=>\'" + str1
                if strn not in confidenceList:
                    confidenceList.append(strn)
            # 01 -> 2
            if pair_dict[str012]/pair_dict[str01] >= min_confidence:
                strn = "rule," + str(supp_dict[element])
                strn = strn + "," + str(pair_dict[str012]/pair_dict[str01])
                strn = strn + "," + str01 + "\'=>\'" + str2
                if strn not in confidenceList:
                    confidenceList.append(strn)

        if len(listElement) == 4:
            str0 = listElement[0]
            str1 = listElement[1]
            str2 = listElement[2]
            str3 = listElement[3]
            str01 = str0 + str1
            str02 = str0 + str2
            str03 = str0 + str3
            str12 = str1 + str2
            str13 = str1 + str3
            str23 = str2 + str3
            str012 = str01 + str2
            str013 = str01 + str3
            str023 = str02 + str3
            str123 = str12 + str3
            str0123 = str01 + str23
            # 0 -> 123
            if pair_dict[str0123]/pair_dict[str0] >= min_confidence:
                strn = "rule," + str(supp_dict[element])
                strn = strn + "," + str(pair_dict[str0123]/pair_dict[str0])
                strn = strn + "," + str0 + "\'=>\'" + str123
                if strn not in confidenceList:
                    confidenceList.append(strn)
            # 1 -> 023
            if pair_dict[str0123]/pair_dict[str1] >= min_confidence:
                strn = "rule," + str(supp_dict[element])
                strn = strn + "," + str(pair_dict[str0123]/pair_dict[str023])
                strn = strn + "," + str1 + "\'=>\'" + str023
                if strn not in confidenceList:
                    confidenceList.append(strn)
            # 2 -> 013
            if pair_dict[str0123]/pair_dict[str2] >= min_confidence:
                strn = "rule," + str(supp_dict[element])
                strn = strn + "," + str(pair_dict[str0123]/pair_dict[str2])
                strn = strn + "," + str2 + "\'=>\'" + str013
                if strn not in confidenceList:
                    confidenceList.append(strn)
            # 3 -> 012
            if pair_dict[str0123]/pair_dict[str3] >= min_confidence:
                strn = "rule," + str(supp_dict[element])
                strn = strn + "," + str(pair_dict[str0123]/pair_dict[str3])
                strn = strn + "," + str3 + "\'=>\'" + str012
                if strn not in confidenceList:
                    confidenceList.append(strn)
            # 01 -> 23
            if pair_dict[str0123]/pair_dict[str01] >= min_confidence:
                strn = "rule," + str(supp_dict[element])
                strn = strn + "," + str(pair_dict[str0123]/pair_dict[str01])
                strn = strn + "," + str01 + "\'=>\'" + str23
                if strn not in confidenceList:
                    confidenceList.append(strn)
            # 02 -> 13
            if pair_dict[str0123]/pair_dict[str02] >= min_confidence:
                strn = "rule," + str(supp_dict[element])
                strn = strn + "," + str(pair_dict[str0123]/pair_dict[str02])
                strn = strn + "," + str02 + "\'=>\'" + str13
                if strn not in confidenceList:
                    confidenceList.append(strn)
            # 03 -> 12
            if pair_dict[str0123]/pair_dict[str03] >= min_confidence:
                strn = "rule," + str(supp_dict[element])
                strn = strn + "," +str(pair_dict[str0123]/pair_dict[str03])
                strn = strn + "," + str03 + "\'=>\'" + str12
                if strn not in confidenceList:
                    confidenceList.append(strn)
            # 23 -> 01
            if pair_dict[str0123]/pair_dict[str23] >= min_confidence:
                strn = "rule," + str(supp_dict[element])
                strn = strn + "," + str(pair_dict[str0123]/pair_dict[str23])
                strn = strn + "," + str23 + "\'=>\'" + str01
                if strn not in confidenceList:
                    confidenceList.append(strn)
            # 13 -> 02
            if pair_dict[str0123]/pair_dict[str13] >= min_confidence:
                strn = "rule," + str(supp_dict[element])
                strn = strn + "," + str(pair_dict[str0123]/pair_dict[str13])
                strn = strn + "," + str2 + "\'=>\'" + str01
                if strn not in confidenceList:
                    confidenceList.append(strn)
            # 12 -> 03
            if pair_dict[str0123]/pair_dict[str12] >= min_confidence:
                strn = "rule," + str(supp_dict[element])
                strn = strn + "," + str(pair_dict[str0123]/pair_dict[str12])
                strn = strn + "," + str12 + "\'=>\'" + str03
                if strn not in confidenceList:
                    confidenceList.append(strn)
            # 123 -> 0
            if pair_dict[str0123]/pair_dict[str123] >= min_confidence:
                strn = "rule," + str(supp_dict[element])
                strn = strn + "," + str(pair_dict[str0123]/pair_dict[str123])
                strn = strn + "," + str123 + "\'=>\'" + str0
                if strn not in confidenceList:
                    confidenceList.append(strn)
            # 023 -> 1
            if pair_dict[str0123]/pair_dict[str023] >= min_confidence:
                strn = "rule," + str(supp_dict[element])
                strn = strn + "," + str(pair_dict[str0123]/pair_dict[str023])
                strn = strn + "," + str023 + "\'=>\'" + str1
                if strn not in confidenceList:
                    confidenceList.append(strn)
            # 013 -> 2
            if pair_dict[str0123]/pair_dict[str013] >= min_confidence:
                strn = "rule," + str(supp_dict[element])
                strn = strn + "," + str(pair_dict[str0123]/pair_dict[str013])
                strn = strn + "," + str013 + "\'=>\'" + str2
                if strn not in confidenceList:
                    confidenceList.append(strn)
            # 012 -> 3
            if pair_dict[str0123]/pair_dict[str012] >= min_confidence:
                strn = "rule," + str(supp_dict[element])
                strn = strn + "," + str(pair_dict[str0123]/pair_dict[str012])
                strn = strn + "," + str012 + "\'=>\'" + str3
                if strn not in confidenceList:
                    confidenceList.append(strn)

    with open(output_filename, 'w+') as out:
        for s in supportList:
            out.write(s + "\n")
        for s in confidenceList:
            out.write(s + "\n")
        
#calls main at start of program
if __name__ == "__main__": main()