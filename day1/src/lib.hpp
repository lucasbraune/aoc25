#ifndef LIB_H
#define LIB_H

#include <iostream>

namespace aoc {

int solve_part1(std::istream& in);
int solve_part2(std::istream& in);

namespace impl {

int zeros(int pos, int move);

}

}  // namespace aoc

#endif
