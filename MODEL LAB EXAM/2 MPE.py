w1 = 0
w2 = 0
bias = 0
lr = 0.1
x = [[0,0], [0,1], [1,0], [1,1]]
y = [0, 0, 0, 1]
for i in range(10):
    for j in range(4):
        s = w1*x[j][0] + w2*x[j][1] + bias
        output = 1 if s > 0 else 0
        error = y[j] - output
        w1 = w1 + lr*error*x[j][0]
        w2 = w2 + lr*error*x[j][1]
        bias = bias + lr*error
    print("Weights:", w1, w2, "Bias:", bias)
print("AND Gate Output:")
for a, b in x:
    s = w1*a + w2*b + bias
    output = 1 if s > 0 else 0
    print(a, b, "=", output)
