%{
#include "_scriptapi_function.h"
%}

%rename (Function_Add) Script::Function::Add;
%rename (Function_Get) Script::Function::Get;
%rename (Function_GetInfo) Script::Function::GetInfo;
%rename (Function_Overlaps) Script::Function::Overlaps;
%rename (Function_Delete) Script::Function::Delete;
%rename (Function_DeleteRange) Script::Function::DeleteRange;
%rename (Function_Clear) Script::Function::Clear;
%rename (Function_GetList) Script::Function::GetList;

%typemap(in) duint* start (duint temp) "$1 = &temp;"
%typemap(in) duint* end (duint temp) "$1 = &temp;"
%typemap(in) duint* instructionCount (duint temp) "$1 = &temp;"
SCRIPT_EXPORT bool Script::Function::Get(duint addr, duint* start = nullptr, duint* end = nullptr, duint* instructionCount = nullptr);

%include _scriptapi_function.h

%ListInfo_class(Script::Function::FunctionInfo,FunctionInfoList)
