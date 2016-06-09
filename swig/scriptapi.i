%module scriptapi
#define SCRIPT_EXPORT extern

%{
#include "_scriptapi.h"
%}

%include "scriptapi_assembler.i"
%include "scriptapi_argument.i"
%include "scriptapi_bookmark.i"
%include "scriptapi_comment.i"
%include "scriptapi_debug.i"
%include "scriptapi_module.i"
%include "scriptapi_flag.i"
%include "scriptapi_function.i"
%include "scriptapi_gui.i"
%include "scriptapi_label.i"
%include "scriptapi_memory.i"
%include "scriptapi_misc.i"
%include "scriptapi_module.i"
%include "scriptapi_pattern.i"
%include "scriptapi_register.i"
%include "scriptapi_stack.i"
%include "scriptapi_symbol.i"