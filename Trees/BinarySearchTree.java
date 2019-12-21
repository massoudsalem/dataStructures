import java.util.LinkedList;
import java.util.Queue;

public class BinarySearchTree<T> {
    private class Node<T>{
        private Integer key;
        private T data;
        private Node leftChild;
        private Node rightChild;
        private Node parent;

        public Node(Integer key) {
            this.key = key;
            this.leftChild = null;
            this.rightChild = null;
        }

        public void displayNode(){
            System.out.printf("The key of node is %s the leftChild is %s and the right child is %s.", key, getLeftChild().getKey(), getRightChild().getKey());
        }

        public Node getLeftChild() {
            return leftChild;
        }

        public void setLeftChild(Node leftChild) {
            this.leftChild = leftChild;
        }

        public Node getRightChild() {
            return rightChild;
        }

        public void setRightChild(Node rightChild) {
            this.rightChild = rightChild;
        }
        public Integer getKey(){
            return key;
        }

        public T getData() {
            return data;
        }

        public void setData(T data) {
            this.data = data;
        }

        public Node getParent() {
            return parent;
        }

        public void setParent(Node parent) {
            this.parent = parent;
        }

        @Override
        public String toString() {
            return "Node{" +
                    "key=" + key +
                    '}';
        }
    }
    private Node root;

    public Node getRoot() {
        return root;
    }

    public Node search(Integer key){
        if(root == null)
            return null;
        return supportSearch(root, key);
    }
    private Node supportSearch(Node currentNode, Integer key){
        if(currentNode.getKey() == key)
            return currentNode;
        else if (currentNode.getKey() > key && currentNode.getLeftChild() != null)
            return supportSearch(currentNode.getLeftChild(),key);
        else if (currentNode.getKey() < key && currentNode.getRightChild() != null)
            return supportSearch(currentNode.getRightChild(), key);
        return null;
    }
    public boolean find(Integer key){
        if(search(key) != null)
            return true;
        return false;
    }
    public void insert(Integer key){
        Node<T> node = new Node<>(key);
        if(root == null){
            root = node;
            root.parent = null;
        }
        else if(!find(key))
            supportInsert(root, key);
        else
            System.out.println("The key is already found, Please, enter another one.");
    }
    private void supportInsert(Node currentNode,Integer key){
        if(currentNode.getKey() > key){
            if(currentNode.getLeftChild() == null) {
                currentNode.setLeftChild(new Node(key));
                currentNode.getLeftChild().setParent(currentNode);
            }else {
                supportInsert(currentNode.getLeftChild(), key);
            }
        }else if(currentNode.getKey() < key){
            if(currentNode.getRightChild() == null) {
                currentNode.setRightChild(new Node(key));
                currentNode.getRightChild().setParent(currentNode);
            }else{
                supportInsert(currentNode.getRightChild(), key);
            }
        }
    }

    public Node findMinimum(Node currentNode){
        while(currentNode.getLeftChild() != null)
            currentNode = currentNode.getRightChild();
        return currentNode;
    }

    public Node findMaximum(Node currnetNode){
        while(currnetNode.getLeftChild() != null)
            currnetNode = currnetNode.getRightChild();
        return currnetNode;
    }

    public Node successor(Node currentNode){
        if(currentNode.getRightChild() != null)
            return findMinimum(currentNode.getRightChild());
        Node parent = currentNode.getParent();
        while(parent.getParent() != null && currentNode == parent.getRightChild()){
            currentNode = parent;
            parent = parent.getParent();
        }
        return parent;
    }

    public Node predecessor(Node currentNode){
        if(currentNode.getLeftChild() != null)
            return findMaximum(currentNode);
        Node parent = currentNode.getParent();
        while(parent.getParent() != null && currentNode == parent.getLeftChild()){
            currentNode = parent;
            parent = parent.getParent();
        }
        return parent;
    }

    public void transplant(Node currentNode, Node newSubTreeParent){
        if(currentNode.getParent() == null){
            root = newSubTreeParent;
        }else if(currentNode == currentNode.getParent().getLeftChild()){
            currentNode.getParent().setLeftChild(newSubTreeParent);
        }else{
            currentNode.getParent().setRightChild(newSubTreeParent);
        }
        if(newSubTreeParent != null){
            newSubTreeParent.setParent(currentNode.getParent());
        }
    }

    public void delete(Node nodeToBeDeleted) {
        if (nodeToBeDeleted.getLeftChild() == null) {
            transplant(nodeToBeDeleted, nodeToBeDeleted.getRightChild());
        } else if (nodeToBeDeleted.getRightChild() == null) {
            transplant(nodeToBeDeleted, nodeToBeDeleted.getLeftChild());
        } else {
            Node successor = findMinimum(nodeToBeDeleted);
            if (successor.getParent() != nodeToBeDeleted) {
                transplant(successor, successor.getRightChild());
                successor.setRightChild(nodeToBeDeleted.getRightChild());
                successor.getRightChild().setParent(successor);
            }
            transplant(nodeToBeDeleted, successor);
            successor.setLeftChild(nodeToBeDeleted.getLeftChild());
            successor.getLeftChild().setParent(successor);
        }
    }

    public void printInOrder(Node currentNode){
        if(currentNode == null)
            return;
        printInOrder(currentNode.getLeftChild());
        System.out.print(currentNode + " ");
        printInOrder(currentNode.getRightChild());
    }
    public void printPreOrder(Node currentNode){
        if(currentNode == null)
            return;
        System.out.print(currentNode + " ");
        printPreOrder(currentNode.getLeftChild());
        printPreOrder(currentNode.getRightChild());
    }

    public void printPostOrder(Node currentNode){
        if(currentNode == null)
            return;
        printPostOrder(currentNode.getLeftChild());
        printPostOrder(currentNode.getRightChild());
        System.out.print(currentNode + " ");
    }

    public void printBFS(Node currentNode){
        if(currentNode == null) {
            System.out.println("[ ]");
            return;
        }
        Queue<Node> queue = new LinkedList<>();
        queue.add(currentNode);
        System.out.print("[ ");
        while(!queue.isEmpty()){
            Node front = queue.remove();
            System.out.print(front+" ");
            if(front.getLeftChild() != null)
                queue.add(front.getLeftChild());
            if(front.getRightChild() != null)
                queue.add(front.getRightChild());
        }
        System.out.print("]\n");
    }

    public static void main(String args[]){
        BinarySearchTree binarySearchTree = new BinarySearchTree();
        binarySearchTree.insert(0);
        binarySearchTree.insert(1);
        binarySearchTree.insert(2);
        binarySearchTree.insert(-1);
        binarySearchTree.printBFS(binarySearchTree.getRoot());
        binarySearchTree.delete(binarySearchTree.search(0));
        binarySearchTree.printBFS(binarySearchTree.getRoot());
        binarySearchTree.delete(binarySearchTree.search(-1));
        binarySearchTree.printBFS(binarySearchTree.getRoot());
        binarySearchTree.delete(binarySearchTree.search(1));
        binarySearchTree.printBFS(binarySearchTree.getRoot());
        binarySearchTree.delete(binarySearchTree.search(2));
        binarySearchTree.printBFS(binarySearchTree.getRoot());

    }
}
