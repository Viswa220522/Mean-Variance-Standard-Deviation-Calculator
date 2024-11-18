import numpy as np

def calculate(list):
    if len(list)!=9:
        raise ValueError("List must contain nine numbers.")


    nine_arr=np.array(list).reshape(3,3)
    calculations={
    'mean':[np.mean(nine_arr,axis=0).tolist(),np.mean(nine_arr,axis=1).tolist(),np.mean(list)],
    'variance':[np.var(nine_arr,axis=0).tolist(),np.var(nine_arr,axis=1).tolist(),np.var(list)],
    'standard deviation':[np.std(nine_arr,axis=0).tolist(),np.std(nine_arr,axis=1).tolist(),np.std(list)],
    'max':[np.max(nine_arr,axis=0).tolist(),np.max(nine_arr,axis=1).tolist(),np.max(list)],
    'min':[np.min(nine_arr,axis=0).tolist(),np.min(nine_arr,axis=1).tolist(),np.min(list)],
    'sum':[np.sum(nine_arr,axis=0).tolist(),np.sum(nine_arr,axis=1).tolist(),np.sum(list)]
    }
    return calculations