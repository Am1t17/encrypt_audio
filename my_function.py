from scipy.io.wavfile import read as wavread
import  numpy as np
import sys
my_secret = [1,5,2,6,12,3,7,1,2,8]



def to_bit(data):

    """
    :param data: audio
    :return: list of 2 last bits for audio
    """
    l = []
    for i in range(len(data)):
        l.append(data[i] & 3)
    return l

def reset_bit(data,size):
    """
    :param data: audoi as mono
    :param size: len for bits
    :return: audio cleaned by 2 last bits for size time
    """
    new = data.copy()
    for i in range(size):
        new[i] = (new[i] >> 2) << 2
    return new

def char_to_bits(char):
    """
    :param char:
    :return: list of 4 numbers contains values of 0-3
    """
    l_bit_wise = []
    for _ in range(4):
        l_bit_wise.append(char & 3)
        char >>=2
    return l_bit_wise

def add_pass(string):
    new_string = ""
    for i in range(len(string)):
        new_string += chr(ord(string[i])+my_secret[i%len(my_secret)]) 
    return new_string

def min_pass(string):

    new_string = ""
    for i in range(len(string)):
        new_string += chr(ord(string[i])-my_secret[i%len(my_secret)]) 
    return new_string

def bit_to_char(l):
    num = 0
    for i in range(4):
        num+=l[i]*(2**(i*2))
    return chr(num)

def string_to_audio(l_string,data):

    lenBits = len(l_string)*4
    minn = min(lenBits,len(data))
    if(lenBits + 4<len(data)):
        new_data = reset_bit(data,minn +4)
    else:
        new_data = reset_bit(data, minn)

    for i in range(int(minn/4)):
        l = char_to_bits(ord(l_string[i]))
        for j in range(4):
            new_data[i*4 + j] +=l[j]
    return new_data


def audio_to_string(data,lenBits):
    l = []
    new_data = to_bit(data)
    for i in range(0,lenBits,4):
        ch = bit_to_char(new_data[i:i+4])
        if(sum(new_data[i:i+4]) == 0):
            return l
        l.append(ch)

    return l



def max_len(data,fs):
    """
    :param data:
    :param fs:
    :return: is mono and max len for each string
    """
    num_of_chanels = str(np.shape(data)).split(",")[1].split(")")[0]
    if(len(num_of_chanels) != 0):
        num_of_chanels = int(num_of_chanels)
    else:
        num_of_chanels = 1
    max_len = len(data)/4
    return num_of_chanels,int(max_len)



