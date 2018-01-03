# -*- coding: utf-8 -*-

import os

'''
作者：liuhuisen
'''


def pcap_to_csv_bat_generator(folder_path):
    # 将Windows路径格式更改成Python路径格式
    folder_path = '/'.join(folder_path.split('\\'))
    if folder_path[len(folder_path) - 1] != '/':
        folder_path += '/'

    # 创建存储csv文件的目录
    if not os.path.exists(folder_path + 'sample_traffic_csv'):
        os.mkdir(folder_path + 'sample_traffic_csv/')

    # 提取目标字段至csv文件
    file_list = os.listdir(folder_path + 'sample_traffic_pcap/')
    bat_file = open('pcap_to_csv.bat', 'w')
    bat_file.write('@echo off')
    bat_file.write('\n')
    for file_name in file_list:
        bat_file.write(
            'tshark -r ' + folder_path + 'sample_traffic_pcap/' + file_name + ' -Y "(ip)&&(tcp)" -T fields -e _ws.col.No. -e _ws.col.Time -e _ws.col.Source -e _ws.col.Destination -e _ws.col.Protocol -e _ws.col.Length -e _ws.col.Info -E header=y -E separator=, -E quote=d -E occurrence=f > ' + folder_path + 'sample_traffic_csv/' +
            file_name.split('.')[0] + '.csv')
        bat_file.write('\n')
        bat_file.write('pause')
        bat_file.write('\n')
    bat_file.close()


if __name__ == '__main__':
    folder_path = raw_input('输入商品的根目录：')
    pcap_to_csv_bat_generator(folder_path)
