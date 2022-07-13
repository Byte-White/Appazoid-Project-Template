# CMakeList.txt : CMake project for Application, include source and define
# project specific logic here.
#
project(Application)

file(GLOB APP_SRC_FILES
     "../app/src/*.cpp"
)

# Add source to this project's executable.
add_executable (${PROJECT_NAME} ${APP_SRC_FILES})

target_link_libraries(
    ${PROJECT_NAME}
    appazoid::appazoid
)