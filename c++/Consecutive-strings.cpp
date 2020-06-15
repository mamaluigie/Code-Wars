#include <iostream>
#include <string>
#include <vector>

class LongestConsec
{

public:
    static std::string longestConsec(std::vector<std::string> &strarr, int k);

};

std::string LongestConsec::longestConsec(std::vector<std::string> &strarr, int k)
{

	int vector_size = int(strarr.size());
	
	std::string max_string = "";
	
	std::string max_string_left = "";
	
	std::string max_string_right = "";

	int longest_location;
	
	if (vector_size == 0 || k > vector_size || k <= 0)
	{
		return "";
	}	

	for(int x = 0;x < int(strarr.size()); x++)
	{
		
		if (int(max_string.length()) < int(strarr[x].length()))
		{
			max_string = strarr[x];
			longest_location = x;
		}	
	}
	
	if(k == 1)
	{
		return max_string;
	}
	
	for(int x = longest_location ; x > longest_location - (k - 1) && x > 0; x--)
	{
		max_string_left.insert(0, strarr[x]);
	}	
	
	for(int x = longest_location ; x <= longest_location + (k - 1) && x < int(strarr.size()) - 1; x++)
	{
		max_string_right += strarr[x];
	}

	if(max_string_left >= max_string_right)
	{
		return max_string_left;
	}
	else
	{
		return max_string_right;
	}
}

int main()
{
	LongestConsec consec;
	std::vector<std::string> arr = {"zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"};
	std::cout << consec.longestConsec(arr, 1);
	//arr = {"ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"};
	//std::cout << consec.longestConsec(arr, 4);
	return 0;
}
