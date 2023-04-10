from enum import Enum


class FileType(Enum):
    PEERSTAT = 1
    LOOPSTAT = 2


class FirstByte(Enum):
    BCST = 0x08
    REACH = 0x10
    AUTHENB = 0x20
    AUTH = 0x40
    CONFIG = 0x80


class SecondByte(Enum):
    SEL_REJECT = 0x00
    SEL_FALSETICK = 0x01
    SEL_EXCESS = 0x02
    SEL_OUTLYER = 0x03
    SEL_CANDIDATE = 0x04
    SEL_BACKUP = 0x05
    SEL_SYSPEER = 0x06
    SEL_PPSPEER = 0x07


class FourthByte(Enum):
    MOBILIZE = 0x01
    DEMOBILIZE = 0x02
    UNREACHABLE = 0x03
    REACHABLE = 0x04
    RESTART = 0x05
    NO_REPLY = 0x06
    RATE_EXCEEDED = 0x07
    ACCESS_DENIED = 0x08
    LEAP_ARMED = 0x09
    SYS_PEER = 0x0A
    CLOCK_EVENT = 0x0B
    BAD_AUTH = 0x0C
    POPCORN = 0x0D
    INTERLEAVE_MODE = 0x0E
    INTERLEAVE_ERROR = 0x0F


class FirstResults(dict):
    def __init__(self):
        self[FirstByte.BCST.value] = "bcst: broadcast assocation"
        self[FirstByte.REACH.value] = "reach: host reachable"
        self[FirstByte.AUTHENB.value] = "authenb: authentication enabled"
        self[FirstByte.AUTH.value] = "auth: authentication ok"
        self[FirstByte.CONFIG.value] = "config: persistent association"
        super().__init__()


class SecondResults(dict):
    def __init__(self):
        self[SecondByte.SEL_REJECT.value] = "sel_reject\tdiscarded as not valid"
        self[SecondByte.SEL_FALSETICK.value] = "sel_falsetick\tdiscarded by intersection algorithm"
        self[SecondByte.SEL_EXCESS.value] = "sel_excess\tdiscarded by table overflow"
        self[SecondByte.SEL_OUTLYER.value] = "sel_outlyer\tdiscarded by the cluster algorithm"
        self[SecondByte.SEL_CANDIDATE.value] = "sel_candidate\tincluded by the combine algorithm"
        self[SecondByte.SEL_BACKUP.value] = "sel_backup\tbackup (more than tos maxclock sources)"
        self[SecondByte.SEL_SYSPEER.value] = "sel_sys.peer\tsystem peer"
        self[SecondByte.SEL_PPSPEER.value] = "sel_pps.peer\tPPS peer (when the prefer peer is valid)"
        super().__init__()


class FourthResults(dict):
    def __init__(self):
        self[FourthByte.MOBILIZE.value] = "mobilze\tassociation mobilized"
        self[FourthByte.DEMOBILIZE.value] = "demobilize\tassociation demobilized"
        self[FourthByte.UNREACHABLE.value] = "unreachable\tserver unreachable"
        self[FourthByte.REACHABLE.value] = "reachable\tserver reachable"
        self[FourthByte.RESTART.value] = "restart\tassociation restart"
        self[FourthByte.NO_REPLY.value] = "no_reply\tno server found (ntpdate mode)"
        self[FourthByte.RATE_EXCEEDED.value] = "rate_exceeded\trate exceeded (kiss code RATE)"
        self[FourthByte.ACCESS_DENIED.value] = "access_denied\taccess denied (kiss code DENY)"
        self[FourthByte.LEAP_ARMED.value] = "leap_armed\tleap armed from server LI code"
        self[FourthByte.SYS_PEER.value] = "sys_peer\tbecome system peer"
        self[FourthByte.CLOCK_EVENT.value] = "clock_event\tsee clock status word"
        self[FourthByte.BAD_AUTH.value] = "bad_auth\tauthentication failure"
        self[FourthByte.POPCORN.value] = "popcorn\tpopcorn spike suppressor"
        self[FourthByte.INTERLEAVE_MODE.value] = "interleave_mode\tentering interleave mode"
        self[FourthByte.INTERLEAVE_ERROR.value] = "interleave_error\tinterleave error (recovered)"

        super().__init__()
