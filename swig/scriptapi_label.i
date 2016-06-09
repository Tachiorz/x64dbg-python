%{
#include "_scriptapi_label.h"
%}

%rename (Label_Set) Script::Label::Set;
%rename (Label_Get) Script::Label::Get;
%rename (Label_GetInfo) Script::Label::GetInfo;
%rename (Label_Delete) Script::Label::Delete;
%rename (Label_DeleteRange) Script::Label::DeleteRange;
%rename (Label_Clear) Script::Label::Clear;
%rename (Label_GetList) Script::Label::GetList;

%typemap(in,numinputs=0) duint* addr (duint temp) "$1 = &temp;"
SCRIPT_EXPORT bool Script::Label::FromString(const char* label, duint* addr);
%pybuffer_mutable_string(char* text);
SCRIPT_EXPORT bool Script::Label::Get(duint addr, char* text); //text[MAX_LABEL_SIZE]

%include _scriptapi_label.h

%ListInfo_class(Script::Label::LabelInfo,LabelInfoList)
