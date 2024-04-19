# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from dataclasses import dataclass


@dataclass
class Book:
    title: str
    price: float
    amount_in_stock: int
    rating: int
    category: str
    description: str
    upc: str
