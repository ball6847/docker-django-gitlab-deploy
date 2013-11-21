#include <stdio.h>
#include <stdlib.h>
#include <stdexcept>
#include <iostream>

using std::cout;
using std::endl;
using std::runtime_error;

int main(int argc, char** argv)
{
    if (argc < 1)
    {
        throw std::runtime_error("expected atleast 1 argument.");
    }
    
    std::cout << argv[1] << endl;
    
    return 0;
}

/*
save as "hello.cpp"

compile using:
gcc "say.cpp" -o "say" -lstdc++ 

for komodo we can add this command
gcc "%F" -o "%b" -lstdc++ 

running this command, it should print out "something"
./say something
*/