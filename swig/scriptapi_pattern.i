%{
#include "_scriptapi_pattern.h"
%}

%rename (Pattern_Write) Script::Pattern::Write;

%pybuffer_mutable_string(unsigned char* data);
SCRIPT_EXPORT duint Script::Pattern::Find(unsigned char* data, duint datasize, const char* pattern);
%pybuffer_mutable_string(unsigned char* data);
SCRIPT_EXPORT void Script::Pattern::Write(unsigned char* data, duint datasize, const char* pattern);
%pybuffer_mutable_string(unsigned char* data);
SCRIPT_EXPORT bool Script::Pattern::SearchAndReplace(unsigned char* data, duint datasize, const char* searchpattern, const char* replacepattern);

%include _scriptapi_pattern.h
