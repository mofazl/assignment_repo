def check_limit(borrowed):
    """This function takes the argument borrowed, which refers to the number of books
    borrowed and checks whether the number of books borrowed are within or over limit"""
    if borrowed <= 3:
        return "Within limit"
    elif borrowed > 3 and borrowed <= 6:
        return "Over limit: Fine $5"
    elif borrowed > 6:
        return "Over limit: Fine $10"
    else:
        return "Error: invalid number of books"
