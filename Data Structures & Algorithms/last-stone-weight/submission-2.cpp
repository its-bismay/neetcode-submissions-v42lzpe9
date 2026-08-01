class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int> pq;
        for(auto it:stones){
            pq.push(it);
        }
        while(pq.size()>1){
            int top = pq.top();
            pq.pop();
            int diff = top - pq.top();
            pq.pop();
            if(diff>=0){
                pq.push(diff);
            }
        }
        return pq.top();
    }
};
