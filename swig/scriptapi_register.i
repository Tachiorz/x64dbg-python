%{
#include "_scriptapi_register.h"
%}

%rename (Register_Set) Script::Register::Set;
%rename (Register_Get) Script::Register::Get;

%include _scriptapi_register.h
