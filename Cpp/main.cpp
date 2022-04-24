#include <iostream>    
#include <string>
#include <cstring>
#include <stdio.h>    
#include <conio.h>
#include <stdlib.h>

using namespace std;

const string pyInterpreter = "C:/Users/leone/anaconda3/envs/myEnv/python ";
const string pyFolder = "../";

int main()
{
    system("conda activate myEnv");
    string fileStr = pyInterpreter+pyFolder+"main.py";
    const char* file = (fileStr).c_str();
    system(file);
}