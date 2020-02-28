/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
type queue struct {
    treeQueue []*TreeNode
    sequence []rune
}
func (q *queue) pop() (t *TreeNode){
    t = q.treeQueue[0]
    q.treeQueue = q.treeQueue[1:]
    return
}

func (q *queue) push(tree *TreeNode) {
    q.treeQueue = append(q.treeQueue, tree)
} 

func (q *queue)treeSlice (tree *TreeNode) { 
    if tree.Left != nil {q.sequence = append(q.sequence, rune(tree.Left.Val))} else {q.sequence = append(q.sequence, 'n')}
    if tree.Right !=nil {q.sequence = append(q.sequence, rune(tree.Right.Val))} else {q.sequence = append(q.sequence, 'n')}
    
    q.push(tree.Left)
    q.push(tree.Right)
}

func (q *queue)formSequence (tree *TreeNode) (check bool){
    check = true
    for len(q.treeQueue) > 0 {

        if  q.sequence[0] == 'x' {
            q.sequence = q.sequence[1:]
            // fmt.Println(q.sequence)
            check = check && sym(q.sequence)
            q.sequence = append(q.sequence, 'x')
        }
        
        t := q.pop()
        
        q.sequence = q.sequence[1:]
        
        
        if t != nil {
            q.treeSlice(t)
        }
        
    }
    return check
}

func sym(s []rune) bool {
    first := 0
    last := len(s)-1
    for first < last {
        if s[first] != s[last] {
            return false
        }
        first ++
        last --
    }
    return true
}

func isSymmetric(root *TreeNode) (check bool) {
    if root == nil {
        return true
    }
    if root.Left == nil && root.Right == nil {
        return true
    }
    if root.Left == nil || root.Right == nil {
        return false
    }
    if root.Left.Val != root.Right.Val {
        return false
    }
    var q = queue{sequence:[]rune{}}
    q.sequence = append(q.sequence, rune(root.Left.Val))
    q.sequence = append(q.sequence, rune(root.Right.Val))
    q.sequence = append(q.sequence, 'x')

    q.push(root.Left)
    q.push(root.Right)
    check = q.formSequence(root)
    
    return check
}
