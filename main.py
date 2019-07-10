from time import sleep

from data import text

BLANK = '　'
WIDTH = len(text[0])
HEIGHT = len(text)
LEFT = 0
RIGHT = 1
cache = text


# 在左对齐或右对齐中给字符串填充
def fill_string(string, direction):
    padding = BLANK * (WIDTH - len(string))
    if direction == LEFT:
        return padding + string
    else:
        return string + padding


# 字符串向左或者向右漂移
def shift(text, direction, offset):
    over = offset - WIDTH
    if direction == LEFT:
        if over > 0:
            sub = text[over:]
            return fill_string(sub, RIGHT)
        else:
            sub = text[:offset]
            return fill_string(sub, LEFT)
    else:
        if over > 0:
            sub = text[:WIDTH-over]
            return fill_string(sub, LEFT)
        else:
            sub = text[-offset:]
            return fill_string(sub, RIGHT)


# 第一个倒计时动画
def ready_to_start():
    from data import three, two, one, full
    for frame in [three, two, one]:
        yield frame
        sleep(1)
        yield text
        sleep(0.1)


# 第二个闪闪光光的展示毕业了的动画
def flash_text():
    from data import banner
    for t in range(1, 6):
        width = WIDTH * 2
        speed = 0.001 * t * 1.1
        if t == 5:
            width = WIDTH
            speed = 0.02
        for i in range(1, width + 1):
            sleep(speed)
            frame = []
            for row in range(HEIGHT):
                frame.append(shift(banner[row], row % 2, i))
            yield frame


# 第三个滚屏的动画
def scroll_text():
    from data import saying, full
    # yield text
    sleep(1)
    for i in range(HEIGHT):
        text[i] = cache[i] + full[i]
    for i in range(WIDTH + 1):
        sleep(0.01)
        frame = []
        for row in range(HEIGHT):
            frame.append(text[row][i:i+WIDTH])
        yield frame
    for i in range(HEIGHT):
        if BLANK * WIDTH == saying[i]:
            continue
        for j in range(1, WIDTH + 1):
            sleep(0.03)
            frame[i] = shift(saying[i], LEFT, j)
            yield frame


# 演示每个动画并加上外框的装饰
def show(animals):
    from os import system
    global cache
    for animal in animals:
        for frame in animal():
            system('clear')
            print('————龙影的原创小动画：（程序和数据各仅100行！凭空开始做起！只用os,time模块！）————')
            for row in frame:
                print(f'|{row}|')
            print('——' * (WIDTH + 1))
            cache = frame


# 开始运行播放一系列动画
show([ready_to_start, flash_text, scroll_text])
