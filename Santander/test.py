import pandas as pd
from timeit import default_timer as timer
start = timer()
trn = pd.read_csv("./Data/train_ver2.csv")
test = pd.read_csv("./Data/test_ver2.csv")

print('end : ', timer() - start)