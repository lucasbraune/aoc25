find_package(GTest CONFIG REQUIRED)

add_executable(lib_test lib_test.cpp)
target_include_directories(lib_test PRIVATE ${CMAKE_SOURCE_DIR}/src)
target_link_libraries(lib_test PRIVATE GTest::gtest GTest::gtest_main
    GTest::gmock GTest::gmock_main lib)

include(GoogleTest)
gtest_discover_tests(lib_test)

add_custom_target(run-tests
    COMMAND ${CMAKE_CTEST_COMMAND} --output-on-failure
    DEPENDS lib_test
)
