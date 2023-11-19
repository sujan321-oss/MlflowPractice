# import sys 


# alpha=float(sys.argv[1]) if len(sys.argv)>1 else 0.5
# beta=float(sys.argv[2]) if len(sys.argv)>2 else 0.5

# print(alpha,beta)

# import mlflow

# print(mlflow.sklearn)


import mlflow
from urllib.parse import urlparse

print(urlparse(mlflow.get_tracking_uri()).scheme)

# print(mlflow.get_tracking_uri().scheme)
