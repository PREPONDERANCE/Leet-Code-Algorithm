#include <iostream>
#include <set>
#include <vector>
#include <unordered_set>
using namespace std;

bool containsDuplicate(vector<int>& nums){
//	set<int> hashset;
//	for(vector<int>::const_iterator i = nums.begin(); i != nums.end(); i++)
//		hashset.insert(*i);
//	
//	return hashset.size() != nums.size();
	
	unordered_set<int> s(nums.begin(), nums.end());
	return (s.size() != nums.size());
}

int main(int argc, char *argv[]) {
	vector<int> v = {1, 2, 3, 4, 5, 4};
	cout << containsDuplicate(v);
	
	return 0;
}