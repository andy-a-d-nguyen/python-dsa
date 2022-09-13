# Trees

- Tree: A directed, acyclic structure of linked nodes
  - Directed: Has one-way links between nodes
  - Acyclic: No path wraps back around to the same node twice
    - Only one unique path from a node to any other node
- Binary tree: 
  - One where each node has at most two children
  - Each child has only one parent
- Recursive definition: 
  - A tree is either:
    - Empty(nullptr)
    - A root node that contains:
      - Data
      - A left subtree, and
      - A right subtree (left and/or right subtree could be empty)

## Trees in Computer Science

- Folders/files on a computer
- Family genealogy; organizational charts
- AI: Decision trees
- Compilers: Parse tree (a = (b + c) * d)
- Cell phone word auto-completion

## Terminology

- Node: An object containing a data value and left/right children
  - Root: Topmost node of a tree
  - Leaf: A node that has no children
  - Branch: Any internal node; neither the root nor a leaf
  - Parent: A node that refers to this one
  - Child: A node that this node refers to
  - Sibling: A node with a common this
- Subtree: The smaller tree of nodes on the left or right of the current node
- Height: Length of the longest path from the root to any node
- Level or depth: Length of the path from a root to a given node

## Tree Node Structure

```c++
// A TreeNode is one node in a binary tree of integers
struct TreeNode {
  int data;         // data stored at this node
  TreeNode* left;   // pointer to left subtree
  TreeNode* right;  // pointer to right subtree
  
  // Constructs a node with the given data and links
  TreeNode(int data, TreeNode* left, TreeNode* right) {
    this->data = data;
    this->left = left;
    this->right = right;
  }
  
  bool isLeaf() const {
    return left == nullptr && right == nullptr;
  }
};
```