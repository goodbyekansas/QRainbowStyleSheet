# -*- coding: utf-8 -*-
"""Script to process UI files (convert .ui to .py).

It compiles .ui files to be used with PyQt5, PySide2, PySide6, QtPy.
You just need to run (it has default values) from script folder.

To run this script you need to have these tools available on system:

    - pyuic5 for PyQt5 and QtPy
    - pyside2-uic for Pyside2
    - pyside6-uic for Pyside6

Links to understand those tools:

    - pyuic5: http://pyqt.sourceforge.net/Docs/PyQt5/designer.html#pyuic5
    - pyside2-uic: https://wiki.qt.io/Qt_for_Python_UiFiles (Documentation Incomplete)
    - pyside6-uic: https://doc.qt.io/qtforpython-6/tools/pyside-uic.html

"""

# Standard library imports
import argparse
import glob
import os
import sys
import shutil

# Constants
HERE = os.path.abspath(os.path.dirname(__file__))
REPO_ROOT = os.path.dirname(HERE)


def main(arguments):
    """Process UI files."""
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "--ui_dir",
        default=os.path.join(REPO_ROOT, "example", "ui"),
        type=str,
        help="UI files directory, relative to current directory.",
    )
    parser.add_argument(
        "--create",
        default="qtpy",
        choices=["pyqt5", "pyside2", "pyside6", "qtpy", "all"],
        type=str,
        help="Choose which one would be generated.",
    )

    args = parser.parse_args(arguments)

    print("Changing directory to: ", args.ui_dir)
    os.chdir(args.ui_dir)

    print("Converting .ui to .py ...")

    for ui_file in glob.glob("*.ui"):
        # get name without extension
        filename = os.path.splitext(ui_file)[0]
        print(filename, "...")
        ext = ".py"

        # creating names
        py_file_pyqt5 = filename + "_pyqt5_ui" + ext
        py_file_pyside2 = filename + "_pyside2_ui" + ext
        py_file_pyside6 = filename + "_pyside6_ui" + ext
        py_file_qtpy = filename + "_ui" + ext

        # calling external commands
        if args.create in ["pyqt5", "qtpy", "all"]:
            try:
                pyuic5_path = shutil.which("pyuic5")
                if pyuic5_path:
                    subprocess.run(
                        [
                            pyuic5_path,
                            "--import-from=qrainbowstyle",
                            ui_file,
                            "-o",
                            py_file_pyqt5,
                        ],
                        check=True,
                    )
            except FileNotFoundError:
                print("You must install pyuic5")
            else:
                print("Compiling using pyuic5 ...")

        if args.create in ["pyside2", "all"]:
            try:
                pyside2_uic_path = shutil.which("pyside2-uic")
                if pyside2_uic_path:
                    subprocess.run(
                        [
                            pyside2_uic_path,
                        "--import-from=qrainbowstyle",
                        ui_file,
                        "-o",
                        py_file_pyside2,
                        ],
                        check=True,
                    )
            except FileNotFoundError:
                print("You must install pyside2-uic")
            else:
                print("Compiling using pyside2-uic ...")

        if args.create in ["pyside6", "all"]:
            try:
                pyside6_uic_path = shutil.which("pyside6-uic")
                if pyside6_uic_path:
                    subprocess.run(
                        [
                            pyside6_uic_path,
                        "--import-from=qrainbowstyle",
                        ui_file,
                        "-o",
                        py_file_pyside6,
                        ],
                        check=True,
                    )
            except FileNotFoundError:
                print("You must install pyside6-uic %s", str(er))
            else:
                print("Compiling using pyside6-uic ...")

        if args.create in ["qtpy", "all"]:
            print("Creating also for qtpy ...")
            # special case - qtpy - syntax is PyQt5
            with open(py_file_pyqt5, "r") as file:
                filedata = file.read()

            # replace the target string
            filedata = filedata.replace("from PyQt5", "from qtpy")

            with open(py_file_qtpy, "w+") as file:
                # write the file out again
                file.write(filedata)

            if args.create not in ["pyqt5"]:
                os.remove(py_file_pyqt5)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
