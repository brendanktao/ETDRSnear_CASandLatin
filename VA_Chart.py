#to do --- columns to save space, line spacing between lines needs to vary with the letter size

import math, random
from string import ascii_uppercase, Template

# Constants for ETDRS chart generation
METER_TO_INCHES = 39.37008
INCH_TO_POINTS = 72
VIEWING_DISTANCE_METERS = 4  # Standard viewing distance for ETDRS
BASE_OPTOTYPE_MM = 5.82  # Corrected size of optotype for 20/20 vision at 4 meters in mm
mm_to_points = METER_TO_INCHES * INCH_TO_POINTS / 1000
base_optotype_size = BASE_OPTOTYPE_MM * mm_to_points

# Optotypes: Sloan letters for ETDRS
optotypes = list("ᐱᑎᑭᒧᒋᒥᑯᒧᔨ") # standard CASE letters

# ETDRS chart configuration
glyphs = [5] * 14  # Assuming 14 lines for demonstration

# TeX code templates for layout adjustments
t1 = Template(r"\deflen{$name}{$length$unit} % $dist m")
t2 = Template(r"$feet & \optotype{\factor\$name}{$string} & $meters & $logMAR\\")

def randstring(length=1):
    """Generate a random string of optotypes."""
    random.shuffle(optotypes)
    return "".join(optotypes[:length])

def draw_line_for_logMAR(logMAR_value):
    """Determine if a horizontal line is needed for a specific LogMAR value."""
    if logMAR_value == 0 or logMAR_value == 0.5:
        return r"\hline"
    return ""

output = []

output.append("\n% Length definitions")
for line in range(len(glyphs)):
    # Adjust for standard ETDRS progression: starting from the top (poorest acuity)
    logMAR_value = -0.1 * (line - 10)
    scaling_factor = 10 ** logMAR_value
    optotype_size = round(base_optotype_size * scaling_factor, 0)
    
    output.append(
        t1.substitute(
            name="Set" + ascii_uppercase[line],
            length=optotype_size,
            unit="pt",
            dist=VIEWING_DISTANCE_METERS
        )
    )

output.append("\n% Tables\n")
output.append(r"\begin{longtable}{cccc}")
output.append(r"\textbf{20/} & \textbf{Optotypes} & \textbf{6/} & \textbf{LogMAR} \\[30pt]")
output.append(r"\hline")
for line, g in enumerate(glyphs):
    # Correct logMAR scaling for visual acuity reporting
    logMAR_value = -0.1 * (line - 10)
    visual_acuity_20 = round(20 * 10 ** logMAR_value)
    visual_acuity_6 = round(6 * 10 ** logMAR_value)
    
    # Check for horizontal line requirement
    line_command = draw_line_for_logMAR(logMAR_value)
    if line_command:
        output.append(line_command)
    
    output.append(
        t2.substitute(
            meters=visual_acuity_6,
            feet=visual_acuity_20,
            logMAR=round(logMAR_value, 2),
            name="Set" + ascii_uppercase[line],
            string=randstring(g)
        )
    )
output.append(r"\end{longtable}")

output_joined = "\n".join(output)
output_joined

