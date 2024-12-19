add_executable(11a a.c)
target_link_libraries(11a PUBLIC DataStructures)
set_target_properties(11a PROPERTIES
    RUNTIME_OUTPUT_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
    OUTPUT_NAME "a.exe"
)

add_executable(11b b.c)
target_link_libraries(11b PUBLIC DataStructures)
set_target_properties(11b PROPERTIES
    RUNTIME_OUTPUT_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
    OUTPUT_NAME "b.exe"
)
