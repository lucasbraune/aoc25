#include "lib.hpp"

namespace aoc {

constexpr int START_POS = 50;
constexpr int TRACK_LENGTH = 100;

int rotate(int pos, int move) {
  pos = (pos + move) % TRACK_LENGTH;
  if (pos < 0) pos += TRACK_LENGTH;
  return pos;
}

// Returns how many times the arrow points to zero
// during the move
int impl::zeros(int pos, int move) {
  // move = (move / TRACK_LENGTH) * TRACK_LENGTH + move % TRACK_LENGTH
  int turns = std::abs(move / TRACK_LENGTH);
  int dest = pos + move % TRACK_LENGTH;
  bool crossed_right = pos < TRACK_LENGTH && dest >= TRACK_LENGTH;
  bool crossed_left = pos > 0 && dest <= 0;
  return crossed_left || crossed_right ? turns + 1 : turns;
}

int parse_move(const std::string& line) {
  int sign = line[0] == 'R' ? 1 : -1;
  int value = std::stoi(line.substr(1));
  return sign * value;
}

int solve_part1(std::istream& in) {
  int pos = START_POS;
  int password = 0;
  std::string line;
  while (std::getline(in, line)) {
    int move = parse_move(line);
    pos = rotate(pos, move);
    if (pos == 0) ++password;
  }
  return password;
}

int solve_part2(std::istream& in) {
  int pos = START_POS;
  int zeroes_crossed = 0;
  std::string line;
  while (std::getline(in, line)) {
    int move = parse_move(line);
    int zeros = impl::zeros(pos, move);
    zeroes_crossed += zeros;
    pos = rotate(pos, move);

    // std::cerr << "Dial moves " << line << " to position " << pos;
    // if (zeros > 0) {
    //   std::cerr << "; zeroes crossed: " << zeros;
    // }
    // std::cerr << std::endl;
  }
  return zeroes_crossed;
}

}  // namespace aoc
