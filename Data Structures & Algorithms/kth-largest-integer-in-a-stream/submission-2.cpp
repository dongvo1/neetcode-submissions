class KthLargest {
    std::priority_queue<int, std::vector<int>, std::greater<int>> pq;
    int k;
public:
    KthLargest(int k, vector<int>& nums) {
        this->k = k;
        // third largest
        // three numbers into the min heap
        // size > 3 -> pop
        // std::priority_queue<int, std::vector<int>, std::greater<int>> pq;
        for (int n : nums) {
            pq.push(n);
            if (pq.size() > k) {
                pq.pop();
            }
        }
    }
    
    int add(int val) {
        pq.push(val);
        if (pq.size() > k) pq.pop();
        return pq.top();
    }
};
