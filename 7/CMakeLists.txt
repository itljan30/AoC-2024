add_executable(7a a.c)
target_link_libraries(7a PUBLIC DataStructures)
set_target_properties(7a PROPERTIES
    RUNTIME_OUTPUT_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
    OUTPUT_NAME "a.exe"
)

# add_executable(6b b.c)
# target_link_libraries(6b PUBLIC DataStructures)
# set_target_properties(6b PROPERTIES
#     RUNTIME_OUTPUT_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
#     OUTPUT_NAME "b.exe"
# )
