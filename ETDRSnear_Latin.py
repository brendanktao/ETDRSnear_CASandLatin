import math
from string import ascii_uppercase, Template

# Constants for ETDRS chart generation
METER_TO_INCHES = 39.37008
INCH_TO_POINTS = 72
VIEWING_DISTANCE_METERS = 4  # Standard viewing distance for ETDRS
BASE_OPTOTYPE_MM = 5.82  # Base optotype size for 20/20 vision viewed from 4 meters (in mm)
mm_to_points = METER_TO_INCHES * INCH_TO_POINTS / 1000
base_optotype_size = BASE_OPTOTYPE_MM * mm_to_points

# Predefined charts
chart1 = "NCKZORHSDKDOVHRCZRHSONHRCDKSNVZSOKNCKDNRSRZKDHZOVCNVDOKVHCNOSVHCZOZDVK"
chart2 = "DSRKNCKZOHONRKDKZVDCVSHZOHDKCRCSRHNSVZDKNCVOZRHSDVSNROHODHKRZKCSNCRHDV"
chartR = "HVZDSNCVKDCZSHNONVSRKDNROZKCSVDVOHCOHVCKHZCKONCKHDZHCSRSZRDNHCDRORDOSN"

# Choose which chart to use
optotypes = list(chart2)  # pick the chart you want to create

# ETDRS chart configuration
glyphs_per_row = 5
rows = [optotypes[i:i+glyphs_per_row] for i in range(0, len(optotypes), glyphs_per_row)]

# TeX code templates for layout adjustments
t1 = Template(r"\deflen{$name}{$length$unit} % $dist m")
t2 = Template(r"\noalign{\vskip $vspace pt} $feet / $meters & \optotype{\factor\$name}{$string} & $logMAR\\")

output = []

output.append("\n% Length definitions")
optotype_sizes = []
for line in range(len(rows)):
    logMAR_value = -0.1 * (line - 10)
    scaling_factor = 10 ** logMAR_value
    optotype_size = round(base_optotype_size * scaling_factor, 0)
    optotype_sizes.append(optotype_size)
    
    output.append(
        t1.substitute(
            name="Set" + ascii_uppercase[line],
            length=optotype_size,
            unit="pt",
            dist=VIEWING_DISTANCE_METERS
        )
    )

output.append("\n% Tables\n")
output.append(r"\begin{longtable}{ccc}")
output.append(r"\textbf{20/ / 6/} & \textbf{Optotypes} & \textbf{LogMAR} \\ \hline")
for line, row in enumerate(rows):
    logMAR_value = -0.1 * (line - 10)
    visual_acuity_20 = round(20 * 10 ** logMAR_value)
    visual_acuity_6 = round(6 * 10 ** logMAR_value)
    
    # Calculate spacing based on the next line's optotype size, if available
    vspace = optotype_sizes[line + 1] if line + 1 < len(optotype_sizes) else 0
    
    output.append(
        t2.substitute(
            vspace=round(vspace, 2),
            feet=visual_acuity_20,
            meters=visual_acuity_6,
            logMAR=round(logMAR_value, 2),
            name="Set" + ascii_uppercase[line],
            string="".join(row)
        )
    )
output.append(r"\end{longtable}")

output_joined = "\n".join(output)
print(output_joined)
