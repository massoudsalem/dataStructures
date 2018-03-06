#include "listNode.h"
using namespace std;
#ifdef _LINKEDLIST_H_
#define _LINKEDLIST_H_

template <typename T>
class mLinkedList{
  friend class mNode<T>;
  public:
    mLinkedList();
    ~mLinkedList();
    bool empty();
    void print();
    int size();
    void insert(int index,T x);
    void earse(T x);
    mNode<T>* findNode();
  private:
    mNode<T>* head;  //head of the list.
    int sz=0;
};

template <typename T>
bool mLinkedList<T>::empty(){
  return head==NULL; //if the head == null then there is no elments in the list yet.
}

template <typename T>
void mLinkedList<T>::print(){
  mNode<T>* currNode=head; //start with the head of the list
  int index=0;  //zero based linkedList
  if(empty()){
    printf("This list is empty\n");
  }else{
    while(currNode){ //while currNode is not equal to null
      printf("List[%d] = ",index);  //display index of the element in the list.
      cout<<currNode->data <<endl;  //display the contant of the element.
      currNode = *currNode->next;   //going to the next element.
    }
  }
}

int size(){
  return sz;
}

template <typename T>
void mLinkedList<T>::insert(int index,T x){
  if(index <0){ //insureing the index of the insertion.
    cout<<"Index error please try again"<<endl;
    return;
  }
  mNode<T>* newNode= new mNode<T>*; //Creating node that carry the data needed.
  newNode->data = x;  //Passing data to the newNode
  if(index==0){ //In case of adding in the beginning.
    newNode->next = head; //moving head data.
    head = newNode; //replace head data with the newone.
  }else{
    int currIndex=0;  //assume that current index is 0.
    mNode<T>* currNode=head;  //start from head.
    while (currNode && index >= currIndex) {
      //while currNode!=NULL then the current node is not the last node or the targeted element
      currNode = currNode->next; //moving current node.
      ++currIndex; //increasing the index.
    }
    newNode->next=currNode->next; //moving currNode next
    currNode->next=newNode; //insert after the currNode
  }
  ++sz;//increasing the size of the linkedList
}

template <typename T>
int mLinkedList<T>::findNode(T x){
  int currIndex=0;
  mNode<T>* currNode=head;
  while (currNode && currNode->data!=x) {
    currNode = currNode->next;
    ++currIndex;
  }
  return currIndex;
}

template <typename T>
int mLinkedList<T>::erase(T x){
  mNode<T>* prevNode = NULL;
  mNode<T>* currNode = NULL;
  currIndex=0;
  while (currNode && currNode->data!=x) {
    prevNode = currNode;
    currNode = currNode->next;
    ++currIndex;
  }
  if(currNode){
    if(prevNode){
      prevNode=currNode->next
    }else{
      head=currNode->next;
      delete currNode;
    }
    return currIndex;
  }
  cout<<"element is not found"<<endl;
  return -1;
}

template <typename T>
void mLinkedList<T>::~mLinkedList(){
  Node<T>* currNode = head, *nextNode = NULL;
  while (currNode != NULL)
  {
    nextNode = currNode->next;
    delete currNode;
    currNode = nextNode;
  }
}

#endif
