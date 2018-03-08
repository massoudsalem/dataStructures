#define _LINKEDLIST_H_
#ifdef _LINKEDLIST_H_

#include "listNode.h"
using namespace std;

template <class T>
class mLinkedList{
  public:
    mLinkedList(){
      head=NULL;
      sz=0;
    }
    bool empty(){
      return head==NULL; //if the head == null then there is no elments in the list yet.
    }

    void print(){
      mNode<T>* currNode=head; //start with the head of the list
      int index=0;  //zero based linkedList
      if(empty()){
        printf("This list is empty\n");
      }else{
        while(currNode){ //while currNode is not equal to null
          printf("List[%d] = ",index);  //display index of the element in the list.
          cout<< currNode->data <<endl;  //display the contant of the element.
          currNode = currNode->next;   //going to the next element.
          ++index;
        }
      }
    }

    int size(){
      return sz;
    }

    void insert(int index,T x){
      if(index <0){ //insureing the index of the insertion.
        cout<<"Index error please try again"<<endl;
        return;
      }
      mNode<T>* newNode = new mNode<T>(x); //Creating node that carry the data needed.

      if(index==0){ //In case of adding in the beginning.
        newNode->next = head; //moving head data.
        head = newNode; //replace head data with the newone.
      }else{
        int currIndex=0;  //assume that current index is 0.
        mNode<T>* currNode=head;  //start from head.
        while (currNode && index > currIndex + 1) {
          //while currNode!=NULL then the current node is not the last node or the targeted element
          currNode = currNode->next; //moving current node.
          ++currIndex; //increasing the index.
        }
        newNode->next=currNode->next; //moving currNode next
        currNode->next = newNode; //insert after the currNode
      }
      ++sz;//increasing the size of the linkedList
    }

    mNode<T>* findNode(T x){
      int currIndex=0;
      mNode<T>* currNode=head;
      while (currNode && currNode->data!=x) {
        currNode = currNode->next;
        ++currIndex;
      }
      return currIndex;
    }

    int erase(T x){
      mNode<T>* prevNode = NULL;
      mNode<T>* currNode = NULL;
      int currIndex=0;
      while (currNode && currNode->data!=x) {
        prevNode = currNode;
        currNode = currNode->next;
        ++currIndex;
      }
      if(currNode){
        if(prevNode){
          prevNode=currNode->next;
        }else{
          head=currNode->next;
          delete currNode;
        }
        return currIndex;
      }
      cout<<"element is not found"<<endl;
      return -1;
    }

    ~mLinkedList(){
      mNode<T>* currNode = head, *nextNode = NULL;
      while (currNode != NULL)
      {
        nextNode = currNode->next;
        delete currNode;
        currNode = nextNode;
      }
    }
  private:
    mNode<T>* head;  //head of the list.
    int sz;
};

#endif
