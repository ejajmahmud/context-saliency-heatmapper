"""Unit tests for context-saliency-heatmapper."""
import unittest
from context_saliency_heatmapper.heatmapper import SaliencyHeatmapper, PassageItem


class TestSaliencyHeatmapper(unittest.TestCase):
    def setUp(self):
        self.mapper = SaliencyHeatmapper()

    def test_u_shape_distribution(self):
        p = [
            PassageItem("p1", "c1", 1.0),
            PassageItem("p2", "c2", 0.9),
            PassageItem("p3", "c3", 0.2),
            PassageItem("p4", "c4", 0.1)
        ]
        opt = self.mapper.optimize_passage_order(p)
        # First item should be p1 (1.0), last item should be p2 (0.9)
        self.assertEqual(opt[0].passage_id, "p1")
        self.assertEqual(opt[-1].passage_id, "p2")
        # Middle items are lower score
        self.assertLess(opt[1].salience_score, 0.9)
