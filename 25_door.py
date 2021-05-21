#test
# pub_a = 5764801
# pub_b = 17807724


#actual
pub_a = 18499292
pub_b = 8790390



def transform(subject, loop):
    value = 1

    for i in range(loop):
        value = value * subject
        value = value % 20201227

    return value

value = 1
loop = 1

breakpoint()

while True:
    if loop % 10000 == 0:
        print(loop)
    value = value * 7
    value = value % 20201227

    if value in (pub_a,pub_b):
        print(loop, value)
        break

    loop += 1
