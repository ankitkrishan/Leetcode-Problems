//https://leetcode.com/problems/fibonacci-number/
map<int, int>dic{{0, 0}, {1, 1}};
class Solution {
public:
    int fib(int n) {
       if(dic.find(n) != dic.end()){
           return dic[n];
       }else{
           dic[n] = fib(n - 1) + fib(n - 2);
        }
        return dic[n];
    }
};
