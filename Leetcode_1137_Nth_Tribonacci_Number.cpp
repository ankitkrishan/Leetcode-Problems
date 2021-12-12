//https://leetcode.com/problems/n-th-tribonacci-number/
map<int, int>dic{{0, 0}, {1, 1}, {2, 1}};
class Solution {
public:
    int tribonacci(int n) {
        if(dic.find(n) != dic.end()){
           return dic[n];
       }else{
           dic[n] = tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3);
        }
        return dic[n];
    }
};
