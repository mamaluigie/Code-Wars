#include <iostream>
#include <string>
#include <vector>
#include <map>


int findOdd(const std::vector<int>& numbers)
{
  
	//your code here
	std::map<int, int> dictionary_of_numbers;
	
	std::map<int, int>::iterator iterator;


	for(int i = 0; i < numbers.size(); i++)
	{
		if (is_it_in(dictionary_of_numbers, numbers.at(i))
		{
			dictionary_of_numbers[numbers.at(i)] = dictionary_of_numbers[number.at(i)] + 1;
		}
		else
		{
			dictionary_of_numbers[numbers.at(i)] = 1;
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

bool is_it_in(std::map<int, int> &map, int number)
{
	for(std::map::iterator it = map.begin(); it != map.end(); ++it)
	{
		if it->first == number
		{
			return true;
		}
	}
	return false;
}

int main()
{


	//std::cout << findOdd({20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5});	
	findOdd({20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5});	
	return 0;
}

