import ctypes
import _x64dbg

GUI_MAX_LINE_SIZE = 65536


def DbgIsDebugging():
    return _x64dbg.DbgIsDebugging()


def GuiGetLineWindow(title=''):
    line = ctypes.create_string_buffer(GUI_MAX_LINE_SIZE)
    return_value = _x64dbg.GuiGetLineWindow("%s" % title, line)
    if return_value:
        return line.value


def GuiGetWindowHandle():
    return _x64dbg.GuiGetWindowHandle()


#Debugger functions
DbgMemRead = _x64dbg.DbgMemRead
DbgMemWrite = _x64dbg.DbgMemWrite
DbgMemGetPageSize = _x64dbg.DbgMemGetPageSize
DbgMemFindBaseAddr = _x64dbg.DbgMemFindBaseAddr
DbgCmdExec = _x64dbg.DbgCmdExec
DbgCmdExecDirect = _x64dbg.DbgCmdExecDirect
DbgIsValidExpression = _x64dbg.DbgIsValidExpression
DbgIsJumpGoingToExecute = _x64dbg.DbgIsJumpGoingToExecute
DbgSetLabelAt = _x64dbg.DbgSetLabelAt
DbgGetCommentAt = _x64dbg.DbgGetCommentAt
DbgSetCommentAt = _x64dbg.DbgSetCommentAt
DbgGetBookmarkAt = _x64dbg.DbgGetBookmarkAt
DbgSetBookmarkAt = _x64dbg.DbgSetBookmarkAt
DbgGetModuleAt = _x64dbg.DbgGetModuleAt
DbgValFromString = _x64dbg.DbgValFromString
DbgValToString = _x64dbg.DbgValToString
DbgMemIsValidReadPtr = _x64dbg.DbgMemIsValidReadPtr
DbgGetBranchDestination = _x64dbg.DbgGetBranchDestination
DbgScriptLoad = _x64dbg.DbgScriptLoad
DbgScriptUnload = _x64dbg.DbgScriptUnload
DbgScriptRun = _x64dbg.DbgScriptRun
DbgScriptStep = _x64dbg.DbgScriptStep
DbgScriptBpToggle = _x64dbg.DbgScriptBpToggle
DbgScriptBpGet = _x64dbg.DbgScriptBpGet
DbgScriptCmdExec = _x64dbg.DbgScriptCmdExec
DbgScriptAbort = _x64dbg.DbgScriptAbort
DbgScriptSetIp = _x64dbg.DbgScriptSetIp
DbgAssembleAt = _x64dbg.DbgAssembleAt
DbgModBaseFromName = _x64dbg.DbgModBaseFromName
DbgSettingsUpdated = _x64dbg.DbgSettingsUpdated
DbgMenuEntryClicked = _x64dbg.DbgMenuEntryClicked
DbgFunctionGet = _x64dbg.DbgFunctionGet
DbgFunctionOverlaps = _x64dbg.DbgFunctionOverlaps
DbgFunctionAdd = _x64dbg.DbgFunctionAdd
DbgFunctionDel = _x64dbg.DbgFunctionDel
DbgLoopGet = _x64dbg.DbgLoopGet
DbgLoopOverlaps = _x64dbg.DbgLoopOverlaps
DbgLoopAdd = _x64dbg.DbgLoopAdd
DbgLoopDel = _x64dbg.DbgLoopDel
DbgIsRunLocked = _x64dbg.DbgIsRunLocked
DbgIsBpDisabled = _x64dbg.DbgIsBpDisabled
DbgSetAutoCommentAt = _x64dbg.DbgSetAutoCommentAt
DbgClearAutoCommentRange = _x64dbg.DbgClearAutoCommentRange
DbgSetAutoLabelAt = _x64dbg.DbgSetAutoLabelAt
DbgClearAutoLabelRange = _x64dbg.DbgClearAutoLabelRange
DbgSetAutoBookmarkAt = _x64dbg.DbgSetAutoBookmarkAt
DbgClearAutoBookmarkRange = _x64dbg.DbgClearAutoBookmarkRange
DbgSetAutoFunctionAt = _x64dbg.DbgSetAutoFunctionAt
DbgClearAutoFunctionRange = _x64dbg.DbgClearAutoFunctionRange
DbgGetStringAt = _x64dbg.DbgGetStringAt

