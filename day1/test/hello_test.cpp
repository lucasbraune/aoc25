#include <gtest/gtest.h>

#include <string>

#include "lib.hpp"

TEST(Day1Test, ExampleAssertions) {
  std::istringstream in{R"(L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
)"};
  int actual = aoc::solve_part1(in);
  EXPECT_EQ(actual, 3);
}

TEST(Day1Test, ZerosFunction) {
  EXPECT_EQ(aoc::impl::zeros(99, 1), 1);
  EXPECT_EQ(aoc::impl::zeros(0, -1), 0);
  EXPECT_EQ(aoc::impl::zeros(50, 1000), 10);
  EXPECT_EQ(aoc::impl::zeros(55, -55), 1);
}
