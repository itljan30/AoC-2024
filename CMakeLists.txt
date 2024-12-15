cmake_minimum_required(VERSION 3.15)
project(AoC)

include(FetchContent)

FetchContent_Declare(
    DataStructures
    GIT_REPOSITORY git@github.com:itljan30/data-structures.git
    GIT_TAG v1.0.0
)

FetchContent_MakeAvailable(DataStructures)

add_subdirectory(5)
