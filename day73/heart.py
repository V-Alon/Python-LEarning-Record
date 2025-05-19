import turtle


def draw_heart():
    # 设置画笔
    t = turtle.Turtle()
    t.speed(10)  # 设置画笔速度（1-10，1最慢，10最快）
    t.color('red', 'pink')  # 画笔颜色（轮廓色，填充色）

    # 开始填充
    t.begin_fill()

    # 绘制心形的左半部分
    t.left(140)
    t.forward(113)

    # 绘制心形的曲线部分（两个半圆）
    for _ in range(200):
        t.right(1)
        t.forward(1)

    # 调整角度绘制右半部分
    t.left(120)

    # 绘制右半部分的曲线（与左半部分对称）
    for _ in range(200):
        t.right(1)
        t.forward(1)

    t.forward(112)  # 闭合心形

    # 结束填充
    t.end_fill()

    # 隐藏画笔
    t.hideturtle()


# 执行绘制
draw_heart()

# 保持窗口显示
turtle.done()