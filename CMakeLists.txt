cmake_minimum_required (VERSION 3.6)

project (MyApplication)

#'vendor'
add_subdirectory(vendor/Appazoid)


#'app'

add_executable (${PROJECT_NAME} 
app/src/Application.cpp
app/src/Layers/MainLayer.cpp
)

target_link_libraries(
    ${PROJECT_NAME}
    appazoid::appazoid
)