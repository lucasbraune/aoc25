#include <fstream>
#include <iostream>
#include <string>

#include "lib.hpp"

int main() {
  std::ifstream in("resource/input.txt");
  if (!in) {
    std::cerr << "Could not open input file\n";
    return 1;
  }
  auto part1_answer = aoc::solve_part1(in);
  std::cout << "Part 1 answer: " << part1_answer << '\n';

  // auto part2_answer = aoc::solve_part2(in);
  // std::cout << "Part 2 answer: " << part2_answer << '\n';

  return 0;
}
