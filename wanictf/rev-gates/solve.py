import angr, claripy
import sys, logging

logging.getLogger("angr").setLevel(logging.INFO)
project = angr.Project(
    "./gates", main_opts={"base_addr": 0x00100000}, auto_load_libs=False
)
flag = claripy.BVS("flag", 0x20 * 8)
initial_state = project.factory.full_init_state(
    stdin=flag, add_options=angr.options.unicorn
)
simulation = project.factory.simgr(initial_state)

simulation.explore(
    find=lambda state: b"Correct!" in state.posix.dumps(sys.stdout.fileno()),
    avoid=lambda state: b"Wrong!" in state.posix.dumps(sys.stdout.fileno()),
)
if simulation.found:
    print(simulation.found[0].posix.dumps(sys.stdin.fileno()))
