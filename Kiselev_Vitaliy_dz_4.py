import os
from pathlib import Path

dir_ = os.path.abspath(os.curdir)
print(dir_)

current_dir = Path('my_project')

sizes = [100, 1000, 10000, 100000]
dict_files = {}
sizes += [float("inf")]
result = dict.fromkeys(sizes, 0)

for path_from_top, subdirs, files in os.walk(current_dir):
  for file in files:
    path = os.path.join(path_from_top, file)
    size = os.path.getsize(path)
    to_group = min(filter(lambda x: size < x, sizes))
    result[to_group] += 1


prev_size = 0
for size in sizes:
  print(f"Файлов размером (байт) до {size:10} : {result[size]}")
  prev_size = size