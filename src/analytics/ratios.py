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