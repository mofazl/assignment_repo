def check_limit(borrowed):
    """This function takes the argument borrowed, which refers to the number of books
    borrowed and checks whether the number of books borrowed are within or over limit"""
    if borrowed < 0:
        return "Error: Invalid number of books"
    elif borrowed <= 3:
        return "Within limit"
    elif borrowed <= 6:
        return "Over limit: Fine $5"
    else:
        return "Over limit: Fine $10"
