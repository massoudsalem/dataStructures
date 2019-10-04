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
      if(index>sz){
        index=sz; //inorder to add element in the last palce of the list.
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

    int findNode(T x){
      int currIndex=0;  //start index form 0.
      mNode<T>* currNode=head; //inialize the currNode with the head of the linkedList.
      while (currNode && currNode->data!=x) { //break the loop if you find the targeted element or the list is finished without finding it.
        currNode = currNode->next; //rolling of the list.
        ++currIndex; //increasing the index with rolling.
      }
      return (currNode ? currIndex:-1);//return index if the targeted element found.
    }

    int erase(T x){
      mNode<T>* prevNode = NULL;  //inialize the prevNode with null prevNode is previous node.
      mNode<T>* currNode = head;  //inialize the currNode with head currNode is currnet node node.
      int currIndex=0;  //start index form 0.
      while (currNode && currNode->data!=x) { //break the loop if you find the targeted element or the list is finished without finding it.
        prevNode = currNode;  //moving nodes pointers.
        currNode = currNode->next;
        ++currIndex;  //increasing the index.
      }
      if(currNode){ // if it's not the end of the list.
        if(prevNode){ //move the prevNode points on the currNode next.
          prevNode->next=currNode->next;
        }else{  //then the targeted node is the '0' index one.
          head=currNode->next;
          delete currNode;
        }
        --sz; //resize the list by decreasing it by 1.
        return currIndex; //return the index of the erased element.
      }
      return -1;  //return the -1 if the element isn't found.
    }

    void destroymLinkedList(){
      mNode<T>* currNode = head, *nextNode = NULL;  //start the list form head and inialize the next element with null.
      while (currNode)  //loop breaks when the null element found "last element" on the list
      {
        nextNode = currNode->next;  //rolling on the list
        delete currNode;  //delete the current node
        currNode = nextNode;  //move the current pointer
      }
      head=NULL;
    }

    ~mLinkedList(){
      mNode<T>* currNode = head, *nextNode = NULL;  //start the list form head and inialize the next element with null.
      while (currNode)  //loop breaks when the null element found "last element" on the list
      {
        nextNode = currNode->next;  //rolling on the list
        delete currNode;  //delete the current node
        currNode = nextNode;  //move the current pointer
      }
      delete head;  //deleting list head.
    }
  private:
    mNode<T>* head;  //head of the list.
    int sz; //size of the list
};

#endif
