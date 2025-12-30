#include "lib.hpp"

#include <gtest/gtest.h>

#include <string>

TEST(Day2Test, SolvesExample) {
  std::istringstream in{
      R"(11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124)"};

  auto answer = aoc::solve_part1(in);

  EXPECT_EQ(answer, 1227775554L);
}

TEST(Day2Test, ParsesRanges) {
  std::istringstream in{R"(11-22,95-115)"};

  std::vector<aoc::Range> ranges{};
  in >> ranges;

  // NOLINTNEXTLINE(cppcoreguidelines-avoid-magic-numbers)
  std::vector<aoc::Range> expected{{11, 22}, {95, 115}};
  EXPECT_EQ(ranges, expected);
}

TEST(Day2Test, ParsesEmptyRange) {
  std::istringstream in{""};

  std::vector<aoc::Range> ranges{};
  in >> ranges;

  std::vector<aoc::Range> expected{};
  EXPECT_EQ(ranges, expected);
}

aoc::Range parse_range(const std::string& s) {
  std::istringstream in{s};
  aoc::Range r{};
  in >> r;
  return r;
}

TEST(Day2Test, LeadingDigits) {
  using aoc::leading_digits;
  EXPECT_EQ(leading_digits(123456), 123);
  EXPECT_EQ(leading_digits(1234567), 123);
  EXPECT_EQ(leading_digits(12), 1);
  EXPECT_EQ(leading_digits(1), 0);
  EXPECT_EQ(leading_digits(0), 0);
}

TEST(Day2Test, AddsValidIds) {
  using aoc::add_valid_ids;
  EXPECT_EQ(add_valid_ids(parse_range("11-22")), 33);  // 11 + 22
  EXPECT_EQ(add_valid_ids(parse_range("95-115")), 99);
  EXPECT_EQ(add_valid_ids(parse_range("998-1012")), 1010);
  EXPECT_EQ(add_valid_ids(parse_range("1188511880-1188511890")), 1188511885L);
  EXPECT_EQ(add_valid_ids(parse_range("222220-222224")), 222222);
  EXPECT_EQ(add_valid_ids(parse_range("1698522-1698528")), 0);
  EXPECT_EQ(add_valid_ids(parse_range("446443-446449")), 446446);
  EXPECT_EQ(add_valid_ids(parse_range("38593856-38593862")), 38593859);
  EXPECT_EQ(add_valid_ids(parse_range("565653-565659")), 0);
  EXPECT_EQ(add_valid_ids(parse_range("824824821-824824827")), 0);
  EXPECT_EQ(add_valid_ids(parse_range("2121212118-2121212124")), 0);
}
