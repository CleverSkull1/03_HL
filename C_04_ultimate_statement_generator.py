def make_statement(statement, decoration, amount):
    """Adds additional characters to the start and end of headings as decoration"""

    ends = decoration * amount
    print(f"\n{ends} {statement} {ends}")

