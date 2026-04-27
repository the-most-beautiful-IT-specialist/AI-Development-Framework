def calculate_manual_fix_rate(total_ai_lines, fixed_lines):
    """
    Calculates the Manual Fix Rate (MFR) according to the framework methodology.
    """
    if total_ai_lines == 0:
        return 0
    mfr = (fixed_lines / total_ai_lines) * 100
    return round(mfr, 2)

# Example of use for a report:
ai_generated = 120
manual_edits = 15
print(f"Current Manual Fix Rate of the project: {calculate_manual_fix_rate(ai_generated, manual_edits)}%")
