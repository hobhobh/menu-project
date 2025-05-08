import sys


def greet_user():
    print("你好，欢迎使用 CLI 菜单工具！")


def show_info():
    print("项目名: CLI Menu")
    print("作者: chenhao")
    print("版本: v0.2")


def exit_program():
    print("感谢使用，程序已退出。")
    sys.exit(0)


def show_menu():
    print("\n====== 菜单 ======")
    print("1. 打招呼")
    print("2. 显示信息")
    print("3. 退出")


def handle_choice(choice):
    choices = {
        "1": greet_user,
        "2": show_info,
        "3": exit_program
    }

    action = choices.get(choice)
    if action:
        action()
    else:
        print("⚠️ 输入无效，请输入 1 ~ 3 之间的数字。")


def main():
    while True:
        show_menu()
        choice = input("请输入选项：").strip()
        handle_choice(choice)


if __name__ == "__main__":
    main()
