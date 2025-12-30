#include "lib.hpp"

namespace aoc {

int64_t solve_part1(std::istream& in) {
  int64_t sum = 0;
  std::vector<Range> ranges{};
  in >> ranges;
  for (const auto& r : ranges) {
    sum += add_valid_ids(r);
  }
  return sum;
}
int64_t solve_part2(std::istream& in) {
  // TODO
  return -1;
}

std::ostream& operator<<(std::ostream& os, const Range& r) {
  return os << r.start << "-" << r.end;
}

std::istream& operator>>(std::istream& is, Range& range) {
  is >> range.start;
  is.ignore();  // ignore the '-'
  is >> range.end;
  return is;
}

std::istream& operator>>(std::istream& is, std::vector<Range>& ranges) {
  Range curr = {};
  while (is >> curr) {
    ranges.push_back(curr);
    if (is) {
      is.ignore();  // ignore the ','
    }
  }
  return is;
}

int digit_count(int64_t n) {
  int count = 0;
  while (n != 0) {
    // NOLINTNEXTLINE(cppcoreguidelines-avoid-magic-numbers)
    n /= 10;
    ++count;
  }
  return count;
}

int64_t leading_digits(int64_t n) {
  int discard_count = (digit_count(n) + 1) / 2;
  for (int i = 0; i < discard_count; ++i) {
    // NOLINTNEXTLINE(cppcoreguidelines-avoid-magic-numbers)
    n /= 10;
  }
  return n;
}

int64_t make_invalid_id(int64_t leading_digits) {
  int count = digit_count(leading_digits);
  int64_t result = leading_digits;
  for (int i = 0; i < count; ++i) {
    // NOLINTNEXTLINE(cppcoreguidelines-avoid-magic-numbers)
    result = result * 10;
  }
  return result + leading_digits;
}

int64_t add_valid_ids(Range r) {
  int64_t curr = leading_digits(r.start);
  while (make_invalid_id(curr) < r.start) ++curr;
  int64_t sum = 0;
  while (make_invalid_id(curr) <= r.end) {
    sum += make_invalid_id(curr);
    // std::cerr << r << ": adding " << make_invalid_id(curr) << "\n";
    ++curr;
  }
  return sum;
}

}  // namespace aoc
