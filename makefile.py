#!/usr/bin/env python3

import os
import sys


if __name__ == "__main__":
    try:
        Path = os.path.dirname(os.path.abspath(__file__))

        if len(sys.argv) > 1:
            if "clean" == sys.argv[1]:
                if os.path.exists(f"{Path}/GnuChanGUI.egg-info"):
                    print("rm -r GnuChanGUI.egg-info build")
                    os.chdir(Path)
                    os.system("rm -r GnuChanGUI.egg-info build")

                else:
                    print("There is no Build Files Here!")

            elif "build" == sys.argv[1]:
                os.system("pip install .")

            else:
                print("do like this!:| ./makefile build or clean")

        else:
            print("do like this!:| ./makefile build or clean")

    except Exception as ERR:
        print(ERR)




