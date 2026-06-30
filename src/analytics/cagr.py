"""
CAGR calculations for the
Nifty100 Financial Intelligence Platform.

Day 10 - Sprint 2

Implemented

1. Revenue CAGR
2. PAT CAGR
3. EPS CAGR

Supported Windows

• 3 Year
• 5 Year
• 10 Year

Handles all required edge cases.
"""

from __future__ import annotations

from typing import Optional


# =====================================================
# CAGR FLAGS
# =====================================================

DECLINE_TO_LOSS = "DECLINE_TO_LOSS"

TURNAROUND = "TURNAROUND"

BOTH_NEGATIVE = "BOTH_NEGATIVE"

ZERO_BASE = "ZERO_BASE"

INSUFFICIENT = "INSUFFICIENT"


# =====================================================
# CORE CAGR ENGINE
# =====================================================

def calculate_cagr(
    start_value: float,
    end_value: float,
    years: int
) -> tuple[Optional[float], Optional[str]]:
    """
    Calculate CAGR.

    Formula

        ((End / Start) ** (1 / Years) - 1) * 100

    Returns

        (cagr, flag)
    """

    if years <= 0:
        return None, INSUFFICIENT

    if start_value == 0:
        return None, ZERO_BASE

    if start_value > 0 and end_value < 0:
        return None, DECLINE_TO_LOSS

    if start_value < 0 and end_value > 0:
        return None, TURNAROUND

    if start_value < 0 and end_value < 0:
        return None, BOTH_NEGATIVE

    cagr = (
        (
            end_value / start_value
        ) ** (1 / years) - 1
    ) * 100

    return cagr, None

# =====================================================
# REVENUE CAGR
# =====================================================

def revenue_cagr(
    start_sales: float,
    end_sales: float,
    years_available: int,
    window: int,
) -> tuple[Optional[float], Optional[str]]:
    """
    Revenue CAGR.

    Returns
    -------
    (cagr, flag)
    """

    if years_available < window:
        return None, INSUFFICIENT

    return calculate_cagr(
        start_value=start_sales,
        end_value=end_sales,
        years=window,
    )


# =====================================================
# PAT CAGR
# =====================================================

def pat_cagr(
    start_pat: float,
    end_pat: float,
    years_available: int,
    window: int,
) -> tuple[Optional[float], Optional[str]]:
    """
    Profit After Tax CAGR.

    Returns
    -------
    (cagr, flag)
    """

    if years_available < window:
        return None, INSUFFICIENT

    return calculate_cagr(
        start_value=start_pat,
        end_value=end_pat,
        years=window,
    )


# =====================================================
# EPS CAGR
# =====================================================

def eps_cagr(
    start_eps: float,
    end_eps: float,
    years_available: int,
    window: int,
) -> tuple[Optional[float], Optional[str]]:
    """
    Earnings Per Share CAGR.

    Returns
    -------
    (cagr, flag)
    """

    if years_available < window:
        return None, INSUFFICIENT

    return calculate_cagr(
        start_value=start_eps,
        end_value=end_eps,
        years=window,
    )

