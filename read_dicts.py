from dict_2015 import dict_2015
from dict_2016 import dict_2016
from dict_2017 import dict_2017
from dict_2018 import dict_2018
from dict_2019 import dict_2019
from dict_2018 import dict_2018

for i, dictionary in enumerate([dict_2015,dict_2016,dict_2017,dict_2018,dict_2019 ]):
    for key in dict_2018.keys():
        print(f'\n\n {i} ----------------------------{key}')
        if key in dictionary.keys():
            print(f'key found: {key}')
            lv1_2020 =  dict_2018[key]
            if 'columns' in lv1_2020.keys():
                elements2020 = dict_2018[key]['columns']
                elementsDictionary= dictionary[key]['columns']
                in2020 = [x for x in elements2020 if x not in elementsDictionary]
                inDict =  [x for x in elementsDictionary if x not in elements2020]
                print(f'\tin2020: {in2020}')
                print(f'\tinDict: {inDict}')

        else:
            print(f'key not found: {key}')
            