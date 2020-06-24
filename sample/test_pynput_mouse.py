from pynput import mouse


# 控制鼠标

def read_pointer_position():
    """获取光标位置"""
    mc = mouse.Controller()
    print('The current pointer position is {0}'.format(mc.position))


def set_pointer(x, y):
    """设置光标位置"""
    mc = mouse.Controller()
    mc.position = (x, y)
    print('Now we have moved it to {0}'.format(mc.position))


def move_pointer(x, y):
    """相对于当前位置移动"""
    mc = mouse.Controller()
    mc.move(5, -5)
    print('Now we have moved it to {0}'.format(mc.position))


def press_button():
    mc = mouse.Controller()
    mc.press(mouse.Button.left)
    mc.release(mouse.Button.left)

    mc.click(mouse.Button.left, 2)  # 双击
    mc.scroll(0, 2)  # 向下滚动两步


def monitoring():
    """监视鼠标"""

    def on_move(x, y):
        print('Pointer moved to {0}'.format((x, y)))

    def on_click(x, y, button, pressed):
        print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))
        if not pressed:
            # Stop listener
            return False

    def on_scroll(x, y, dx, dy):
        print('Scrolled {0} at {1}'.format('down' if dy < 0 else 'up', (x, y)))

    with mouse.Listener(
            on_move=on_move,
            on_click=on_click,
            on_scroll=on_scroll) as listener:
        listener.join()


if __name__ == "__main__":
    read_pointer_position()
    set_pointer(10, 20)
    move_pointer(105, -105)
    press_button()

    monitoring()
