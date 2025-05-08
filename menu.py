def show_menu():
    print("===== 菜单系统 =====")
    print("1. 打招呼")
    print("2. 显示信息")
    print("3. 退出")

def main():
    while True:
        show_menu()
        choice = input("请选择操作 (1/2/3): ")
        if choice == "1":
            print("你好，欢迎使用菜单程序！")
        elif choice == "2":
            print("作者：hobhobh，版本：v1.0")
        elif choice == "3":
            print("再见！程序退出。")
            break
        else:
            print("无效输入，请重新选择。")

if __name__ == "__main__":
    main()
