
def monitor_water_demand(demand, supply, threshold=5):
    """Monitor water demand and generate an agent decision."""

    if demand < 0 or supply < 0 or threshold < 0:
        raise ValueError("Values cannot be negative.")

    gap = demand - supply

    shortage_percentage = (
        (gap / demand) * 100 if demand > 0 else 0
    )

    if gap > 0 and shortage_percentage >= threshold:
        status = "SHORTAGE ALERT"
        message = (
            "Water demand exceeds available supply. "
            "Review allocation and conservation measures."
        )

    elif gap > 0:
        status = "MONITOR"
        message = (
            "A small supply shortage exists. "
            "Continue monitoring the situation."
        )

    else:
        status = "SUFFICIENT SUPPLY"
        message = (
            "Available water supply meets predicted demand."
        )

    return {
        "Predicted Demand": round(demand, 2),
        "Available Supply": round(supply, 2),
        "Supply Gap": round(gap, 2),
        "Shortage Percentage": round(shortage_percentage, 2),
        "Agent Status": status,
        "Message": message
    }
