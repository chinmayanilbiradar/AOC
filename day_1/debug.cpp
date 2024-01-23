#include <iostream>
#include <fstream>
#include <string>

int main()
{
    // Specify the file path
    std::string filePath = "C:/Users/birad/Desktop/AOC/sample.txt";

    // Create an input file stream object
    std::ifstream inputFile(filePath);

    // Check if the file is open
    if (inputFile.is_open())
    {
        // Read and print each line in the file
        std::string line;
        while (std::getline(inputFile, line))
        {
            std::cout << line << std::endl;
        }

        // Close the file after reading
        inputFile.close();
    }
    else
    {
        // Print an error message if the file couldn't be opened
        std::cerr << "Unable to open file: " << filePath << std::endl;
    }

    return 0;
}
