# Appazoid-Project-Template
A Template For GUI Apps With Appazoid Framework

# How To Build:
open the `scripts/` folder and run `build.bat`. If you can't run it you can run `py build.py` in the command prompt.

edit `project.json` to change the build settings

# project.json example:
```json
{
    "project":
    {
        "name": "MyProject",
        "version": 1.0,
        "cmake_minimum_version": 3.6,
        "link_libraries": ["appazoid::appazoid"],
        "render_api": "AZ_RENDER_API_OPENGL",
        "output_folder": "out"
    }
}
```

# 'vendor' folder:
Add your 3rd party libraries in there. After you build your project it will automatically 
add them to the cmake file (`CMakeLists.txt`)
# 'app' folder:
Add your code there. After you build your project it will automatically compile all `.cpp`
files. in the `src` folder