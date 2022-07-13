# CMakeList.txt : Top-level CMake project file, do global configuration
# and include sub-projects here.
#
cmake_minimum_required (VERSION 3.6)

project (AppazoidProject)

# Include sub-projects.

add_subdirectory ("vendor")
add_subdirectory ("app")