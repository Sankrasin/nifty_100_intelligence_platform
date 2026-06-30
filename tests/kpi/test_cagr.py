from src.analytics.cagr import (
    calculate_cagr,
    revenue_cagr,
    pat_cagr,
    eps_cagr,
    DECLINE_TO_LOSS,
    TURNAROUND,
    BOTH_NEGATIVE,
    ZERO_BASE,
    INSUFFICIENT,
)


def test_calculate_cagr_normal():
    cagr, flag = calculate_cagr(
        start_value=100,
        end_value=200,
        years=5,
    )

    assert round(cagr, 2) == 14.87
    assert flag is None


def test_decline_to_loss():
    cagr, flag = calculate_cagr(
        start_value=100,
        end_value=-50,
        years=5,
    )

    assert cagr is None
    assert flag == DECLINE_TO_LOSS


def test_turnaround():
    cagr, flag = calculate_cagr(
        start_value=-100,
        end_value=100,
        years=5,
    )

    assert cagr is None
    assert flag == TURNAROUND


def test_both_negative():
    cagr, flag = calculate_cagr(
        start_value=-100,
        end_value=-50,
        years=5,
    )

    assert cagr is None
    assert flag == BOTH_NEGATIVE


def test_zero_base():
    cagr, flag = calculate_cagr(
        start_value=0,
        end_value=100,
        years=5,
    )

    assert cagr is None
    assert flag == ZERO_BASE


def test_revenue_cagr_insufficient():
    cagr, flag = revenue_cagr(
        start_sales=100,
        end_sales=200,
        years_available=2,
        window=3,
    )

    assert cagr is None
    assert flag == INSUFFICIENT


def test_pat_cagr_normal():
    cagr, flag = pat_cagr(
        start_pat=100,
        end_pat=150,
        years_available=5,
        window=5,
    )

    assert round(cagr, 2) == 8.45
    assert flag is None


def test_eps_cagr_normal():
    cagr, flag = eps_cagr(
        start_eps=20,
        end_eps=40,
        years_available=5,
        window=5,
    )

    assert round(cagr, 2) == 14.87
    assert flag is None


def test_eps_cagr_insufficient():
    cagr, flag = eps_cagr(
        start_eps=20,
        end_eps=40,
        years_available=4,
        window=5,
    )

    assert cagr is None
    assert flag == INSUFFICIENT


def test_invalid_years():
    cagr, flag = calculate_cagr(
        start_value=100,
        end_value=200,
        years=0,
    )

    assert cagr is None
    assert flag == INSUFFICIENT