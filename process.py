import os
import subprocess


def run_script(script_name):
    try:
        subprocess.run(["python", script_name], check=True)
        print(f"{script_name} 运行成功。")
    except subprocess.CalledProcessError as e:
        print(f"{script_name} 运行失败: {e}")


def clear_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            os.remove(file_path)
    print(f"{folder_path} 文件夹已清空。")


if __name__ == "__main__":
    rounded_script = "./main/round.py"
    main_script = "./main/main.py"
    rounded_folder = "./main/rounded"

    run_script(rounded_script)
    run_script(main_script)

    clear_folder(rounded_folder)