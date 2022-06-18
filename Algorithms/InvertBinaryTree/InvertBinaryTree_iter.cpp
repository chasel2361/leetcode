/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if (!root) return NULL;
        std::queue<TreeNode*> q;
        
        q.push(root);
        while (q.size() > 0){
            TreeNode* ptr = q.front();
            q.pop();
            std::swap(ptr->left, ptr->right);
            if (ptr->left) q.push(ptr->left);
            if (ptr->right) q.push(ptr->right);
        }
        return root;
    }
};