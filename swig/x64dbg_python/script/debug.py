from .. import _x64dbg


class HardwareType:
    HardwareAccess = _x64dbg.HardwareAccess
    HardwareWrite = _x64dbg.HardwareWrite
    HardwareExecute = _x64dbg.HardwareExecute

Wait = _x64dbg.Wait
Run = _x64dbg.Run
Pause = _x64dbg.Pause
Stop = _x64dbg.Stop
StepIn = _x64dbg.StepIn
StepOver = _x64dbg.StepOver
StepOut = _x64dbg.StepOut
SetBreakpoint = _x64dbg.SetBreakpoint
DeleteBreakpoint = _x64dbg.DeleteBreakpoint
SetHardwareBreakpoint = _x64dbg.SetHardwareBreakpoint
DeleteHardwareBreakpoint = _x64dbg.DeleteHardwareBreakpoint
