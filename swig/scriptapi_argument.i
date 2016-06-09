%{
#include "_scriptapi_argument.h"
%}

%rename (Argument_Add) Script::Argument::Add;
%rename (Argument_Get) Script::Argument::Get;
%rename (Argument_GetInfo) Script::Argument::GetInfo;
%rename (Argument_Overlaps) Script::Argument::Overlaps;
%rename (Argument_Delete) Script::Argument::Delete;
%rename (Argument_DeleteRange) Script::Argument::DeleteRange;
%rename (Argument_Clear) Script::Argument::Clear;
%rename (Argument_GetList) Script::Argument::GetList;

%typemap(in) duint* start (duint temp) "$1 = &temp;"
%typemap(in) duint* end (duint temp) "$1 = &temp;"
%typemap(in) duint* instructionCount (duint temp) "$1 = &temp;"
SCRIPT_EXPORT bool Script::Argument::Get(duint addr, duint* start = nullptr, duint* end = nullptr, duint* instructionCount = nullptr);

%include _scriptapi_argument.h

%ListInfo_class(Script::Argument::ArgumentInfo,ArgumentInfoList)
