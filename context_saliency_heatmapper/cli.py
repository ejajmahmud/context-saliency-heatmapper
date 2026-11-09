"""CLI for context-saliency-heatmapper."""
import sys
import argparse
from .heatmapper import SaliencyHeatmapper, PassageItem


def main():
    parser = argparse.ArgumentParser(description="Context Saliency Heatmapper CLI")
    parser.add_argument("--demo", action="store_true", help="Run U-shaped saliency layout optimization demo")
    args = parser.parse_args()

    if args.demo:
        mapper = SaliencyHeatmapper()
        passages = [
            PassageItem("p_auth", "Authentication tokens", 0.95),
            PassageItem("p_db", "Database credentials", 0.88),
            PassageItem("p_log", "Standard server logs", 0.30),
            PassageItem("p_metric", "CPU telemetry info", 0.25),
            PassageItem("p_api", "API endpoint routes", 0.60)
        ]

        print("Original Order Heatmap:")
        print(mapper.render_ascii_heatmap(passages))

        optimized = mapper.optimize_passage_order(passages)
        print("
Optimized U-Curve Order Heatmap (Highest at boundaries):")
        print(mapper.render_ascii_heatmap(optimized))
    else:
        parser.print_help()
    sys.exit(0)


if __name__ == "__main__":
    main()
