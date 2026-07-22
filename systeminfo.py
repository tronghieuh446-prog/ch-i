import os
import platform
import socket
import getpass
from datetime import datetime

try:
    import psutil
except ImportError:
    psutil = None


def get_system_info():
    """Trả về thông tin hệ thống dưới dạng dict."""

    info = {
        "Computer": socket.gethostname(),
        "User": getpass.getuser(),
        "OS": f"{platform.system()} {platform.release()}",
        "Version": platform.version(),
        "Python": platform.python_version(),
        "Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

    if psutil:
        info["CPU Usage"] = f"{psutil.cpu_percent(interval=0.2)}%"
        info["RAM Usage"] = f"{psutil.virtual_memory().percent}%"

        disk = psutil.disk_usage(os.path.abspath(os.sep))

        info["Disk Used"] = (
            f"{disk.used // (1024**3)}GB / "
            f"{disk.total // (1024**3)}GB"
        )

    return info


def print_system_info():

    print("=" * 60)
    print("           SYSTEM INFORMATION")
    print("=" * 60)

    data = get_system_info()

    for key, value in data.items():
        print(f"{key:<15}: {value}")

    print("=" * 60)
