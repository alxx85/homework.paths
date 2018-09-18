import glob
import os.path
import subprocess

resource = 'Source'
result = 'Result'
path_dir = os.path.dirname(__file__)

files = glob.glob(os.path.join(resource, "*.jpg"))

if os.path.exists('Result') == False:
  os.mkdir('Result')

for file in files:
  out_list = os.path.split(file)
  if resource in out_list:
    out_file = file[len(resource) + 1:]
  string_run = 'convert ' + os.path.join(path_dir, file) + ' -resize 200 ' + os.path.join(path_dir, os.path.join(result, out_file))
  print(string_run)
  subprocess.run(string_run, shell = True)
