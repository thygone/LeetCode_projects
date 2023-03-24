/*
* Author: Dane Selch
* source: LeetCode
* title: jump game
* direction: 
*  You are given a 0-indexed array of integers 
*  nums of length n. You are initially positioned at nums[0].
*
*  Each element nums[i] represents the maximum length of 
*  a forward jump from index i. In other words, if you 
*  are at nums[i], you can jump to any nums[i + j] where:
*     0 <= j <= nums[i] and
*     i + j < n
*  Return the minimum number of jumps to reach nums[n - 1].
*  The test cases are generated such that you can 
*  reach nums[n - 1].
* 
* EX:
*   input: nums = [2,3,1,1,4]
*   out: 2
*   explanation: you take 1 jump form index 0 to 1
*                then you jump 3 spaces from index 1
*                to the end
*/
#include <iostream>
#include <vector>
using namespace std;


int main{
    int arr[] = { 2, 3, 1, 1, 4 };
    int n = sizeof(arr) / sizeof(arr[0]);
  
    vector<int> vect(arr, arr + n);
    return 0;
}


class Solution {
public:
    int minJumps;
    int jump(vector<int>& nums) {
        minJumps = 1e4+1;
        int size = sizeof(nums)/sizeof(int);
        
        solve(0,0, size, nums);
        return minJumps;
        }
        

  // assuming we do not have negative numbers......
    void solve(int jumps, int index,int size,vector<int>& nums){
        int curJumps = jumps+1;

        for (int i = index; i < size-1; i++){
            
            // check if at end
            //cannot jump at all
            if (nums[i] == 0){
                break;
            }
            //can jump
            else{
                for (int j = 1; j <= nums[i]-1; j++){

                    //jumpping short of end
                    if (j+i < size-1){
                        solve(curJumps, i+j,size,nums);
                    }
                    //jumping to the end
                    else if (j+i == size){
                        updateMin(curJumps);             
                        cout << "\n index: " << i;
                        cout << " value: " << nums[i];
                        cout << " jumpcount: " << curJumps << "\n";
                        break;// you found the solution, any increase to j will just overshoot the mark
                    }
                    
                }
            }
            
            }
    }
    void updateMin(int jumps){
        if (jumps < minJumps){
            minJumps = jumps;
        }
    }
};