"""Core Context Saliency Heatmapper implementation."""
from typing import Dict, List, Optional, Tuple, Any


class PassageItem:
    def __init__(self, passage_id: str, content: str, salience_score: float):
        self.passage_id = passage_id
        self.content = content
        self.salience_score = salience_score


class SaliencyHeatmapper:
    def __init__(self):
        pass

    def optimize_passage_order(self, passages: List[PassageItem]) -> List[PassageItem]:
        # Sort by salience score descending
        sorted_p = sorted(passages, key=lambda x: x.salience_score, reverse=True)
        if len(sorted_p) <= 2:
            return sorted_p

        # Place highest at the ends (U-shaped distribution):
        # 0 -> start, 1 -> end, 2 -> second from start, 3 -> second from end...
        optimized = [None] * len(sorted_p)
        left = 0
        right = len(sorted_p) - 1

        for i, item in enumerate(sorted_p):
            if i % 2 == 0:
                optimized[left] = item
                left += 1
            else:
                optimized[right] = item
                right -= 1

        return [p for p in optimized if p is not None]

    def render_ascii_heatmap(self, passages: List[PassageItem]) -> str:
        lines = []
        for idx, p in enumerate(passages, 1):
            bars = int(p.salience_score * 20)
            bar_str = "█" * bars
            lines.append(f"Pos {idx:02d} [{p.passage_id[:10]}]: {bar_str} ({p.salience_score:.2f})")
        return "\n".join(lines)
