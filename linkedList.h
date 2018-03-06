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
    sz=0;
};

bool mLinkedList::empty(){
  return head==NULL; //if the head == null then there is no elments in the list yet.
}

void mLinkedList::print(){
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

void mLinkedList::insert(int index,T x){
  if(index <0){ //insureing the index of the insertion.
    cout<<"Index error please try again"<<endl;
    return;
  }
  mNode<T>* newNode= new mNode<T>*; //Creating node that carry the data needed.
  newNode->data = x;  //Passing data to the newNode
  if(index==0){ //In case of adding in the beginning
    newNode->next = head; //
    head = newNode;
  }else{
    int currIndex=0;
    mNode<T>* currNode=head;
    while (currNode && index >= currIndex) {
      currNode = currNode->next;
      ++currIndex;
    }
    newNode->next=currNode;
    currNode->next=newNode;
  }
  ++sz;
}

int mLinkedList::findNode(T x){
  int currIndex=0;
  mNode<T>* currNode=head;
  while (currNode && currNode->data!=x) {
    currNode = currNode->next;
    ++currIndex;
  }
  return currIndex;
}

int mLinkedList::erase(T x){
  mNode* prevNode = NULL;
  mNode* currNode = NULL;
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

mLinkedList::~mLinkedList(){
  Node* currNode = head, *nextNode = NULL;
  while (currNode != NULL)
  {
    nextNode = currNode->next;
    delete currNode;
    currNode = nextNode;
  }
}

#endif
