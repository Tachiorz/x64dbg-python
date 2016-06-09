%{
#include "_scriptapi_gui.h"
%}

%rename (Gui_Disassembly_SelectionGet) Script::Gui::Disassembly::SelectionGet;
%rename (Gui_Disassembly_SelectionSet) Script::Gui::Disassembly::SelectionSet;
%rename (Gui_Disassembly_SelectionGetStart) Script::Gui::Disassembly::SelectionGetStart;
%rename (Gui_Disassembly_SelectionGetEnd) Script::Gui::Disassembly::SelectionGetEnd;

%rename (Gui_Dump_SelectionGet) Script::Gui::Dump::SelectionGet;
%rename (Gui_Dump_SelectionSet) Script::Gui::Dump::SelectionSet;
%rename (Gui_Dump_SelectionGetStart) Script::Gui::Dump::SelectionGetStart;
%rename (Gui_Dump_SelectionGetEnd) Script::Gui::Dump::SelectionGetEnd;

%rename (Gui_Stack_SelectionGet) Script::Gui::Stack::SelectionGet;
%rename (Gui_Stack_SelectionSet) Script::Gui::Stack::SelectionSet;
%rename (Gui_Stack_SelectionGetStart) Script::Gui::Stack::SelectionGetStart;
%rename (Gui_Stack_SelectionGetEnd) Script::Gui::Stack::SelectionGetEnd;

%rename (Gui_SelectionGet) Script::Gui::SelectionGet;
%rename (Gui_SelectionSet) Script::Gui::SelectionSet;
%rename (Gui_SelectionGetStart) Script::Gui::SelectionGetStart;
%rename (Gui_SelectionGetEnd) Script::Gui::SelectionGetEnd;

%typemap(in,numinputs=0) duint* start (duint temp) "$1 = &temp;"
%typemap(in,numinputs=0) duint* end (duint temp) "$1 = &temp;"
SCRIPT_EXPORT bool Script::Gui::Disassembly::SelectionGet(duint* start, duint* end);
%typemap(in,numinputs=0) duint* start (duint temp) "$1 = &temp;"
%typemap(in,numinputs=0) duint* end (duint temp) "$1 = &temp;"
SCRIPT_EXPORT bool Script::Gui::Dump::SelectionGet(duint* start, duint* end);
%typemap(in,numinputs=0) duint* start (duint temp) "$1 = &temp;"
%typemap(in,numinputs=0) duint* end (duint temp) "$1 = &temp;"
SCRIPT_EXPORT bool Script::Gui::Stack::SelectionGet(duint* start, duint* end);
%typemap(in,numinputs=0) duint* start (duint temp) "$1 = &temp;"
%typemap(in,numinputs=0) duint* end (duint temp) "$1 = &temp;"
SCRIPT_EXPORT bool Script::Gui::SelectionGet(Window window, duint* start, duint* end);

%pybuffer_mutable_string(char* text);
SCRIPT_EXPORT bool Script::Gui::InputLine(const char* title, char* text); //text[GUI_MAX_LINE_SIZE]
%typemap(in,numinputs=0) duint* value (duint temp) "$1 = &temp;"
SCRIPT_EXPORT bool Script::Gui::InputValue(const char* title, duint* value);

%ignore Script::Gui::AddQWidgetTab;
%ignore Script::Gui::ShowQWidgetTab;
%ignore Script::Gui::CloseQWidgetTab;

%include _scriptapi_gui.h
