
def optimize_allocation(supply, household_weight,
                        agriculture_weight, industry_weight):
    """Distribute available supply proportionally by priority."""

    weights = {
        "Household": household_weight,
        "Agriculture": agriculture_weight,
        "Industry": industry_weight
    }

    if supply < 0:
        raise ValueError("Supply cannot be negative.")

    if any(weight < 0 for weight in weights.values()):
        raise ValueError("Priority weights cannot be negative.")

    total_weight = sum(weights.values())

    if total_weight == 0:
        raise ValueError("At least one priority weight must be positive.")

    allocation = {}

    for sector, weight in weights.items():
        amount = supply * weight / total_weight

        allocation[sector] = {
            "Allocated Water": round(amount, 2),
            "Percentage": round(
                weight / total_weight * 100, 2
            )
        }

    return allocation
