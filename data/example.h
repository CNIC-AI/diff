
#include <iostream>

template <typename T> int func_template(T &a) { return 0; }

class A {
public:
  int func_in_class();

  int func_in_class_with_impl(char a) { return 0; }

  template <typename T> int func_in_class_template(T &a) { return 0; }
};

class B {
protected:
  int func_in_class_with_impl(char a) { return 0; }
};

namespace example {
namespace example2 {
class B {
protected:
  int func_in_class_with_impl(const char a) { return 0; }

  int operator+(int) { return 0; }
  operator int() { return 0; }
  operator char() { return 0; }

  static int static_func() { return 0; }
};
} // namespace example2
} // namespace example