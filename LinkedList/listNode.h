#define NODE_H
#ifdef NODE_H
#include <bits/stdc++.h>
using namespace std;

template <class T>
class mNode {
public:
  T data;
  mNode* next;
  mNode(T d) {
    data = d;
    next = NULL;
  }
};
#endif
