add_executable(5a a.c)
add_executable(5b b.c)

target_link_libraries(5a PUBLIC DataStructures)
target_link_libraries(5b PUBLIC DataStructures)

set_target_properties(5a PROPERTIES
    RUNTIME_OUTPUT_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
    OUTPUT_NAME "5a.exe"
)

set_target_properties(5b PROPERTIES
    RUNTIME_OUTPUT_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
    OUTPUT_NAME "5b.exe"
)
