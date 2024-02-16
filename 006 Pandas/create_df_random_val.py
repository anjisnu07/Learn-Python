#creating a dataframe with random values
import numpy as np
import pandas as pd

# random values b/w 0 to 1
random_df=pd.DataFrame(np.random.rand(20,10)) # 20,10 is size of dataframe
print(random_df.head())



