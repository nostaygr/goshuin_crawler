# -*- coding: utf-8 -*-

import glob


def read_files(path):
    files_path = glob.glob(path)
    list = []
    for file_path in files_path:
        with open(file_path, 'r') as f:
            for line in f:
                list.append(line.rstrip().split(','))
    return list


def read_rank_file(path):
    dict = {}
    with open(path, 'r') as f:
        for line in f:
            item = line.rstrip().split(',')
            dict[item[1]] = item[0]
    return dict


def update_rank(worship_list, rank_dict):
    for idx, worship in enumerate(worship_list):
        if worship[0] in rank_dict:
            worship_list[idx][6] = rank_dict[worship[0]]
    return worship_list


def add_placeid(shrines_list, temples_list):
    place_id = 1
    for idx, shrine in enumerate(shrines_list):
        shrines_list[idx].insert(0, str(place_id))
        place_id += 1
    for idx, temple in enumerate(temples_list):
        temples_list[idx].insert(0, str(place_id))
        place_id += 1


def main():
    shrines_list = read_files('res/shrines_*')
    temples_list = read_files('res/temples_*')

    shrine_rank_dict = read_rank_file('res/rank_shrines')
    shrines_list = update_rank(shrines_list, shrine_rank_dict)

    add_placeid(shrines_list, temples_list)
    output_fn = 'res/worship_place'
    with open(output_fn, 'w') as f:
        for shrine in shrines_list:
            f.write('{0}\n'.format(
                ','.join([str(i) if i != "" else "" for i in shrine[0:7]])
            ))
        for temples in temples_list:
            f.write('{0}\n'.format(
                ','.join([str(i) if i != "" else "" for i in temples[0:7]])
            ))

    output_fn = 'res/shrines'
    with open(output_fn, 'w') as f:
        for shrine in shrines_list:
            f.write('{0},{1},{2}\n'.format(
                shrine[0],
                shrine[7],
                shrine[8]
            ))
    
    output_fn = 'res/temples'
    with open(output_fn, 'w') as f:
        for temple in temples_list:
            f.write('{0},{1},{2},{3}\n'.format(
                temple[0],
                temple[7],
                temple[8],
                temple[9]
            ))


if __name__ == '__main__':
    main()
