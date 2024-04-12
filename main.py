# Only integer scalar arrays can be converted to a scalar index

import numpy as np

arr = [0, 1, 2, 3, 4,
       5, 6, 7, 8, 9]

# ✅ Convert the Python list to a NumPy array
arr = np.array(arr)

# 👇️ [0 1 2 3 4 5 6 7 8 9]
print(arr)

print(type(arr))  # 👉️ <class 'numpy.ndarray'>


indices = np.array([0, 2, 3])

print(arr[indices])  # 👉️ [0 2 3]