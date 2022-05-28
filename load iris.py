# Basic Machine Learning

from sklearn.datasets import load_iris
iris = load_iris()

x = iris.data
y = iris.target

print('x.shape =', x.shape)
print('y.shape =', y.shape)

# x.shape = (150, 4)
# y.shape = (150,)
