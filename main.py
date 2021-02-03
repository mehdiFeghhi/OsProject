# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import signal
from colorama import Fore, Back, Style, init
from termcolor import colored, cprint
from datetime import datetime


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def make_list(a):
    a = a + " "

    see_char = False
    have_bacslash = False
    have_cotation = False
    string = ""
    list = []
    for i in a:

        if have_cotation:

            if i == '"':
                # string += '"'
                list.append(string)
                have_cotation = False
                string = ""
            else:
                string += i

        elif i == '"':
            have_cotation = True
            # string = '"'


        elif have_bacslash:
            if i == ' ':
                if see_char:
                    list.append(string)
                    string = ""
                else:

                    string += i
                    see_char = True
            else:
                if i == '\\':
                    see_char = False
                    # string += '\\'

                else:

                    string += i
                continue

        elif i == "\\":
            string += i
            have_bacslash = True
            see_char = False
            continue

        elif i == ' ':

            if string != "":
                list.append(string)
            string = ""

        else:

            string += i
    # print(list)
    if len(string) > 0:
        list.append(string)
    return list


def show_list(list_of_bg):
    for i in list_of_bg:
        inpu = list_of_bg.get(i)
        print(colored(str(i), 'green') + colored(" ✎ ") + colored(" ".join(inpu[1]), 'yellow'))


def function_get_input(number_program_in_backGround):
    now = datetime.now()
    return input(colored('Me:hi', 'blue') + colored("♁☽ ", 'blue')
                 + colored('[', 'yellow') + colored(now.strftime("%H:%M:%S"), 'red') + colored(']', 'yellow') + colored(
        '', 'yellow') +
                 colored("[", 'yellow') + colored(number_program_in_backGround, 'red') +
                 colored("]", 'yellow') + colored(" ", 'yellow') + colored('', 'yellow') + colored('☯', ) + " ")


def shell_Run():
    list_of_bg = {}
    list_of_pip = []
    while True:

        if len(list_of_pip) == 0:
            try:
                # a = input("Please Enter your Item : ")
                a = function_get_input(len(list_of_bg))
                if " | " in a:
                    list_of_pip = a.split(" | ")
                    list_of_pip.reverse()
                    continue
            except:
                exit()

        else:
            a = list_of_pip.pop()

        if a == "bglist":
            show_list(list_of_bg)
            continue

        if a == "exit":
            exit()
        if a == "":
            continue

        list_of_input = make_list(a)
        # if list_of_input[0] == "clear":
        #     clear = "\n" * 15
        #     print(clear)
        #     continue

        if list_of_input[0] == "bgkill":
            if len(list_of_input) == 2 and list_of_input[1] in list_of_bg:
                # print(list_of_bg)
                list_of_bg.pop(list_of_input[1])
                os.kill(int(list_of_input[1]), signal.SIGKILL)
            continue

        if list_of_input[0] == "bgstop" and list_of_input[1] in list_of_bg:
            if len(list_of_input) == 2:
                list_of_bg[list_of_input[1]][2] = "suspend"
                os.kill(int(list_of_input[1]), signal.SIGSTOP)
            continue

        if list_of_input[0] == "bgstart" and list_of_input[1] in list_of_bg:
            if len(list_of_input) == 2:
                list_of_bg[list_of_input[1]][2] = "running"
                os.kill(int(list_of_input[1]), signal.SIGCONT)
            continue

        if list_of_input[0] == "cd":
            if len(list_of_input) == 2:
                try:
                    os.chdir(list_of_input[1])
                except:
                    print(colored("there isn't this path", 'red'))
            else:
                print(colored("Number of cd Item isn't one", 'red'))
            continue

        child_pid = os.fork()

        bg = False
        if list_of_input[0] == 'bg':
            list_of_input = list_of_input[1:]
            list_of_bg[str(child_pid)] = [child_pid, list_of_input, "running"]
            bg = True

        if child_pid == 0:
            if list_of_input[0] == "pwd":
                cwd = os.getcwd()
                print(cwd)
                exit()

            else:
                try:
                    os.execvp(list_of_input[0], list_of_input)
                    exit()
                except:
                    print(colored("we haven't this comment (" + ' '.join(list_of_input) + ")", 'red'))
                    exit()

        elif bg:
            pass
            # os.waitpid(child_pid, 0)
        else:
            os.waitpid(child_pid, 0)


if __name__ == '__main__':
    shell_Run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
