"""Single source of truth for every number the pipeline and dashboard use.

Everything marked TODO / PLACEHOLDER is YOUR decision. You will be asked to
defend each of them in the comprehension check, so write the justification in
REPORT.md next to the value you choose.
"""
from pathlib import Path

# ----------------------------------------------------------------- dataset
# TODO: exact Roboflow Universe workspace / project / version (public, NOT forked)
ROBOFLOW_WORKSPACE = "pbl-ez66k"
ROBOFLOW_PROJECT = "rotten-and-fresh-fruits"
ROBOFLOW_VERSION = 1

# Class name(s) that mean "bad" -- must match data.yaml names exactly.
# These are the POSITIVE class: the thing we are trying to catch.
# (Dataset classes: fresh-apple, fresh-banana, rotten-apple, rotten-banana)
POSITIVE_CLASSES = ["rotten-apple", "rotten-banana"]

# ---------------------------------------------------------------- training
MODEL_NAME = "yolo11s.pt"      # yolo11n.pt or yolo11s.pt
EPOCHS = 50
IMGSZ = 640
BATCH = 16
SEED = 0

# ------------------------------------------------------------------- paths
ROOT = Path(__file__).resolve().parent
WEIGHTS = ROOT / "weights" / "best.pt"
OUT = ROOT / "outputs"
DATA_DIR = ROOT / "datasets" / "data"

# --------------------------------------------------------------- cost model
# A "case" = one image = one unit that gets a pass / review / fail decision
# (e.g. one fruit, or one crate photo). Decide and defend what a case is.
#
# PLACEHOLDER VALUES. Replace each with a figure you can justify
# ("I assumed X because Y, and the answer changes if X drops below Z").
PLACEHOLDER_COSTS = True       # set False once you've replaced everything below

COSTS = {                      # euros per case
    "fn": 50.0,   # diseased fruit passed as good (complaint, spoilage spread, recall risk)
    "fp": 1.0,    # good fruit rejected (lost margin on one unit)
    "tp": 0.0,    # diseased correctly rejected (maybe disposal cost?)
    "tn": 0.0,    # good correctly passed (usually 0)
}

# Assumed share of cases that are actually diseased IN PRODUCTION.
# NOT the share in the test set -- the test set is usually balanced differently.
BASE_RATE = 0.05

# ------------------------------------------------------------ human review
REVIEW = {
    "seconds": 6,          # time for a person to check one case
    "accuracy": 0.98,      # how often the human gets it right
    "hourly_cost": 18.0,   # EUR / hour, fully loaded
}
REVIEW["cost_per_case"] = REVIEW["seconds"] / 3600 * REVIEW["hourly_cost"]

CASES_PER_DAY = 20_000     # TODO: volume through the line
SHIFT_HOURS = 7.0          # productive hours per reviewer per day
REVIEWERS_AVAILABLE = 2    # people you could realistically staff

# ----------------------------------------------------- chosen thresholds
# Fill in AFTER you've run the sweep and defended the choice in REPORT.md.
# score < LO -> pass ; LO <= score < HI -> human review ; score >= HI -> fail
CHOSEN_LO = 0.30
CHOSEN_HI = 0.70
CHOSEN_SINGLE = 0.50       # best single threshold (no review band), for the curve marker
