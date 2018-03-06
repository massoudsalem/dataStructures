#include <bits/stdc++.h>
using namespace std;
#ifdef NODE_H
#define NODE_H

template <typename T>
class mNode{
    friend class mLinkedList<T>;
    //making a friend in order to give it an access to all the private and protected member of that class
  private:
    T data{}; //storing data of Type T
    mNode<T>* next{}; //pinter on the next element
};
#endif
