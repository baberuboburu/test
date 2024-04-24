
# # input
# N, X, Y, Z = [int(x) for x in input().split()]
N = 4
X = 5
Y = 3
Z = 2

# 初期値
red = [0] * 10
green = [0] * 10
blue = [0] * 10

red[N-1] = 1


# 操作1(n: 枚数, N: 数字)
def option1(red, green, blue):
  red_indexs = [(index, value) for index, value in enumerate(red) if value != 0]
  red = [0] * 10
  for tuple in red_indexs:
    red_index = tuple[0] - 1
    green_index = tuple[0]
    red[red_index] = tuple[1]
    green[green_index] += tuple[1] * X
  
# option1(red, green, blue)


# 操作2(n: 枚数, N: 数字)
def option2(red, green, blue):
  blue_indexs = [(index, value) for index, value in enumerate(blue) if value != 0]
  blue = [0] * 10
  for tuple in blue_indexs:
    blue_index = tuple[0] - 1
    red_index = tuple[0] - 1
    blue[blue_index] = tuple[1] * Y
    red[red_index] += tuple[1]
  
# option2(red, green, blue)


# 操作3(n: 枚数, N: 数字)
def option3(red, green, blue):
  green_indexs = [(index, value) for index, value in enumerate(green) if value != 0]
  for tuple in green_indexs:
    red_index = tuple[0] - 1
    blue_index = tuple[0] - 2
    blue[blue_index] += tuple[1] * Z
    red[red_index] += tuple[1]

# option3(red, green, blue)


