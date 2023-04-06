import PySimpleGUI as sg
import numpy as np


def linear_equation_2(a1, b1, z1, a2, b2, z2):
    array1 = np.array([a1, b1, z1], dtype=float)
    array2 = np.array([a2, b2, z2], dtype=float)
    array = (array1/array2)[0]*array2-array1
    y = array[2] / array[1]
    x = (array1[2] - array1[1] * y) / array1[0]
    return x, y


if __name__ == '__main__':
    layout = [[sg.Text('输入两个方程的系数，求解x, y的值')],
              [sg.InputText(size=(2, 1)), sg.Text('x'), sg.Text('+'), sg.InputText(size=(2, 1)), sg.Text('y'),
               sg.Text('='),sg.InputText(size=(4, 1))],
              [sg.InputText(size=(2, 1)), sg.Text('x'), sg.Text('+'), sg.InputText(size=(2, 1)), sg.Text('y'),
               sg.Text('='), sg.InputText(size=(4, 1))],
              [sg.Text(key='output')],
              [sg.Button('求解'), sg.Button('退出')],
              [sg.Text('Design by 邱致诚', font=('宋体', 10), justification='r', key='author')]]



    # 生成窗口
    window = sg.Window('Linear_equation', layout, font=('宋体', 17), default_element_size=(50, 1),
                       element_justification='c', icon=r'D:\code\pycharm\2yuan_w\cover.ico', resizable=True)

    # 消息处理和输入消息接收
    while True:
        event, values = window.read()
        if event in (None, '退出'):
            break
        for i in range(len(values)):
            if values[i] == '':
                flag = 0
                break
            elif not values[i].isdigit():
                flag = -1
                window['output'].update('输入必须为数字')
                break
            else:
                flag = 1

        if flag == 1:
            x, y = linear_equation_2(values[0], values[1], values[2], values[3], values[4], values[5])
            print(f'x={x},y={y}')
            if np.isnan(x) or np.isnan(y):
                window['output'].update('无解')
            else:
                window['output'].update(f' x={x}  y={y}')
        elif flag == 0:
            window['output'].update('输入不能为空')
        else:
            window['output'].update('输入必须为数字')

    window.close()
