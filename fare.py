def get_ticket_fare(stops, hour):
    # base ticket price by distance
    if stops <= 2:
        base = 10
    elif stops <= 5:
        base = 20
    elif stops <= 7:
        base = 30
    else:
        base = 40

    # extra 10% during morning and evening rush hours
    if (hour >= 8 and hour <= 10) or (hour >= 17 and hour <= 20):
        extra = base * 0.10   
        total = base + extra
        is_rush = True
    else:
        extra = 0
        total = base
        is_rush = False
        
    return base, extra, total, is_rush


def deduct_card(balance, fare):
    # make sure card has enough balance to deduct
    if balance >= fare:
        new_balance = balance - fare
        return True, new_balance
    else:
        return False, balance