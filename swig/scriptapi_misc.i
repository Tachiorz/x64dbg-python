%{
#include "_scriptapi_misc.h"
%}

%typemap(in,numinputs=0) duint* value (duint temp) "$1 = &temp;"
SCRIPT_EXPORT bool Script::Misc::ParseExpression(const char* expression, duint* value);

// TODO: ??
SCRIPT_EXPORT void* Script::Misc::Alloc(duint size);
SCRIPT_EXPORT void Script::Misc::Free(void* ptr);

%include _scriptapi_misc.h
