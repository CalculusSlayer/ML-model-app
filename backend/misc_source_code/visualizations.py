import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_circle(ax, position, color):
    c = patches.Circle(position,1, linewidth=1, color=color, ec="black")
    ax.add_patch(c)
    return c


def connect(ax, start, end):
    p1 = [start[0]+1, start[1]]
    p2 = [end[0]-1, end[1]]
    c = patches.ConnectionPatch(p1, p2, "data")
    ax.add_patch(c)
    return c


def makeline(ax, n, xloc, color="lightblue", brk=False):
    width = 3*(n-1) + 2
    start = 37.5-width/2+1
    print(start)
    points = [(xloc, start+3*x) for x in range(n)]
    if brk:
        sep = (1*n)//3
        points = [(points[i][0], points[i][1] + 3 * (-1 if i <= sep else 1)) for i in range(len(points))]
    for i in points:
        draw_circle(ax, i, color)
    return points


def dnn_visual():
    fig, ax = plt.subplots(figsize=(20, 20))
    ax.set_ylim(0, 75)
    ax.set_xlim(0, 150)

    arr = [makeline(ax, 5, 10, "#AFE1AF")]
    xpos = 20
    row = makeline(ax, 8, xpos, brk=True)
    for a in arr[-1]:
        for b in row:
            connect(ax, a, b)
    arr.append(row)
    xpos += 10
    for _ in range(10):
        row = makeline(ax, 16, xpos, brk=True)
        for a in row:
            for b in arr[-1]:
                connect(ax, b, a)
        arr.append(row)
        xpos += 10
    out = makeline(ax, 1, xpos, "#FF6420")
    for a in arr[-1]:
        connect(ax, a, out[0])

    ax.set_aspect('equal', adjustable='box')
    ax.set_axis_off()
    plt.show()


def ann_visual():
    fig, ax = plt.subplots(figsize=(20, 20))
    ax.set_ylim(0, 75)
    ax.set_xlim(0, 150)


    arr = [makeline(ax, 5, 10, "#AFE1AF")]
    xpos = 20
    row = makeline(ax, 8, xpos, brk=True)
    for a in arr[-1]:
        for b in row:
            connect(ax, a, b)
    arr.append(row)
    xpos += 10
    for _ in range(1):
        row = makeline(ax, 16, xpos, brk=True)
        for a in row:
            for b in arr[-1]:
                connect(ax, b, a)
        arr.append(row)
        xpos += 10
    out = makeline(ax, 1, xpos, "#FF6420")
    for a in arr[-1]:
        connect(ax, a, out[0])

    ax.set_aspect('equal', adjustable='box')
    ax.set_axis_off()
    plt.show()


def perceptron_visual():
    fig, ax = plt.subplots(figsize=(20, 20))
    ax.set_ylim(0, 75)
    ax.set_xlim(0, 150)

    xpos = 20
    arr = [makeline(ax, 5, 10, "#AFE1AF")]
    out = makeline(ax, 1, xpos, "#FF6420")
    for a in arr[-1]:
        connect(ax, a, out[0])

    ax.set_aspect('equal', adjustable='box')
    ax.set_axis_off()
    plt.show()

def main():
    dnn_visual()
    ann_visual()
    perceptron_visual()


if __name__ == '__main__':
    main()