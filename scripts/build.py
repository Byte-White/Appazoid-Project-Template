#@echo off
#cd ../
#cmake --build out
#cmake -B out
#PAUSE

import json
import os
from generate_build_system import generate_build_system



if(__name__ == "__main__"):
    result = generate_build_system()
    if result:
        print("Building...")
        project_json = open("../project.json", "r")
        data = json.load(project_json)
        output_folder = data["project"]["output_folder"]
        os.chdir("../")
        os.system(f"cmake --build {output_folder}")
        os.system(f"cmake -B {output_folder}")
        pass
    else:
        print("generate_build_system() did not pass.")