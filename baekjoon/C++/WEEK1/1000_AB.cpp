#include <iostream>
#include <iomanip> 
int main()
{
    int a,b;
    std::cin >> a >> b;
    double result = (double)a / b;
    std::cout << std::fixed << std::setprecision(10) << result << std::endl;
}