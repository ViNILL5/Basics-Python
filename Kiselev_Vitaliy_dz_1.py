import os
from pathlib import Path


dir_ = os.path.abspath(os.curdir)

my_project_lst = ['setting', 'mainapp', 'adminapp', 'authapp']

for name in my_project_lst[:]:
  p = Path(f'{dir_}/my_project/{name}')
  p.mkdir(parents=True, exist_ok=True)
