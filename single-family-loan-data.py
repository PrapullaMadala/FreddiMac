import os

file_list = []
if 'historical_data_2013' in os.listdir('.'):
    for file in os.listdir('historical_data_2013'):
        if file.endswith('.txt'):
            file_list.append(file)
            file_list.sort()
    