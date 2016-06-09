%module bridgelist
%{
#include "bridgemain.h"
#include "bridgelist.h"
%}

%include bridgelist.h

%define %ListInfo_class(TYPE,NAME)
  %feature("python:slot", "mp_length", functype="lenfunc") __len__;
  %feature("python:slot", "sq_item", functype="ssizeargfunc") NAME::__getitem__;
  %feature("python:slot", "sq_ass_item", functype="ssizeobjargproc") NAME::__setitem__;

%inline %{
typedef struct {
    int count;
    TYPE *el;
} NAME;
%}

%extend NAME {

  NAME(ListInfo* l) {
      NAME *arr = %new_instance(NAME);
      arr->el = (TYPE*)(l->data);
      arr->count = l->count;
      return arr;
  }

  ~NAME() {
      BridgeFree((void*)self->el);
      %delete(self);
  }
  
  TYPE __getitem__(size_t index) {
      return self->el[index];
  }

  unsigned int __len__() {
      return self->count;
  }

  void __setitem__(size_t index, TYPE value) {
      self->el[index] = value;
  }
};

%types(NAME = TYPE);

%enddef
