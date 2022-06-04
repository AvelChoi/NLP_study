import numpy as np

vec = np.array([1, 2, 3, 4, 5])
print(vec)

mat = np.array([[10, 20, 30], [60, 70, 80]])
print(mat)

print(type(vec), type(mat))

# ndim은 축의 개수 출력, shape는 크기 출력
print(vec.ndim, vec.shape)
print(mat.ndim, mat.shape)

# 모든 값이 0인 2 * 3 배열 생성
zero_mat = np.zeros((2, 3))
print(zero_mat)

one_mat = np.ones((2, 3))
print(one_mat)

# np.full은 사용자가 지정한 값 삽입
same_value_mat = np.full((2, 2), 7)
print(same_value_mat)

# 임의의 값으로 채워진 배열
radnom_mat = np.random.random((2, 2))
print(radnom_mat)

print('-' * 25)

# np.arange(n) 0부터 n-1 까지의 값을 가지는 배열
range_vec = np.arange(10)
print(range_vec)

n = 2
range_n_step_vec = np.arange(1, 10, n)
print(range_n_step_vec)

# np.reshape() 내부의 값을 변경하지 않으면서 배열 구조 바꾸기
reshape_mat = np.array(np.arange(30)).reshape((5, 6))
print(reshape_mat)

mat = np.array([[1, 2, 3], [4, 5, 6]])
print(mat)

# 슬라이싱
# 첫번째 행 출력
slicing_mat = mat[0, :]
print(slicing_mat)

slicing_mat = mat[:, 1]
print(slicing_mat)

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

# numpy 연산
# np.add
# np.subtract
# np.mulitply


