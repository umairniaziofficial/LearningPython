import os

script_dir = os.path.dirname(os.path.realpath(__file__))
file_dr = os.path.join(script_dir, "demo.txt")

print(script_dir)

with open(file_dr, "w") as f:
    f.write("Hello World!")
    f.close()
