%{
#include "_scriptapi_flag.h"
%}

%rename (Flag_Set) Script::Flag::Set;
%rename (Flag_Get) Script::Flag::Get;

%include _scriptapi_flag.h
