# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import signal


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
                    string += '\\'

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
        print(str(i) + " "+str(list_of_bg.get(i)))


def shell_Run():
    list_of_bg = {}

    while True:

        try:
            a = input("Please Enter your Item : ")
        except:
            exit()

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
            if len(list_of_input) == 2:
                # print(list_of_bg)
                list_of_bg.pop(list_of_input[1])
                os.kill(int(list_of_input[1]), signal.SIGKILL)
            continue

        if list_of_input[0] == "bgstop":
            if len(list_of_input) == 2:
                list_of_bg[list_of_input[1]][2] = "suspend"
                os.kill(int(list_of_input[1]), signal.SIGSTOP)
            continue

        if list_of_input[0] == "bgstart":
            if len(list_of_input) == 2:
                list_of_bg[list_of_input[1]][2] = "running"
                os.kill(int(list_of_input[1]), signal.SIGCONT)
            continue

        if list_of_input[0] == "cd":
            if len(list_of_input) == 1:
                try:
                    os.chdir(list_of_input[1])
                except:
                    print("there isn't this path")
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
                    print("we haven't this comment (" + ' '.join(list_of_input) + ")")
                    exit()

        elif bg:
            pass
            # os.waitpid(child_pid, 0)
        else:
            os.waitpid(child_pid, 0)


if __name__ == '__main__':
    shell_Run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
