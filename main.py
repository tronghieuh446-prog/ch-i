# ==========================================
# Alex Dev Hacker Terminal
# main.py
# ==========================================

from theme import set_title, loading, draw
from systeminfo import print_system_info
from terminal import terminal


def main():
    # Đặt tiêu đề cửa sổ
    set_title()

    # Hiệu ứng khởi động
    loading()

    # Hiển thị banner
    draw()

    # Hiển thị thông tin hệ thống
    print_system_info()

    # Bắt đầu terminal
    terminal()


if __name__ == "__main__":
    main()
