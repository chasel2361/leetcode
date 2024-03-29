# include <vector>
class Solution {
public:
    int countPrimes(int n) {
        if (n < 3) return 0;
        vector<bool> seen(n, false);
        int ans = 0;
        for (int i=2; i < n; i++){
            if (seen[i]) continue;
            ans++;
            for (long mult=(long)i * i; mult < n; mult += i){
                seen[mult] = true;
            }
        }
        return ans;
    }
};