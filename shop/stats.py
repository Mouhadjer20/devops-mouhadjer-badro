def most_expensive(prices):
    """prices of the most expensive item, none if empty cart"""
    if not prices:
        return None
    return max(prices)

