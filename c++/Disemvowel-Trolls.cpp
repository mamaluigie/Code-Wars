#include <iostream>
#include <string>

std::string disemvowel(std::string str)
{
    // return
    char c;
    for(int i = 0; i < int(str.length()); i++)
    {
      c = str.at(i);
      if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U')
      {
		  str.erase(i, 1);
		  i--;
      }
    }
    return str;
}

int main()
{
	std::string sentence = "This website is for losers LOL!";
	std::cout << "The unaltered string is:" << sentence << "\n\n\n";
	std::cout << "The altered sentence is:" << disemvowel("This website is for losers LOL!");
	return 0;

}

