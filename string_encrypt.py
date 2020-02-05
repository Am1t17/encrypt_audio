import my_function
import soundfile as sf
import sys


def mono_case_encrypt(string_to_enc, audio_data):

    new_data = my_function.string_to_audio(list(string_to_enc), audio_data)
    return new_data


def N_case_encrypt(string_to_enc,audio2_data,N_channels):
    string_to_enc = my_function.add_pass(string_to_enc)
    cpy_data =audio2_data.copy()
    parss = int(len(audio2_data) / 4)

    if(N_channels == 1):
        cpy_data = mono_case_encrypt(string_to_enc, audio2_data)
        return cpy_data
    for i in range(N_channels):
        cpy_data[:int(parss * 4), i] = mono_case_encrypt(string_to_enc[parss*i:parss*(i+1)], audio2_data[:int(parss * 4), i])

    return cpy_data



if __name__ == "__main__":
    if len(sys.argv != 3):
        exit()
    path = sys.argv[1]
    string = sys.argv[2]
    data,fs = sf.read(path,dtype="int16")
    data = data[:20]
    num_of_chanels, len_data = my_function.max_len(data, fs)
    print(string)
    new_data = N_case_encrypt(list(string), data,num_of_chanels)

    sf.write(path.split(".")[0] + "_encrypt" + ".wav",new_data,fs)


