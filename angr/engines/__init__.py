from .successors import SimSuccessors
from .engine import SimEngine

from .vex import SimEngineVEX
from .tcg import SimEngineTCG
from .procedure import SimEngineProcedure
from .unicorn import SimEngineUnicorn
from .failure import SimEngineFailure
from .syscall import SimEngineSyscall
from .hook import SimEngineHook

from .hub import EngineHub, EnginePreset


# This is a basic preset of essential engines.
# It is meant to serve as the boilerplate for other presets.
basic_preset = EnginePreset(['failure', 'syscall', 'hook'])
basic_preset.add_default_plugin('failure', SimEngineFailure)
basic_preset.add_default_plugin('syscall', SimEngineSyscall)
basic_preset.add_default_plugin('hook', SimEngineHook)
basic_preset.add_default_plugin('procedure', SimEngineProcedure)

basic_preset.procedure_engine = 'procedure'

# This is a VEX engine preset.
# It will be used as a default preset for engine hub.

vex_preset = basic_preset.copy()

vex_preset.add_default_plugin('unicorn', SimEngineUnicorn)
vex_preset.add_default_plugin('vex', SimEngineVEX)
vex_preset.add_default_plugin('tcg', SimEngineTCG)

vex_preset.order = 'unicorn', 'vex'
vex_preset.default_engine = 'vex'

# This is a TCG engine preset.
# It will be used as a default preset for engine hub.
tcg_preset = basic_preset.copy()

tcg_preset.add_default_plugin('unicorn', SimEngineUnicorn)
tcg_preset.add_default_plugin('tcg', SimEngineTCG)
tcg_preset.order = 'unicorn', 'tcg'
tcg_preset.default_engine = 'tcg'

EngineHub.register_preset('default', vex_preset)
EngineHub.register_preset('tcg', tcg_preset)
