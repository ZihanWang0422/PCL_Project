cmake_minimum_required(VERSION 3.5 FATAL_ERROR)


project(passthrough)


find_package(PCL 1.10 REQUIRED)


include_directories(${PCL_INCLUDE_DIRS})

link_directories(${PCL_LIBRARY_DIRS})

add_definitions(${PCL_DEFINITIONS})


add_executable (passthrough passthrough.cpp)

target_link_libraries (passthrough ${PCL_LIBRARIES})