#GUI functions
GuiDisasmAt = _x64dbg.GuiDisasmAt
GuiAddLogMessage = _x64dbg.GuiAddLogMessage
GuiLogClear = _x64dbg.GuiLogClear
GuiUpdateAllViews = _x64dbg.GuiUpdateAllViews
GuiUpdateRegisterView = _x64dbg.GuiUpdateRegisterView
GuiUpdateDisassemblyView = _x64dbg.GuiUpdateDisassemblyView
GuiUpdateBreakpointsView = _x64dbg.GuiUpdateBreakpointsView
GuiUpdateWindowTitle = _x64dbg.GuiUpdateWindowTitle
GuiDumpAt = _x64dbg.GuiDumpAt
GuiScriptAdd = _x64dbg.GuiScriptAdd
GuiScriptClear = _x64dbg.GuiScriptClear
GuiScriptSetIp = _x64dbg.GuiScriptSetIp
GuiScriptError = _x64dbg.GuiScriptError
GuiScriptSetTitle = _x64dbg.GuiScriptSetTitle
GuiScriptSetInfoLine = _x64dbg.GuiScriptSetInfoLine
GuiScriptMessage = _x64dbg.GuiScriptMessage
GuiScriptMsgyn = _x64dbg.GuiScriptMsgyn
GuiScriptEnableHighlighting = _x64dbg.GuiScriptEnableHighlighting
GuiSymbolLogAdd = _x64dbg.GuiSymbolLogAdd
GuiSymbolLogClear = _x64dbg.GuiSymbolLogClear
GuiSymbolSetProgress = _x64dbg.GuiSymbolSetProgress
GuiSymbolRefreshCurrent = _x64dbg.GuiSymbolRefreshCurrent
GuiReferenceAddColumn = _x64dbg.GuiReferenceAddColumn
GuiReferenceSetRowCount = _x64dbg.GuiReferenceSetRowCount
GuiReferenceGetRowCount = _x64dbg.GuiReferenceGetRowCount
GuiReferenceDeleteAllColumns = _x64dbg.GuiReferenceDeleteAllColumns
GuiReferenceInitialize = _x64dbg.GuiReferenceInitialize
GuiReferenceSetCellContent = _x64dbg.GuiReferenceSetCellContent
GuiReferenceReloadData = _x64dbg.GuiReferenceReloadData
GuiReferenceSetSingleSelection = _x64dbg.GuiReferenceSetSingleSelection
GuiReferenceSetProgress = _x64dbg.GuiReferenceSetProgress
GuiReferenceSetSearchStartCol = _x64dbg.GuiReferenceSetSearchStartCol
GuiStackDumpAt = _x64dbg.GuiStackDumpAt
GuiUpdateDumpView = _x64dbg.GuiUpdateDumpView
GuiUpdateThreadView = _x64dbg.GuiUpdateThreadView
GuiUpdateMemoryView = _x64dbg.GuiUpdateMemoryView
GuiAddRecentFile = _x64dbg.GuiAddRecentFile
GuiSetLastException = _x64dbg.GuiSetLastException
GuiGetDisassembly = _x64dbg.GuiGetDisassembly
GuiMenuAdd = _x64dbg.GuiMenuAdd
GuiMenuAddEntry = _x64dbg.GuiMenuAddEntry
GuiMenuAddSeparator = _x64dbg.GuiMenuAddSeparator
GuiMenuClear = _x64dbg.GuiMenuClear
GuiAutoCompleteAddCmd = _x64dbg.GuiAutoCompleteAddCmd
GuiAutoCompleteDelCmd = _x64dbg.GuiAutoCompleteDelCmd
GuiAutoCompleteClearAll = _x64dbg.GuiAutoCompleteClearAll
GuiAddStatusBarMessage = _x64dbg.GuiAddStatusBarMessage
GuiUpdateSideBar = _x64dbg.GuiUpdateSideBar
GuiRepaintTableView = _x64dbg.GuiRepaintTableView
GuiUpdatePatches = _x64dbg.GuiUpdatePatches
GuiUpdateCallStack = _x64dbg.GuiUpdateCallStack
GuiUpdateMemoryView = _x64dbg.GuiUpdateMemoryView
