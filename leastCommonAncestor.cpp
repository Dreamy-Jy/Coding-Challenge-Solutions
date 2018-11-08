#include <iostream>
#include <typeinfo>

// TODO: Get VSCode to compile my code on saves
int main(int argc, char **argv) {
    if (argc > 0) {
        for( int i = 1; i < argc; i++) {
            std::cout << argv[i]<< std::endl;
        }
    }
    return 0;
}