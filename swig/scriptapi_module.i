%{
#include "_scriptapi_module.h"
%}

%rename (Module_GetList) Script::Module::GetList;

%pybuffer_mutable_string(char* name);
SCRIPT_EXPORT bool Script::Module::NameFromAddr(duint addr, char* name); //name[MAX_MODULE_SIZE]
%pybuffer_mutable_string(char* path);
SCRIPT_EXPORT bool Script::Module::PathFromAddr(duint addr, char* path); //path[MAX_PATH]
%pybuffer_mutable_string(char* name);
%pybuffer_mutable_string(char* path);
SCRIPT_EXPORT bool Script::Module::PathFromName(const char* name, char* path); //path[MAX_PATH]
%pybuffer_mutable_string(char* name);
SCRIPT_EXPORT bool Script::Module::GetMainModuleName(char* name); //name[MAX_MODULE_SIZE]
%pybuffer_mutable_string(char* path);
SCRIPT_EXPORT bool Script::Module::GetMainModulePath(char* path); //path[MAX_PATH]

%include _scriptapi_module.h

%ListInfo_class(Script::Module::ModuleInfo,ModuleInfoList)
%ListInfo_class(Script::Module::ModuleSectionInfo,ModuleSectionInfoList)
