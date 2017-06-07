# -*- coding: utf-8 -*-

import glob


def read_files(path):
    files_path = glob.glob(path)
    lst = []
    for file_path in files_path:
        with open(file_path, 'r') as f:
            for line in f:
                lst.append(line.rstrip())
    return lst


def add_placeid(shrines_lst, temples_lst):
    place_id = 1
    for idx, shrine in enumerate(shrines_lst):
        shrines_lst[idx] = str(place_id) + ',' + shrine
        place_id += 1
    for idx, temple in enumerate(temples_lst):
        temples_lst[idx] = str(place_id) + ',' + temple
        place_id += 1


def main():
    shrines_lst = read_files('res/shrines_*')
    temples_lst = read_files('res/temples_*')

    output_fn = 'res/worship_place'
    add_placeid(shrines_lst, temples_lst)
    with open(output_fn, 'w') as f:
        for shrine in shrines_lst:
            f.write('{0}\n'.format(
                ','.join([str(i) if i != "" else "" for i in shrine.split(',')[0:7]])
            ))
        for temples in temples_lst:
            f.write('{0}\n'.format(
                ','.join([str(i) for i in temples.split(',')[0:7]])
            ))

    output_fn = 'res/shrines'
    with open(output_fn, 'w') as f:
        for shrine in shrines_lst:
            f.write('{0},{1},{2}\n'.format(
                shrine.split(',', -1)[0],
                shrine.split(',', -1)[7],
                shrine.split(',', -1)[8]
            ))
    
    output_fn = 'res/temples'
    with open(output_fn, 'w') as f:
        for temple in temples_lst:
            f.write('{0},{1},{2},{3}\n'.format(
                temple.split(',', -1)[0],
                temple.split(',', -1)[7],
                temple.split(',', -1)[8],
                temple.split(',', -1)[9]
            ))


if __name__ == '__main__':
    main()
