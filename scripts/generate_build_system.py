
import json
from time import sleep, time
from xml.etree.ElementTree import tostring
import os
files:list = []
dirs:list = []
seperator = os.path.sep
go_back_prefix = ".."+ seperator

debug_info = True

def get_cpp_files(directory:str) -> list:
    global files
    global go_back_prefix
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)

        # checking if it is a file
        if os.path.isfile(f):
            if (".cpp" in f):
                files.append(f.removeprefix(go_back_prefix))
        else:
            files = get_cpp_files(f) 
    return files
def get_vendor_dirs(directory:str) -> list:
    global dirs
    global go_back_prefix
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)

        # checking if it is a file
        if os.path.isfile(f):
            pass
        else:
            dirs.append(f.removeprefix(go_back_prefix)) 
    return files


def generate_cmake():
    project_json = open("../project.json", "r")
    if(project_json.closed):
        print("error: json file has been closed!")
        return
    data = json.load(project_json) #load json data
    
    cmake_version = data["project"]["cmake_minimum_version"]
    project_name = data["project"]["name"]
    project_version = data["project"]["version"]
    render_api = data["project"]["render_api"]
    link_libraries = data["project"]["link_libraries"]
    
    filepath = "../CMakeLists.txt"
    
    cmake_file = open(filepath,"w")
    #os.system("attrib +h "+filepath)#hides the file
    if(cmake_file.closed):
        print("error: cmake file has been closed!")
        return
    cmake_file.write(f"cmake_minimum_required (VERSION {cmake_version})\n")
    cmake_file.write(f"project ({project_name} VERSION {project_version})")

    #add vendor dirs
    get_vendor_dirs("..\\vendor")
    global dirs
    dirs_str = ""
    for directory in dirs:
        dirs_str += "add_subdirectory(\""
        dirs_str += directory
        dirs_str += "\")\n"
    dirs_str=dirs_str.replace("\\","/")#change to standard
    cmake_file.write(f"""
#'vendor'
{dirs_str}

#'app'

#1 == AZ_RENDER_API_OPENGL
#2 == AZ_RENDER_API_VULKAN
add_compile_definitions(AZ_RENDER_API={render_api})

add_executable (${{PROJECT_NAME}} 
""")

    #C++ files
    global files
    files_str:str = ""
    for file in files:
        files_str += "\""
        files_str += file
        files_str += "\"\n"
    files_str=files_str.replace("\\","/")#change to standard
    
    lib_str:str = ""
    for lib in link_libraries:
        lib_str += lib
        lib_str += "\n"
    lib_str=lib_str.replace("\\","/")#change to standard
    #adding source files here
    cmake_file.write(f"""{files_str})

target_link_libraries(
${{PROJECT_NAME}}
{lib_str})
""")
    global debug_info
    if(debug_info==True):
        json_formatted_str = json.dumps(data, indent=2)
        print(f"json:\n {json_formatted_str}")
    return

def generate_build_system():
    try:
        print("Generating Build Systems...")
        start = time()
        get_cpp_files(go_back_prefix+"app"+seperator) #list saved in global variable
        generate_cmake()
        end = time()
        print("Finished Generating Build Systems.")
        print(f"Total time: {(end-start)}s")
    except Exception as e:
        print(f"(generate_build_system() exception) {str(e)}")
        return False
    return True


if(__name__ == "__main__"):
    generate_build_system()    