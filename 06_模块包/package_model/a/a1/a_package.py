import sys
import os

base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
print(base_path)

sys.path.append(base_path)
from a.a2 import a2_package
from b.b1 import b_package
