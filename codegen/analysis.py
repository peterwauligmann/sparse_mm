from codegen.visitors import Visitor
from codegen.sugar import *

from typing import List, Set

class Analyzer(Visitor):

    clobbered_registers: Set[Register]
    stack: List[Block]

    def __init__(self):
        self.clobbered_registers = set()
        self.stack = []

    def visitFma(self, stmt: FmaStmt):
        self.clobbered_registers.add(stmt.add_dest)

    def visitAdd(self, stmt: AddStmt):
        self.clobbered_registers.add(stmt.dest)

    def visitLabel(self, stmt: LabelStmt):
        pass

    def visitJump(self, stmt: JumpStmt):
        pass

    def visitMov(self, stmt: MovStmt):
        pass

    def visitStore(self, stmt: MovStmt):
        if isinstance(stmt.dest, Register):
            self.clobbered_registers.add(stmt.dest)

    def visitLoad(self, stmt: MovStmt):
        if isinstance(stmt.dest, Register):
            self.clobbered_registers.add(stmt.dest)

    def visitCmp(self, stmt: CmpStmt):
        pass

    def visitBlock(self, block: Block):
        self.stack.append(block)
        for stmt in block.contents:
            stmt.accept(self)
        self.stack.pop()



