


import sys
import os
import time






"""生成目录列表中的某一项"""
def creat_directory_line(line, headline_mark, file_path):
    if headline_mark == '#':
        file_path_new = './' + '/'.join(file_path.split('/')[-2:])
        #print(' #### file_path_new: ', file_path_new)
        return '- [' + line[2:-1] + '](' + file_path_new +')' 
    elif headline_mark == '##':
        return '  - ' + line[3:-1]
    elif headline_mark == '###':
        return '    - ' + line[4:-1]
    elif headline_mark == '####':
        return '      - ' + line[5:-1]
    elif headline_mark == '#####':
        return '        - ' + line[6:-1]
    elif headline_mark == '######':
        return '          - ' + line[7:-1]


"""生成目录列表"""
def creat_directory(file_path):
    headline = ['#','##','###','####','#####','######']

    with open(file_path,'r',encoding='utf-8') as f:
        lines_in_file = []
        for line in f:
            lines_in_file.append(line)
        f.close()

        directory = []
        flag_code = 0
        length = len(lines_in_file)
        for j in range(length):
            line = lines_in_file[j]
            if line[:3] == '```' :
                if flag_code == 0: flag_code = 1
                else: flag_code = 0
                continue

            if flag_code ==1: continue

            splitedline = line.lstrip().split(' ')
            if splitedline[0] in headline:
                #如果为最后一行且末尾无换行（防最后一个字被去除）
                if j == length - 1 and line[-1] != '\n':
                    directory.append(creat_directory_line(line + '\n', splitedline[0], file_path) )
                else:
                    directory.append(creat_directory_line(line, splitedline[0], file_path) )
    return directory


"""以目录列表为参数生成添加目录的文件"""
def creat_file_with_toc(file_path):

    lines_start = [' ',
                 '----------------------------------------']

    lines_sub = creat_directory(file_path)
    lines_sub = lines_start + lines_sub

    lines_sub.append(' ')
    lines_sub.append(' ')

    return lines_sub

def process(folder, save_path):


    def write_md(save_path, lines):
        with open(save_path, 'w',encoding='utf-8') as f:
            for line in lines:
                f.write(line + '\n')


    lines = [ '# Python',
              'python notebook, version: python3+',
              '',
              '**目录：**']



    for file1 in os.listdir(folder):
        print(' #### file1: ', file1)

        if file1.split('.')[-1].lower() not in ['md','mdown','markdown'] : continue 

        file_path = folder + '/' + file1
        lines_sub = creat_file_with_toc(file_path)
        lines = lines + lines_sub

        #break

    
    write_md(save_path, lines)
    


if __name__=='__main__':
    dir_cur = 'D:/_code/github/Python'
    filename = 'Python'

    folder = dir_cur + '/' +  filename
    save_path = dir_cur + '/README.md'
    process(folder, save_path)






