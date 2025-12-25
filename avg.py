import numpy as np
marks=[8,7,6,2,10,2,3,5,3]
m=np.array(marks)
print(m)
print("top:",np.max(m))
print("avg: ",np.mean(m))
print("low: ",np.min(m))
print("sd: ",np.std(m))
value=np.mean(m)
result = np.where(
    value> 5, "above average",
    np.where(value < 5, "below average", "average")
)
print(result)


