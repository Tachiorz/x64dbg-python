%{
#include "_scriptapi_symbol.h"
%}

%rename (Symbol_GetList) Script::Symbol::GetList;

%include _scriptapi_symbol.h

%ListInfo_class(Script::Symbol::SymbolInfo,SymbolInfoList)
