cmake_minimum_required(VERSION 3.15)
project(AoC)

include(FetchContent)

FetchContent_Declare(
    DataStructures
    GIT_REPOSITORY https://github.com/itljan30/data-structures.git
    GIT_TAG v1.0.0-beta
)

FetchContent_MakeAvailable(DataStructures)

add_subdirectory(02)
add_subdirectory(05)
add_subdirectory(06)
add_subdirectory(07)
add_subdirectory(11)
add_subdirectory(21)
