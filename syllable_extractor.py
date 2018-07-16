import sys

if len(argv) == 2:
    end = argv[1]
else:
    end = 9999

places = ["billion", "million", "thousand", "hundred"]
numbers = {0:"",
           1:"one",
           2:"two",
           3:"three",
           4:"four",
           5:"five",
           6:"six",
           7:"seven",
           8:"eight",
           9:"nine",
           10:"ten",
           11:"eleven",
           12:"twelve",
           13:"thirteen",
           14:"fourteen",
           15:"fifteen",
           16:"sixteen",
           17:"seventeen",
           18:"eighteen",
           19:"twenty"}
tens = {2:"twenty",
        3:"thirty",
        4:"fourty",
        5:"fifty",
        6:"sixty",
        7:"seventy",
        8:"eighty",
        9:"ninety"}


int_list = range(end)
str_list = [str(x) for x in int_list]

word_list = []


def three_block_to_words(blk):
    phrase = ""
    if len(blk) == 3:
        phrase += numbers[blk[0]] + " hundred "

        if int(blk[1] + blk[2]) >= 20:
            phrase += tens[blk[1]] + " " + numbers[blk[2]] + " "
        else:
            phrase += numbers[int(blk[1] + blk[2])] + " "
    elif len(blk) == 2:
        if int(blk[0] + blk[1]) >= 20:
            phrase += tens[blk[0]] + " " + numbers[blk[1]] + " "
        else:
            phrase += numbers[int(blk[0] + blk[1])] + " "
    else:
        phrase += numbers[blk[0]] + " "



    print("test phrase from function is: " + phrase)
    return phrase


for num in str_list:
    word = ""
    len = len(num)
    start_mod = len % 3
    for l in range(len // 3)
