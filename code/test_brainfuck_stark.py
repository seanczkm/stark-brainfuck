from concurrent.futures import process
from brainfuck_stark import *


def test_bfs():
    generator = BaseField.main().generator()
    xfield = ExtensionField.main()
    bfs = BrainfuckStark(generator, xfield)
    program = VirtualMachine.compile(">>[++-]<+++")
    log_time, processor_table, instruction_table, memory_table, input_table, output_table = bfs.vm.simulate(
        program)
    log_time = len(bin(len(processor_table.table)-1)[2:])
    print("lengh of processor table:", len(processor_table.table))
    print("log time:", log_time)
    proof = bfs.prove(log_time, program, processor_table, instruction_table,
                      memory_table, input_table, output_table)
    verdict = bfs.verify(proof, log_time, program,
                         input_table.table, output_table.table)
    assert(verdict == True), "honest proof fails to verify"
