#include "linkedList.h"
#include <bits/stdc++.h>
using namespace std;
/*
Testing mlinkedList.
*/
int main(){
  mLinkedList<int>* intlist= new mLinkedList<int>();
  intlist->insert(0,5);
  intlist->insert(1,4);
  intlist->insert(2,6);
  intlist->insert(2,7);
  intlist->insert(0,7);
  intlist->insert(3,4);
  intlist->insert(20,4);
  printf("The list contains:\n");
  intlist->print();
  printf("Size of List is %d\n",intlist->size());
  int idx=intlist->erase(7);
  (idx!=-1) ? printf("The List[%d] is erased\n",idx):printf("Element '%d' is not found\n",7);
  idx=intlist->erase(7);
  (idx!=-1) ? printf("The List[%d] is erased\n",idx):printf("Element '%d' is not found\n",7);
  idx=intlist->erase(7);
  (idx!=-1) ? printf("The List[%d] is erased\n",idx):printf("Element '%d' is not found\n",7);
  printf("\nNow the list contains:\n");
  intlist->print();
  printf("Size of List is %d\n",intlist->size());
  puts("\nFinding 6 and 0:");
  idx=intlist->findNode(6);
  (idx!=-1) ? printf("Element '%d' found at %d\n",6,idx):printf("Element '%d' is not found\n",6);
  idx=intlist->findNode(0);
  (idx!=-1) ? printf("Element '%d' found at %d\n",0,idx):printf("Element '%d' is not found\n",0);
  idx=intlist->findNode(0);
  intlist->empty() ? puts("list is empty"):puts("list isn't empty");
  intlist->destroymLinkedList();
  idx=intlist->findNode(6);
  (idx!=-1) ? printf("Element '%d' found at %d\n",6,idx):printf("Element '%d' is not found\n",6);
  intlist->empty() ? puts("list is empty"):puts("list isn't empty");
  return 0;
}
