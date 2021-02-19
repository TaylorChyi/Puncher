# -*- coding: utf-8 -*-
# @Time : 2021/2/19 4:47 下午
# @Author : Qi Tian yue
# @Github : Orange-66
# @PROJECT : Puncher 
# @File : installer.py
# @Remark : 
# -----------------------------
# -*- coding: utf-8 -*-
# @Time : 2021/1/24 11:19 下午
# @Author : Qi Tianyue
# @Github : Orange-66
# @PROJECT : LAPS
# @File : tool_trans.py
# @Remark : 转换格式类型的工具类
# -----------------------------
import os

# 将此PyQT项目转换成exe文件
def project_to_exe(project_name="puncher"):
    # 打包项目
    cmd = 'pyinstaller -F -w ' \
          '-i ../../Resource/Images/Icon/win_logo.ico ' \
          '../main.py ' \
          '--workpath ./EXE/ ' \
          '--specpath ./EXE/ ' \
          '--distpath ./EXE/ ' \
          '--name {project_name} ' \
          '--clean '.format(project_name=project_name)

    os.system(cmd)

    # 删除spec文件
    root_dir = "./EXE/"
    spec_filename = project_name + ".spec"
    if os.path.exists(os.path.join(root_dir, spec_filename)):
        os.remove(os.path.join(root_dir, spec_filename))
    else:
        print(f'没有找到 [{os.path.join(root_dir, spec_filename)}] 文件或文件夹')

    # 删除workspace文件夹
    root_dir = "./EXE/LAPS/"
    if os.path.exists(root_dir):
        files = os.listdir(root_dir)
        for filename in files:
            if os.path.exists(os.path.join(root_dir, filename)):
                os.remove(os.path.join(root_dir, filename))

        os.rmdir(root_dir)
    else:
        print(f'没有找到 [{root_dir}] 文件或文件夹')


# 程序的主入口
if __name__ == "__main__":
    project_to_exe()
