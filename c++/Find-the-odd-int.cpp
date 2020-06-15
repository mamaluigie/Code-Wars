#include <iostream>
#include <string>
#include <vector>
#include <map>


int findOdd(const std::vector<int>& numbers)
{
  
	//your code here
	std::map<int, int> dictionary_of_numbers;
	
	std::map<int, int>::iterator iterator;

	for(int i = 0; i < int(numbers.size()); i++)
	{
		for(iterator = dictionary_of_numbers.begin(); iterator != dictionary_of_numbers.end(); iterator++)
		{
			
			std::cout << numbers.at(i);
			if (iterator->first == numbers.at(i))
			{
				dictionary_of_numbers[iterator->first] = iterator->second + 1;
			}
			else if(iterator == dictionary_of_numbers.end())
			{
				dictionary_of_numbers[numbers.at(i)] = 1;
			}
		}
	
	}
	for(iterator = dictionary_of_numbers.begin(); iterator != dictionary_of_numbers.end(); ++iterator)
	{	
		if (dictionary_of_numbers[iterator->second]%2 == 1)
		{
			return iterator->first;
		}
	}
}

int main()
{


	//std::cout << findOdd({20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5});	
	findOdd({20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5});	
	return 0;
}
