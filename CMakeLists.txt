cmake_minimum_required (VERSION 3.6)
project (MyProject VERSION 1.0)
#'vendor'
add_subdirectory("vendor/Appazoid")


#'app'

#1 == AZ_RENDER_API_OPENGL
#2 == AZ_RENDER_API_VULKAN
add_compile_definitions(AZ_RENDER_API=AZ_RENDER_API_OPENGL)

add_executable (${PROJECT_NAME} 
"app/src/Application.cpp"
"app/src/Layers/MainLayer.cpp"
)

target_link_libraries(
${PROJECT_NAME}
appazoid::appazoid
)
