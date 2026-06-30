"""
Profitability ratio calculations for the
Nifty100 Financial Intelligence Platform.

Day 08 - Sprint 2

Implemented Ratios
------------------
1. Net Profit Margin (NPM)
2. Operating Profit Margin (OPM)
3. Return on Equity (ROE)
4. Return on Capital Employed (ROCE)
5. Return on Assets (ROA)

ROCE uses:

EBIT = Operating Profit + Other Income

Financial companies will use sector-relative
benchmarking in a later sprint.
"""

from __future__ import annotations

import logging
from typing import Optional


logger = logging.getLogger(__name__)


def net_profit_margin(
    net_profit: float,
    sales: float
) -> Optional[float]:
    """
    Net Profit Margin

    Formula:
        net_profit / sales * 100

    Returns
    -------
    float | None
    """

    if sales == 0:
        return None

    return (net_profit / sales) * 100


def operating_profit_margin(
    operating_profit: float,
    sales: float,
    reported_opm: float | None = None
) -> Optional[float]:
    """
    Operating Profit Margin

    Formula:
        operating_profit / sales * 100

    Cross-checks the calculated value against the
    reported OPM percentage.

    Logs a warning if the difference exceeds 1%.
    """

    if sales == 0:
        return None

    calculated = (operating_profit / sales) * 100

    if reported_opm is not None:

        difference = abs(calculated - reported_opm)

        if difference > 1:

            logger.warning(
                (
                    "OPM mismatch detected. "
                    "Calculated=%.2f "
                    "Reported=%.2f "
                    "Difference=%.2f"
                ),
                calculated,
                reported_opm,
                difference
            )

    return calculated


def return_on_equity(
    net_profit: float,
    equity_capital: float,
    reserves: float
) -> Optional[float]:
    """
    Return on Equity (ROE)

    Formula:
        net_profit /
        (equity_capital + reserves)
        * 100
    """

    denominator = equity_capital + reserves

    if denominator <= 0:
        return None

    return (net_profit / denominator) * 100


def return_on_capital_employed(
    operating_profit: float,
    other_income: float,
    equity_capital: float,
    reserves: float,
    borrowings: float,
    broad_sector: str | None = None
) -> Optional[float]:
    """
    Return on Capital Employed (ROCE)

    EBIT = Operating Profit + Other Income

    Formula

        EBIT /
        (
            Equity Capital +
            Reserves +
            Borrowings
        )
        * 100

    Financial sector benchmarking will be
    implemented in a future sprint.
    """

    ebit = operating_profit + other_income

    denominator = (
        equity_capital +
        reserves +
        borrowings
    )

    if denominator <= 0:
        return None

    if (
        broad_sector is not None
        and broad_sector.strip().lower()
        == "financials"
    ):
        logger.info(
            (
                "Financial sector detected. "
                "Sector-relative ROCE benchmark "
                "will be applied in a future sprint."
            )
        )

    return (ebit / denominator) * 100


def return_on_assets(
    net_profit: float,
    total_assets: float
) -> Optional[float]:
    """
    Return on Assets (ROA)

    Formula

        net_profit /
        total_assets
        * 100
    """

    if total_assets == 0:
        return None

    return (net_profit / total_assets) * 100

def debt_to_equity(
    borrowings: float,
    equity_capital: float,
    reserves: float
) -> Optional[float]:
    """
    Debt-to-Equity Ratio

    Formula

        Borrowings /
        (Equity Capital + Reserves)

    Rules

    • Return 0 if borrowings == 0
    • Return None if denominator <= 0
    """

    if borrowings == 0:
        return 0

    denominator = equity_capital + reserves

    if denominator <= 0:
        return None

    return borrowings / denominator


def high_leverage_flag(
    debt_to_equity_ratio: Optional[float],
    broad_sector: str | None = None
) -> bool:
    """
    High leverage flag.

    True only when

    • D/E > 5
    • Company is NOT Financials
    """

    if debt_to_equity_ratio is None:
        return False

    if (
        broad_sector is not None
        and broad_sector.strip().lower()
        == "financials"
    ):
        return False

    return debt_to_equity_ratio > 5

def interest_coverage_ratio(
    operating_profit: float,
    other_income: float,
    interest: float
) -> Optional[float]:
    """
    Interest Coverage Ratio (ICR)

    Formula

        (Operating Profit + Other Income)
        /
        Interest

    Returns
    -------
    None
        If interest == 0
    """

    if interest == 0:
        return None

    ebit = operating_profit + other_income

    return ebit / interest


def interest_coverage_label(
    icr: Optional[float]
) -> str:
    """
    Display label for Interest Coverage Ratio.

    Returns
    -------
    "Debt Free"
        If ICR is None

    ""

        Otherwise
    """

    if icr is None:
        return "Debt Free"

    return ""


def interest_coverage_warning(
    icr: Optional[float]
) -> bool:
    """
    Returns True if the company is at risk of
    not covering interest payments.

    Rule

        ICR < 1.5
    """

    if icr is None:
        return False

    return icr < 1.5


def net_debt(
    borrowings: float,
    investments: float
) -> float:
    """
    Net Debt

    Formula

        Borrowings - Investments

    Investments are treated as a proxy
    for liquid assets.
    """

    return borrowings - investments


def asset_turnover(
    sales: float,
    total_assets: float
) -> Optional[float]:
    """
    Asset Turnover Ratio

    Formula

        Sales /
        Total Assets

    Returns
    -------
    None
        If total_assets == 0
    """

    if total_assets == 0:
        return None

    return sales / total_assets


