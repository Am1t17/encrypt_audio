import numpy as np
import my_function
import soundfile as sf
import sys

def mono_case_decrypt(audio_data):
    len_bits = len(audio_data) - len(audio_data) % 4
    l = my_function.audio_to_string(audio_data, len_bits)
    new_string = ""
    for i in range(len(l)):
        new_string += l[i]
    return new_string


def N_case_decrypt(audio2_data,n_channels):
    if(n_channels == 1):
        temp = mono_case_decrypt(audio2_data)
        temp = my_function.min_pass(temp)

        return temp
    else:
        temp = mono_case_decrypt(audio2_data[:, 0])
    my_string = temp
    i = 1
    try:
        while(len(temp)*4 == len(audio2_data) -len(audio2_data)% 4):
            print(temp)
            temp = mono_case_decrypt(audio2_data[:, i])
            my_string += temp
            i+=1
    except:
        print("string too long!")
        my_string = my_function.min_pass(my_string)

        return my_string
    my_string = my_function.min_pass(my_string)
    return my_string




if __name__ == "__main__":
    if len(sys.argv != 2):
        exit()
    path = sys.argv[1]
    data,fs = sf.read(path,dtype="int16")
    n_channels, len_data = my_function.max_len(data, fs)
    new_data = N_case_decrypt(data,n_channels)
    print(new_data)






