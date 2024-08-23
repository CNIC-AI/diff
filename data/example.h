#include <iostream>

template <typename T>
int func_template(T& a) {
    return 0;
}

class A {
public:
    int func_in_class();

    int func_in_class_with_impl (char a) {
        return 0;
    }

    template <typename T>
    int func_in_class_template(T& a) {
        return 0;
    }
};
