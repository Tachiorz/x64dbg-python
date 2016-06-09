%{
#include "_scriptapi_assembler.h"
%}

%pybuffer_mutable_string(unsigned char* dest);
%typemap(in,numinputs=0) int* size (int temp) "$1 = &temp;"
SCRIPT_EXPORT bool Script::Assembler::Assemble(duint addr, unsigned char* dest, int* size, const char* instruction); //dest[16]

%pybuffer_mutable_string(unsigned char* dest);
%pybuffer_mutable_string(char* error);
%typemap(in,numinputs=0) int* size (int temp) "$1 = &temp;"
SCRIPT_EXPORT bool Script::Assembler::AssembleEx(duint addr, unsigned char* dest, int* size, const char* instruction, char* error); //dest[16], error[MAX_ERROR_SIZE]

%pybuffer_mutable_string(char* error);
%typemap(in,numinputs=0) int* size (int temp) "$1 = &temp;"
SCRIPT_EXPORT bool Script::Assembler::AssembleMemEx(duint addr, const char* instruction, int* size, char* error, bool fillnop); //error[MAX_ERROR_SIZE]

%include _scriptapi_assembler.h
