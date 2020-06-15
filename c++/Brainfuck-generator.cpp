#include <iostream>
#include <string>
inline std::string to_brainfuck (const std::string& s_in)
{	
	//the string that will be the output string
	std::string brainfuck_string = "";
	
	//the length of the input string
	int string_length = int(s_in.length());
	
	//the array of characters that will be cycled through to calculate how many +'s will be made.
	char char_array[string_length];

	for(int i = 0; i < string_length; i ++)
	{
		//the ascii value at the location i in the string to calculate how many +'s will be made.
		int ascii_value = int(s_in.at(i));
		
		for(int x = 0; x < ascii_value; x++)
		{
			brainfuck_string += "+";
		}
		
		if(i < string_length - 1)
		{	
			brainfuck_string += ".>";
		} 
		else 
		{
			brainfuck_string += ".";
		}
	}

	return brainfuck_string;
}

int main()
{
	std::cout << to_brainfuck("Hello world.");
	return 0;
}
