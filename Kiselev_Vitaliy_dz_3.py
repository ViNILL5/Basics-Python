import os
import shutil


dir_ = os.path.abspath(os.curdir)
print(dir_)

shutil.copytree('my_project/', 'templates', dirs_exist_ok=True)