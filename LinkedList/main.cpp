#include "linkedList.h"
#include <bits/stdc++.h>
using namespace std;

int main(){
  mLinkedList<int> intlist;
 // intlist.InsertNode(0,4);
 // intlist.InsertNode(1,5);
  intlist.insert(0,5);
  intlist.insert(1,4);
  intlist.insert(2,6);
  intlist.insert(3,4);
  intlist.print();
  return 0;
}
