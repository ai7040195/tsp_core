from math import sqrt
from dataclasses import dataclass

@dataclass
class CognitiveVector:
    flc: float  # Failure Logic Component
    ler: float  # Linear Efficiency Rate
    ch: float   # Coherence History
    ilr: float  # Internal Learning Rate

    def magnitude(self) -> float:
        return sqrt(self.flc**2 + self.ler**2 + self.ch**2 + self.ilr**2)

