#include <fstream>
#include <iostream>
#include <string>

#include "lib.hpp"

int main() {
  std::ifstream in("resource/input1");
  // std::ifstream in("resource/example1");
  if (!in) {
    std::cerr << "Could not open input file\n";
    return 1;
  }
  int answer = aoc::solve_part2(in);
  std::cout << "Password: " << answer << '\n';
  return 0;
}
