import PyInstaller.__main__
import sys
import os
from shutil import rmtree, move

def run_build(sn: str, fn: str) -> None:
    """
        Generating final exe file

        #### Params:
        - sn - source name of file which will be used for generating (with extension)
        - fn - final name of file which will be used for saving exe file (without extension)
    """

    try:
        PyInstaller.__main__.run([
            sn, # name of the source file (REQUIRED)
            '--onefile', # option for generating only one file (REQUIRED)
            '--windowed', # option for no displaying console (OPTIONAL)
            f'-n{fn}' # name of the final file (REQUIRED)
        ])
    except Exception as ex:
        print(ex)
        print("[ERROR] Произошла ошибка при генерации exe файла")


def get_only_one_file(exe_name: str) -> None:
    """
        Clear temp folders (build, dist), files (.spec) and moving exe to main directory

        Need final exe name without extension 
    """
    cwd = os.getcwd()

    try:
        move(os.path.join(cwd, "dist", f"{exe_name}.exe"), os.path.join(cwd, f"{exe_name}.exe")) # Moving executable from dist to main folder
    except:
        print("[ERROR] Папка dist или exe файл не найдены")
    
    try:
        rmtree(os.path.join(cwd, 'build')) # Removing build directory
    except:
        print("[ERROR] Папка build не найдена")
    
    try:
        rmtree(os.path.join(cwd, 'dist')) # Removing dist directory
    except:
        print("[ERROR] Папка dist не найдена")

    try:
        os.remove(os.path.join(cwd, f"{exe_name}.spec")) # Removing spec file
    except:
        print("[ERROR] Файл .spec не найден")


def main():
    args = sys.argv
    
    try:
        sn = args[args.index('-sn') + 1].strip()
        fn = args[args.index('-fn') + 1].strip()
    except:
        print("[ERROR] Некорректный формат использования команды.\nКорректный: python generate_exe.py -sn <source-file-name> -fn <final-file-name>")
    
    run_build(sn=sn, fn=fn)
    get_only_one_file(fn)

if __name__ == '__main__':
    main()
