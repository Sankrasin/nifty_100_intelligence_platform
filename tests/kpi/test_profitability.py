import logging

from src.analytics.ratios import (
    net_profit_margin,
    operating_profit_margin,
    return_on_equity,
    return_on_capital_employed,
    return_on_assets,
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