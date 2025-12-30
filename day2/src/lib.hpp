#ifndef LIB_H
#define LIB_H

#include <cstdint>
#include <iostream>
#include <sstream>

namespace aoc {

int64_t solve_part1(std::istream& in);
int64_t solve_part2(std::istream& in);

struct Range {
  int64_t start;
  int64_t end;

  bool operator==(const Range& other) const = default;
};

std::ostream& operator<<(std::ostream& os, const Range& r);
std::istream& operator>>(std::istream& is, Range& range);
std::istream& operator>>(std::istream& is, std::vector<Range>& ranges);

int64_t add_valid_ids(Range r);
int64_t leading_digits(int64_t n);

}  // namespace aoc

#endif
