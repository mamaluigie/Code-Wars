#include <iostream>
#include <string>

using namespace std;

string get_planet_name(int id)
{
	string planets[8] = {"Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"};

	return planets[id - 1];
}




int main()
{
	int x;
	do
	{
		cin >> x;	
		
		cout << "\n\n" << get_planet_name(x) << "\n\n";
	
	}
	while (true);
	return 0;
}
