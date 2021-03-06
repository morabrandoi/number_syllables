import sys
import math
from matplotlib import pyplot as plt

# allows for options of start and end depending how many parameters passed
argv = sys.argv
#creates parameters start, stop, step with defaults, 0, 10000, 1, respectively


if (len(argv)) == 4:
    start = int(argv[1])
    end = int(argv[2])
    step = int(argv[3])
elif len(argv) == 3:
    start = int(argv[1])
    end = int(argv[2])
    step = 1
elif len(argv) == 2:
    start = 0
    end = int(argv[1])
    step = 1
else:
    end = 10000
    start = 0
    step = 1


#word dictionaries
places = {5: "trillion ", 4: "billion ", 3: "million ", 2: "thousand ", 1: "", 0: ""}
numbers = {"0":"",
           "1":"one",
           "2":"two",
           "3":"three",
           "4":"four",
           "5":"five",
           "6":"six",
           "7":"seven",
           "8":"eight",
           "9":"nine",
           "10":"ten",
           "11":"eleven",
           "12":"twelve",
           "13":"thirteen",
           "14":"fourteen",
           "15":"fifteen",
           "16":"sixteen",
           "17":"seventeen",
           "18":"eighteen",
           "19": "nineteen",
           "20": "twenty",
           "00": ""}
tens = {"2":"twenty",
        "3":"thirty",
        "4":"fourty",
        "5":"fifty",
        "6":"sixty",
        "7":"seventy",
        "8":"eighty",
        "9":"ninety"}

#syllables dictionaries
syllables = {"": 0,
             " ": 0,
             "zero": 2,
             "one": 1,
             "two": 1,
             "three": 1,
             "four": 1,
             "five": 1,
             "six": 1,
             "seven": 1,
             "eight": 1,
             "nine": 1,
             "ten" : 1,
             "eleven" : 3,
             "twelve":1,
             "thirteen": 2,
             "fourteen":2,
             "fifteen":2,
             "sixteen":2,
             "seventeen":3,
             "eighteen":2,
             "nineteen":2,
             "twenty":2,
             "thirty": 2,
             "fourty": 2,
             "fifty": 2,
             "sixty": 2,
             "seventy":3,
             "eighty": 2,
             "ninety": 2,
             "hundred": 2,
             "thousand":2,
             "million": 2,
             "billion": 2,
             "trillion":2
             }



#initializing range
int_list = range(start,end)
#converting numbers to strings
str_list = [str(x) for x in int_list]


phrase_list = []

# converts block of three number as string to words
def block_to_words(blk):
    word = ""
    if len(blk) == 3:
        if blk[0] != "0":
            word += numbers[blk[0]] + " hundred "



        if int(blk[1:3]) >= 20:
            if blk[2] != "0":
                word += tens[blk[1]] + " " + numbers[blk[2]] + " "
            else:
                word += tens[blk[1]] + " "
        else:
            if blk[1:2] == "0":
                word += numbers[blk[2:3]] + " "
            else:
                word += numbers[blk[1:3]] + " "
    elif len(blk) == 2:
        if int(blk[0:2]) >= 20:
            word += tens[blk[0]] + " " + numbers[blk[1]] + " "
        else:
            word += numbers[blk[0:2]] + " "
    else:
        if blk[0] == "0":
            word += "zero"
        else:
            word += numbers[blk[0]] + " "


    #print(f"word {word}")
    return word


for num in str_list:
    phrase = ""
    num_len = len(num)
    sections = math.ceil(num_len / 3)
    remainder_section_length = ((num_len-1) % 3 ) + 1
    block = num[0: remainder_section_length]

    phrase += block_to_words(block) + places[sections]

    for remaining_sections in range(sections-1):
        start_splice = remainder_section_length + (3 * remaining_sections)
        end_splice = remainder_section_length + (3 * remaining_sections) + 3
        block = num[start_splice:end_splice]

        if block != "000":
            phrase += block_to_words(block) + places[sections - 1 - remaining_sections]

    phrase_list.append(phrase)
# At this point phrase_list has all numbers in range as word form

syllable_list = []
for number in phrase_list:
    sum = 0
    number = number.split()
    for word in number:
        sum += syllables[word]
    syllable_list.append(sum)

# at this point syllable list has syllables for every word in range


bar_graph = plt.bar(int_list, syllable_list)
plt.show()
