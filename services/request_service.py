from datetime import date


def valid_request_status(status):

    return status in [
        "Open",
        "Assigned",
        "In Progress",
        "Resolved",
        "Closed"
    ]


def valid_priority(priority):

    return priority in [
        "Low",
        "Medium",
        "High",
        "Critical"
    ]


def get_resolution_date(status):

    if status == "Resolved":
        return date.today()

    return None
