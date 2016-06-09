from .. import _x64dbg


class FlagEnum:
    ZF = _x64dbg.ZF
    OF = _x64dbg.OF
    CF = _x64dbg.CF
    PF = _x64dbg.PF
    SF = _x64dbg.SF
    TF = _x64dbg.TF
    AF = _x64dbg.AF
    DF = _x64dbg.DF
    IF = _x64dbg.IF

Set = _x64dbg.Flag_Set
Get = _x64dbg.Flag_Get
GetZF = _x64dbg.GetZF
SetZF = _x64dbg.SetZF
GetOF = _x64dbg.GetOF
SetOF = _x64dbg.SetOF
GetCF = _x64dbg.GetCF
SetCF = _x64dbg.SetCF
GetPF = _x64dbg.GetPF
SetPF = _x64dbg.SetPF
GetSF = _x64dbg.GetSF
SetSF = _x64dbg.SetSF
GetTF = _x64dbg.GetTF
SetTF = _x64dbg.SetTF
GetAF = _x64dbg.GetAF
SetAF = _x64dbg.SetAF
GetDF = _x64dbg.GetDF
SetDF = _x64dbg.SetDF
GetIF = _x64dbg.GetIF
SetIF = _x64dbg.SetIF
