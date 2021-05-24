import tkinter as tk
import random
import time

show_time = 0
case_num = 0
def record(arrow, star, flag, click_time):
    react_time = click_time - show_time
    global case_num
    case_num += 1
    if star == flag:
        if arrow == '←':
            if (star == 1):
                print('No.'+ str(case_num) + ' case information: \r Cue: ' + 'Valid' + '   | reaction time: ' + str(react_time) + 's')
            else:
                print('No.'+ str(case_num) + ' case information: \r Cue: ' + 'Invalid' + ' | reaction time: ' + str(react_time) + 's')
        elif arrow == '→':
            if (star == 2):
                print('No.'+ str(case_num) + ' case information: \r Cue: ' + 'Valid' + '   | reaction time: ' + str(react_time) + 's')
            else:
                print('No.'+ str(case_num) + ' case information: \r Cue: ' + 'Invalid' + ' | reaction time: ' + str(react_time) + 's')
        else:
            print('No.'+ str(case_num) + ' case information: \r Click at the wrong time!')
    else:
        print('No.'+ str(case_num) + ' case information: \r Click on the error button!')
    clear_window()

def add_arrow():
    flag = random.randint(1,2)
    if (flag == 1):
        arrow_label['text'] = '←'
    elif (flag == 2):
        arrow_label['text'] = '→'
    window.after(500, add_star)

def add_star():
    global show_time
    flag = random.randint(1,2)
    arrow = arrow_label['text']
    arrow_label['text'] = ' '
    left_button['command'] = lambda: record(arrow, 1, flag, time.time())
    right_button['command'] = lambda: record(arrow, 2, flag, time.time())
    if (flag == 1):
        left_button['text'] = ' ★ '
        show_time = time.time()
    elif (flag == 2):
        right_button['text'] = ' ★ '
        show_time = time.time()

def clear_window():
    left_button['text'] = '     '
    right_button['text'] = '     '
    left_button['command'] = ''
    right_button['command'] = ''
    window.after(1000, add_arrow)

def A_click(self):
    left_button.invoke()

def D_click(self):
    right_button.invoke()


window = tk.Tk()
window.title('注意指向实验')
window.geometry('300x100+600+300')
window.wm_resizable(False, False)

plus_label = tk.Label(window, text='+', font=('Arial', 30))
arrow_label = tk.Label(window, text=' ', font=('Arial', 20))
left_button = tk.Button(window, text='     ', cursor="hand2")
right_button = tk.Button(window, text='     ', cursor="hand2")

arrow_label.pack(side='top')
left_button.pack(side='left', expand=True)
plus_label.pack(side='left', expand=True)
right_button.pack(side='left', expand=True)

window.bind('<KeyPress-A>', A_click)
window.bind('<KeyPress-D>', D_click)
window.after(1000, add_arrow)
window.mainloop()

