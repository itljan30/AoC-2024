add_executable(21a a.c)
target_link_libraries(21a PUBLIC DataStructures)
set_target_properties(21a PROPERTIES
    RUNTIME_OUTPUT_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
    OUTPUT_NAME "a.exe"
)

# add_executable(21b b.c)
# target_link_libraries(21b PUBLIC DataStructures)
# set_target_properties(21b PROPERTIES
#     RUNTIME_OUTPUT_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
#     OUTPUT_NAME "b.exe"
# )
