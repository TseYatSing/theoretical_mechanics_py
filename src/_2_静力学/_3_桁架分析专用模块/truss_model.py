import numpy as np
from dataclasses import dataclass


@dataclass
class Node:
    id: int
    x: float
    y: float
    is_supported: bool = False
    support_type: str = None  # 'pin' 或 'roller'


@dataclass
class Member:
    id: int
    start_node: int
    end_node: int
    E: float = 2.1e11  # 弹性模量 (钢)
    A: float = 1e-4  # 截面积 (m²)


class TrussModel:
    def __init__(self):
        self.nodes: dict[int, Node] = {}
        self.members: dict[int, Member] = {}
        self.loads: dict[int, np.ndarray] = {}  # 节点荷载

    def add_node(self, node: Node):
        self.nodes[node.id] = node

    def add_member(self, member: Member):
        self.members[member.id] = member

    def apply_load(self, node_id: int, load: np.ndarray):
        """施加节点荷载 [Fx, Fy]"""
        self.loads[node_id] = load