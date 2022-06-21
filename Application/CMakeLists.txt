# CMakeList.txt : CMake project for Application, include source and define
# project specific logic here.
#
project(Application)
# Add source to this project's executable.
add_executable (${PROJECT_NAME} 
"src/Application.cpp"
"src/Layers/MainLayer.cpp"
)

target_link_libraries(
    ${PROJECT_NAME}
    appazoid::appazoid
)