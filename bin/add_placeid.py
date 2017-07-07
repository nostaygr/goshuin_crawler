# -*- coding: utf-8 -*-

import glob


def read_files(path):
    files_path = glob.glob(path)
    lst = []
    for file_path in files_path:
        with open(file_path, 'r') as f:
            for line in f:
                lst.append(line.rstrip().split(','))
    return lst


def read_rank_file(path):
    dic = {}
    with open(path, 'r') as f:
        for line in f:
            item = line.rstrip().split(',')
            dic[item[1]] = item[0]
    return dic


def replace_rank(worship_lst, rank_dic):
    for idx, worship in enumerate(worship_lst):
        if worship[0] in rank_dic:
            worship_lst[idx][6] = rank_dic[worship[0]]
    return worship_lst


def add_placeid(shrines_lst, temples_lst):
    place_id = 1
    for idx, shrine in enumerate(shrines_lst):
        shrines_lst[idx].insert(0, str(place_id))
        place_id += 1
    for idx, temple in enumerate(temples_lst):
        temples_lst[idx].insert(0, str(place_id))
        place_id += 1


def main():
    shrines_lst = read_files('res/shrines_*')
    temples_lst = read_files('res/temples_*')

    rank_dic = read_rank_file('res/rank_shrines')
    shrines_lst = replace_rank(shrines_lst, rank_dic)

    add_placeid(shrines_lst, temples_lst)
    output_fn = 'res/worship_place'
    with open(output_fn, 'w') as f:
        for shrine in shrines_lst:
            f.write('{0}\n'.format(
                ','.join([str(i) if i != "" else "" for i in shrine[0:7]])
            ))
        for temples in temples_lst:
            f.write('{0}\n'.format(
                ','.join([str(i) if i != "" else "" for i in temples[0:7]])
            ))

    output_fn = 'res/shrines'
    with open(output_fn, 'w') as f:
        for shrine in shrines_lst:
            f.write('{0},{1},{2}\n'.format(
                shrine[0],
                shrine[7],
                shrine[8]
            ))
    
    output_fn = 'res/temples'
    with open(output_fn, 'w') as f:
        for temple in temples_lst:
            f.write('{0},{1},{2},{3}\n'.format(
                temple[0],
                temple[7],
                temple[8],
                temple[9]
            ))


if __name__ == '__main__':
    main()
