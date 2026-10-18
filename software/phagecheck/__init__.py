"""phagecheck — database-free sanity checks for phage genome assemblies and folds."""

from .betahelix import FoldCall, classify, classify_all
from .dtr import DTRResult, check, coverage_profile, find_dtr

__all__ = ["DTRResult", "check", "coverage_profile", "find_dtr",
           "FoldCall", "classify", "classify_all"]
__version__ = "0.1.0"
