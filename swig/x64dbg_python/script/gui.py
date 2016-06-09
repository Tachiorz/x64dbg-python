from .. import _x64dbg

Disassembly_SelectionGet = _x64dbg.Gui_Disassembly_SelectionGet
Disassembly_SelectionSet = _x64dbg.Gui_Disassembly_SelectionSet
Disassembly_SelectionGetStart = _x64dbg.Gui_Disassembly_SelectionGetStart
Disassembly_SelectionGetEnd = _x64dbg.Gui_Disassembly_SelectionGetEnd

Dump_SelectionGet = _x64dbg.Gui_Dump_SelectionGet
Dump_SelectionSet = _x64dbg.Gui_Dump_SelectionSet
Dump_SelectionGetStart = _x64dbg.Gui_Dump_SelectionGetStart
Dump_SelectionGetEnd = _x64dbg.Gui_Dump_SelectionGetEnd

Stack_SelectionGet = _x64dbg.Gui_Stack_SelectionGet
Stack_SelectionSet = _x64dbg.Gui_Stack_SelectionSet
Stack_SelectionGetStart = _x64dbg.Gui_Stack_SelectionGetStart
Stack_SelectionGetEnd = _x64dbg.Gui_Stack_SelectionGetEnd

SelectionGet = _x64dbg.Gui_SelectionGet
SelectionSet = _x64dbg.Gui_SelectionSet
SelectionGetStart = _x64dbg.Gui_SelectionGetStart
SelectionGetEnd = _x64dbg.Gui_SelectionGetEnd

Message = _x64dbg.Message
MessageYesNo = _x64dbg.MessageYesNo
InputLine = _x64dbg.InputLine
InputValue = _x64dbg.InputValue
Refresh = _x64dbg.Refresh


class Window:
    DisassemblyWindow = _x64dbg.DisassemblyWindow
    DumpWindow = _x64dbg.DumpWindow
    StackWindow = _x64dbg.StackWindow
