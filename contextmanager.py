from contextlib import contextmanager
from time
import re
@contextmanager
def log_file(obj):
    try:
        f=open(obj,"w+")
        f.write(":statt of logs\n")
        yield f
    finally:
        f.write(":end of logs\n")
        f.close()

with log_file("new.txt") as file:
    file.write("main body\n")

print(time.now())