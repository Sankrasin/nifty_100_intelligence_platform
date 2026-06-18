from src.etl.loader import (
    normalize_ticker,
    normalize_year
)


# --------------------
# TICKER TESTS
# --------------------

def test_ticker_01():
    assert normalize_ticker("tcs") == "TCS"

def test_ticker_02():
    assert normalize_ticker("  tcs ") == "TCS"

def test_ticker_03():
    assert normalize_ticker("hdfcbank") == "HDFCBANK"

def test_ticker_04():
    assert normalize_ticker("INFY") == "INFY"

def test_ticker_05():
    assert normalize_ticker(" axisbank ") == "AXISBANK"

def test_ticker_06():
    assert normalize_ticker("reliance") == "RELIANCE"

def test_ticker_07():
    assert normalize_ticker("sbin") == "SBIN"

def test_ticker_08():
    assert normalize_ticker("itc") == "ITC"

def test_ticker_09():
    assert normalize_ticker("wipro") == "WIPRO"

def test_ticker_10():
    assert normalize_ticker("abb") == "ABB"

def test_ticker_11():
    assert normalize_ticker("  abb") == "ABB"

def test_ticker_12():
    assert normalize_ticker("abb  ") == "ABB"

def test_ticker_13():
    assert normalize_ticker("tatasteel") == "TATASTEEL"

def test_ticker_14():
    assert normalize_ticker("asianpaints") == "ASIANPAINTS"

def test_ticker_15():
    assert normalize_ticker("nestleind") == "NESTLEIND"

def test_ticker_16():
    assert normalize_ticker("maruti") == "MARUTI"

def test_ticker_17():
    assert normalize_ticker("sunpharma") == "SUNPHARMA"

def test_ticker_18():
    assert normalize_ticker("bajaj-auto") == "BAJAJ-AUTO"

def test_ticker_19():
    assert normalize_ticker(None) is None

def test_ticker_20():
    assert normalize_ticker(float("nan")) is None


# --------------------
# YEAR TESTS
# --------------------

def test_year_01():
    assert normalize_year("Mar-23") == "2023-03"

def test_year_02():
    assert normalize_year("Dec 2012") == "2012-12"

def test_year_03():
    assert normalize_year("Mar-14") == "2014-03"

def test_year_04():
    assert normalize_year("Mar-15") == "2015-03"

def test_year_05():
    assert normalize_year("Mar-16") == "2016-03"

def test_year_06():
    assert normalize_year("Mar-17") == "2017-03"

def test_year_07():
    assert normalize_year("Mar-18") == "2018-03"

def test_year_08():
    assert normalize_year("Mar-19") == "2019-03"

def test_year_09():
    assert normalize_year("Mar-20") == "2020-03"

def test_year_10():
    assert normalize_year("Mar-21") == "2021-03"

def test_year_11():
    assert normalize_year("Mar-22") == "2022-03"

def test_year_12():
    assert normalize_year("Mar-24") == "2024-03"

def test_year_13():
    assert normalize_year("Jan 2020") == "2020-01"

def test_year_14():
    assert normalize_year("Feb 2021") == "2021-02"

def test_year_15():
    assert normalize_year("Apr 2022") == "2022-04"

def test_year_16():
    assert normalize_year("May 2023") == "2023-05"

def test_year_17():
    assert normalize_year("Jun 2024") == "2024-06"

def test_year_18():
    assert normalize_year(None) is None

def test_year_19():
    assert normalize_year(float("nan")) is None

def test_year_20():
    assert normalize_year("invalid") == "invalid"