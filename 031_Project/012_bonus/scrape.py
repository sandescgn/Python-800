import json
from urllib.parse import urljoin

import pandas as pd
import requests
from bs4 import BeautifulSoup
from slugify import slugify

FILE_NAME = "today_prices.json"
BASE_URL = "https://www.sharesansar.com/"
TODAY_PRICE_URL = "today-share-price"


column_mapper = {
    "s_no": "s_no",
    "symbol": "symbol",
    "conf": "stock_confidence",
    "low": "low_price",
    "high": "high_price",
    "open": "open_price",
    "close": "close_price",
    "prev_close": "prev_close_price",
    "vwap": "vwap",
    "vol": "volume",
    "turnover": "turnover",
    "trans": "transaction",
    "diff": "diff",
    "range": "range",
    "diff_percent": "diff_percent",
    "range_percent": "range_percent",
    "vwap_percent": "vwap_percent",
    "_120_days": "_120_days",
    "_180_days": "_180_days",
    "_52_weeks_low": "_52_weeks_low_price",
    "_52_weeks_high": "_52_weeks_high_price",
}

float_columns = [
    "conf",
    "low",
    "high",
    "open",
    "close",
    "prev_close",
    "vwap",
    "vol",
    "turnover",
    "trans",
    "diff",
    "range",
    "diff_percent",
    "range_percent",
    "vwap_percent",
    "_120_days",
    "_180_days",
    "_52_weeks_low",
    "_52_weeks_high",
]


class ShareSansarScrapper:
    def __init__(self, base_url: str = BASE_URL) -> None:
        self.base_url = base_url

    def fetch_response(self, url: str):
        data = requests.get(url)
        data = data.content
        return data

    def fetch_data(self) -> BeautifulSoup:
        url = urljoin(self.base_url, TODAY_PRICE_URL)
        response = self.fetch_response(url)
        soup = BeautifulSoup(response, "html.parser")
        return soup

    def parse_columns(self, soup: BeautifulSoup) -> list:
        t_heads = soup.find_all("thead")
        columns = []
        for t_head in t_heads:
            for th in t_head.find_all("th"):
                th = th.text.replace("%", "percent")
                column = slugify(th)
                column = column.replace("-", "_")
                if not column.isidentifier():
                    column = "_" + column
                columns.append(column)
        return columns

    def parse_rows(self, soup: BeautifulSoup, columns: list) -> list[dict]:
        t_bodies = soup.find_all("tbody")
        today_prices = []
        for t_body in t_bodies:
            for tr in t_body.find_all("tr"):
                td_data = {}
                for i, td in enumerate(tr.find_all("td")):
                    if columns[i] == "symbol":
                        td_data.update(
                            {
                                columns[i]: td.a.text,
                                "name": td.a.get("title"),
                            }
                        )
                    else:
                        td_data.update({columns[i]: td.text})
                today_prices.append(td_data)
        return today_prices

    def format_data(self, today_prices: list[dict]) -> pd.DataFrame:
        df: pd.DataFrame = pd.DataFrame.from_records(today_prices)
        df = df.drop(columns=["s_no"], axis=1)
        df[float_columns] = (
            df[float_columns]
            .replace("(-?[^\d\.])", "", regex=True)
            .replace("", float("0"))
            .astype(float)
        )
        df[["vol"]] = (
            df[["vol"]]
            .replace("(-?[^\d\.])", "", regex=True)
            .replace("", int("0"))
            .astype(int)
        )
        df.rename(columns=column_mapper, inplace=True)
        return df

    def save_as_json(self, FILE_NAME, today_prices: list[dict]):
        # save to json file directly using to_json
        # today_prices = df.to_json(FILE_NAME, indent=2, orient="records")
        with open(FILE_NAME, "w") as f:
            json.dump(today_prices, f, indent=2)

    def parse_data(self, soup: BeautifulSoup):
        columns = self.parse_columns(soup)
        today_prices = self.parse_rows(soup, columns)
        df = self.format_data(today_prices)
        today_prices = df.to_dict(orient="records")
        self.save_as_json(FILE_NAME, today_prices)
        return today_prices

    def update_today_price(self):
        soup = self.fetch_data()
        today_prices = self.parse_data(soup)
        return today_prices


if __name__ == "__main__":
    ShareSansarScrapper().update_today_price()
