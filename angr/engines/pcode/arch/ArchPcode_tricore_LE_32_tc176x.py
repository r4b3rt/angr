###
### This file was automatically generated
###

from archinfo.arch import register_arch, Endness, Register

from .common import ArchPcode


class ArchPcode_tricore_LE_32_tc176x(ArchPcode):
    name = 'tricore:LE:32:tc176x'
    pcode_arch = 'tricore:LE:32:tc176x'
    description = 'Siemens Tricore Embedded Processor TC1762/TC1766'
    bits = 32
    ip_offset = 0xfe08
    sp_offset = 0xffa8
    bp_offset = sp_offset
    instruction_endness = Endness.LE
    register_list = [
        Register('contextreg', 4, 0x0),
        Register('task_asi', 4, 0x8004),
        Register('pma0', 4, 0x8100),
        Register('pma1', 4, 0x8104),
        Register('pma2', 4, 0x8108),
        Register('dcon2', 4, 0x9000),
        Register('dcon1', 4, 0x9008),
        Register('smacon', 4, 0x900c),
        Register('dstr', 4, 0x9010),
        Register('datr', 4, 0x9018),
        Register('deadd', 4, 0x901c),
        Register('diear', 4, 0x9020),
        Register('dietr', 4, 0x9024),
        Register('dcon0', 4, 0x9040),
        Register('pstr', 4, 0x9200),
        Register('pcon1', 4, 0x9204),
        Register('pcon2', 4, 0x9208),
        Register('pcon0', 4, 0x920c),
        Register('piear', 4, 0x9210),
        Register('pietr', 4, 0x9214),
        Register('compat', 4, 0x9400),
        Register('fpu_trap_con', 4, 0xa000),
        Register('fpu_trap_pc', 4, 0xa004),
        Register('fpu_trap_opc', 4, 0xa008),
        Register('fpu_trap_src1', 4, 0xa010),
        Register('fpu_trap_src2', 4, 0xa014),
        Register('fpu_trap_src3', 4, 0xa018),
        Register('dpr0_l', 4, 0xc000),
        Register('dpr0_u', 4, 0xc004),
        Register('dpr1_l', 4, 0xc008),
        Register('dpr1_u', 4, 0xc00c),
        Register('dpr2_l', 4, 0xc010),
        Register('dpr2_u', 4, 0xc014),
        Register('dpr3_l', 4, 0xc018),
        Register('dpr3_u', 4, 0xc01c),
        Register('dpr4_l', 4, 0xc020),
        Register('dpr4_u', 4, 0xc024),
        Register('dpr5_l', 4, 0xc028),
        Register('dpr5_u', 4, 0xc02c),
        Register('dpr6_l', 4, 0xc030),
        Register('dpr6_u', 4, 0xc034),
        Register('dpr7_l', 4, 0xc038),
        Register('dpr7_u', 4, 0xc03c),
        Register('dpr8_l', 4, 0xc040),
        Register('dpr8_u', 4, 0xc044),
        Register('dpr9_l', 4, 0xc048),
        Register('dpr9_u', 4, 0xc04c),
        Register('dpr10_l', 4, 0xc050),
        Register('dpr10_u', 4, 0xc054),
        Register('dpr11_l', 4, 0xc058),
        Register('dpr11_u', 4, 0xc05c),
        Register('dpr12_l', 4, 0xc060),
        Register('dpr12_u', 4, 0xc064),
        Register('dpr13_l', 4, 0xc068),
        Register('dpr13_u', 4, 0xc06c),
        Register('dpr14_l', 4, 0xc070),
        Register('dpr14_u', 4, 0xc074),
        Register('dpr15_l', 4, 0xc078),
        Register('dpr15_u', 4, 0xc07c),
        Register('cpr0_l', 4, 0xd000),
        Register('cpr0_u', 4, 0xd004),
        Register('cpr1_l', 4, 0xd008),
        Register('cpr1_u', 4, 0xd00c),
        Register('cpr2_l', 4, 0xd010),
        Register('cpr2_u', 4, 0xd014),
        Register('cpr3_l', 4, 0xd018),
        Register('cpr3_u', 4, 0xd01c),
        Register('cpr4_l', 4, 0xd020),
        Register('cpr4_u', 4, 0xd024),
        Register('cpr5_l', 4, 0xd028),
        Register('cpr5_u', 4, 0xd02c),
        Register('cpr6_l', 4, 0xd030),
        Register('cpr6_u', 4, 0xd034),
        Register('cpr7_l', 4, 0xd038),
        Register('cpr7_u', 4, 0xd03c),
        Register('cpr8_l', 4, 0xd040),
        Register('cpr8_u', 4, 0xd044),
        Register('cpr9_l', 4, 0xd048),
        Register('cpr9_u', 4, 0xd04c),
        Register('cpr10_l', 4, 0xd050),
        Register('cpr10_u', 4, 0xd054),
        Register('cpr11_l', 4, 0xd058),
        Register('cpr11_u', 4, 0xd05c),
        Register('cpr12_l', 4, 0xd060),
        Register('cpr12_u', 4, 0xd064),
        Register('cpr13_l', 4, 0xd068),
        Register('cpr13_u', 4, 0xd06c),
        Register('cpr14_l', 4, 0xd070),
        Register('cpr14_u', 4, 0xd074),
        Register('cpr15_l', 4, 0xd078),
        Register('cpr15_u', 4, 0xd07c),
        Register('cpxe_0', 4, 0xe000),
        Register('cpxe_1', 4, 0xe004),
        Register('cpxe_2', 4, 0xe008),
        Register('cpxe_3', 4, 0xe00c),
        Register('dpre_0', 4, 0xe010),
        Register('dpre_1', 4, 0xe014),
        Register('dpre_2', 4, 0xe018),
        Register('dpre_3', 4, 0xe01c),
        Register('dpwe_0', 4, 0xe020),
        Register('dpwe_1', 4, 0xe024),
        Register('dpwe_2', 4, 0xe028),
        Register('dpwe_3', 4, 0xe02c),
        Register('tps_con', 4, 0xe400),
        Register('tps_timer0', 4, 0xe404),
        Register('tps_timer1', 4, 0xe408),
        Register('tps_timer2', 4, 0xe40c),
        Register('tr0evt', 4, 0xf000),
        Register('tr0adr', 4, 0xf004),
        Register('tr1evt', 4, 0xf008),
        Register('tr1adr', 4, 0xf00c),
        Register('tr2evt', 4, 0xf010),
        Register('tra2dr', 4, 0xf014),
        Register('tr3evt', 4, 0xf018),
        Register('tr3adr', 4, 0xf01c),
        Register('tr4evt', 4, 0xf020),
        Register('tr4adr', 4, 0xf024),
        Register('tr5evt', 4, 0xf028),
        Register('tr5adr', 4, 0xf02c),
        Register('tr6evt', 4, 0xf030),
        Register('tr6adr', 4, 0xf034),
        Register('tr7evt', 4, 0xf038),
        Register('tr7adr', 4, 0xf03c),
        Register('cctrl', 4, 0xfc00),
        Register('ccnt', 4, 0xfc04),
        Register('icnt', 4, 0xfc08),
        Register('m1cnt', 4, 0xfc0c),
        Register('m2cnt', 4, 0xfc10),
        Register('m3cnt', 4, 0xfc14),
        Register('dbgsr', 4, 0xfd00),
        Register('exevt', 4, 0xfd08),
        Register('crevt', 4, 0xfd0c),
        Register('swevt', 4, 0xfd10),
        Register('trig_acc', 4, 0xfd30),
        Register('dms', 4, 0xfd40),
        Register('dcx', 4, 0xfd44),
        Register('dbgtcr', 4, 0xfd48),
        Register('pcxi', 4, 0xfe00),
        Register('psw', 4, 0xfe04),
        Register('pc', 4, 0xfe08, alias_names=('ip',)),
        Register('syscon', 4, 0xfe14),
        Register('cpu_id', 4, 0xfe18),
        Register('core_id', 4, 0xfe1c),
        Register('biv', 4, 0xfe20),
        Register('btv', 4, 0xfe24),
        Register('isp', 4, 0xfe28),
        Register('icr', 4, 0xfe2c),
        Register('pipn', 1, 0xfe2e),
        Register('fcx', 4, 0xfe38),
        Register('lcx', 4, 0xfe3c),
        Register('e0', 8, 0xff00),
        Register('d0', 4, 0xff00),
        Register('d1', 4, 0xff04),
        Register('e2', 8, 0xff08),
        Register('d2', 4, 0xff08),
        Register('d3', 4, 0xff0c),
        Register('e4', 8, 0xff10),
        Register('d4', 4, 0xff10),
        Register('d5', 4, 0xff14),
        Register('e6', 8, 0xff18),
        Register('d6', 4, 0xff18),
        Register('d7', 4, 0xff1c),
        Register('e8', 8, 0xff20),
        Register('d8', 4, 0xff20),
        Register('d9', 4, 0xff24),
        Register('e10', 8, 0xff28),
        Register('d10', 4, 0xff28),
        Register('d11', 4, 0xff2c),
        Register('e12', 8, 0xff30),
        Register('d12', 4, 0xff30),
        Register('d13', 4, 0xff34),
        Register('e14', 8, 0xff38),
        Register('d14', 4, 0xff38),
        Register('d15', 4, 0xff3c),
        Register('p0', 8, 0xff80),
        Register('a0', 4, 0xff80),
        Register('a1', 4, 0xff84),
        Register('p2', 8, 0xff88),
        Register('a2', 4, 0xff88),
        Register('a3', 4, 0xff8c),
        Register('p4', 8, 0xff90),
        Register('a4', 4, 0xff90),
        Register('a5', 4, 0xff94),
        Register('p6', 8, 0xff98),
        Register('a6', 4, 0xff98),
        Register('a7', 4, 0xff9c),
        Register('p8', 8, 0xffa0),
        Register('a8', 4, 0xffa0),
        Register('a9', 4, 0xffa4),
        Register('p10', 8, 0xffa8),
        Register('a10', 4, 0xffa8),
        Register('a11', 4, 0xffac),
        Register('p12', 8, 0xffb0),
        Register('a12', 4, 0xffb0),
        Register('a13', 4, 0xffb4),
        Register('p14', 8, 0xffb8),
        Register('a14', 4, 0xffb8),
        Register('a15', 4, 0xffbc),
        Register('r0', 4, 0xf0043f00),
        Register('r1', 4, 0xf0043f04),
        Register('r2', 4, 0xf0043f08),
        Register('r3', 4, 0xf0043f0c),
        Register('r4', 4, 0xf0043f10),
        Register('r5', 4, 0xf0043f14),
        Register('r6', 4, 0xf0043f18),
        Register('r7', 4, 0xf0043f1c)
    ]

register_arch(['tricore:le:32:tc176x'], 32, Endness.LE, ArchPcode_tricore_LE_32_tc176x)
