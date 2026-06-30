import logging

from src.analytics.ratios import (
    net_profit_margin,
    operating_profit_margin,
    return_on_equity,
    return_on_capital_employed,
    return_on_assets,
    debt_to_equity,
    high_leverage_flag,
    interest_coverage_ratio,
    interest_coverage_label,
    interest_coverage_warning,
    net_debt,
    asset_turnover,
)


def test_net_profit_margin_normal():
    result = net_profit_margin(
        net_profit=250,
        sales=1000,
    )

    assert result == 25.0


def test_net_profit_margin_zero_sales():
    assert (
        net_profit_margin(
            net_profit=100,
            sales=0,
        )
        is None
    )


def test_return_on_equity_normal():
    result = return_on_equity(
        net_profit=300,
        equity_capital=100,
        reserves=900,
    )

    assert result == 30.0


def test_return_on_equity_negative_denominator():
    assert (
        return_on_equity(
            net_profit=100,
            equity_capital=-200,
            reserves=100,
        )
        is None
    )


def test_return_on_assets_zero_assets():
    assert (
        return_on_assets(
            net_profit=500,
            total_assets=0,
        )
        is None
    )


def test_operating_profit_margin_logs_mismatch(caplog):
    with caplog.at_level(logging.WARNING):

        result = operating_profit_margin(
            operating_profit=300,
            sales=1000,
            reported_opm=20,
        )

    assert result == 30.0

    assert "OPM mismatch detected" in caplog.text


def test_return_on_capital_employed_normal():
    result = return_on_capital_employed(
        operating_profit=250,
        other_income=50,
        equity_capital=500,
        reserves=500,
        borrowings=500,
    )

    assert result == 20.0


def test_return_on_capital_employed_zero_denominator():
    assert (
        return_on_capital_employed(
            operating_profit=100,
            other_income=20,
            equity_capital=0,
            reserves=0,
            borrowings=0,
        )
        is None
    )

# -------------------------------------------------
# DAY 9 TESTS
# -------------------------------------------------

def test_debt_to_equity_debt_free():
    assert debt_to_equity(
        borrowings=0,
        equity_capital=500,
        reserves=500,
    ) == 0


def test_debt_to_equity_normal():
    assert debt_to_equity(
        borrowings=500,
        equity_capital=250,
        reserves=250,
    ) == 1.0


def test_high_leverage_flag():
    ratio = debt_to_equity(
        borrowings=6000,
        equity_capital=500,
        reserves=500,
    )

    assert high_leverage_flag(
        ratio,
        "Industrials",
    ) is True


def test_interest_coverage_ratio_zero_interest():
    assert (
        interest_coverage_ratio(
            operating_profit=500,
            other_income=100,
            interest=0,
        )
        is None
    )


def test_interest_coverage_label():
    assert (
        interest_coverage_label(None)
        == "Debt Free"
    )


def test_interest_coverage_warning():
    icr = interest_coverage_ratio(
        operating_profit=100,
        other_income=0,
        interest=100,
    )

    assert interest_coverage_warning(icr) is True


def test_net_debt():
    assert (
        net_debt(
            borrowings=1200,
            investments=300,
        )
        == 900
    )


def test_asset_turnover():
    assert (
        asset_turnover(
            sales=1000,
            total_assets=500,
        )
        == 2.0
    )
