%{
#include "_scriptapi_memory.h"
%}

%rename (Memory_Write) Script::Memory::Write;

%typemap(in,numinputs=0) duint* sizeRead (duint temp) "$1 = &temp;"
%pybuffer_mutable_string(void* data);
SCRIPT_EXPORT bool Script::Memory::Read(duint addr, void* data, duint size, duint* sizeRead);

%typemap(in,numinputs=0) duint* sizeWritten (duint temp) "$1 = &temp;"
%pybuffer_mutable_string(void* data);
SCRIPT_EXPORT bool Script::Memory::Write(duint addr, const void* data, duint size, duint* sizeWritten);

%include _scriptapi_memory.h
