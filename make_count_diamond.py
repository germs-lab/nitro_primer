#!/usr/bin/python 
"""
This script count how many hit found ; cutoff = 80 percent identity
usage: python make_count_diamond.py mgm4477807.3.fastq.m8 mgm4477807.3.fastq.m8
python make_count_diamond.py *.m8 > count.txt
"""

import sys
import screed

def main():
    cutoff = 80
    
    dict = {}
    for one_file in sys.argv[1:]:

        prev = ""
        for line in open(one_file,'r'):
            spl = line.strip().split('\t')
            if prev == spl[0]:
                continue
            else:
                prev = spl[0]
            if float(spl[2]) > cutoff: 
                dict[spl[1]] = dict.get(spl[1],0) + 1

    for item in dict.items():
        result = [item[0],str(item[1])]
        print '\t'.join(result)

if  __name__ == '__main__':
    main()
