import math
from string import ascii_uppercase, Template

# Constants for ETDRS chart generation
METER_TO_INCHES = 39.37008
INCH_TO_POINTS = 72
VIEWING_DISTANCE_METERS = 0.4  # Standard viewing distance for near ETDRS viewing
BASE_OPTOTYPE_MM = 0.582  # in mm, for 0 LogMAR viewed from 40 cm
mm_to_points = METER_TO_INCHES * INCH_TO_POINTS / 1000
base_optotype_size = BASE_OPTOTYPE_MM * mm_to_points

# Predefined sequences for the Latin alphabet ETDRS chart
chart1 = "NCKZORHSDKDOVHRCZRHSONHRCDKSNVZSOKNCKDNRSRZKDHZOVCNVDOKVHCNOSVHCZOZDVK"
chart2 = "DSRKNCKZOHONRKDKZVDCVSHZOHDKCRCSRHNSVZDKNCVOZRHSDVSNROHODHKRZKCSNCRHDV"
chartR = "HVZDSNCVKDCZSHNONVSRKDNROZKCSVDVOHCOHVCKHZCKONCKHDZHCSRSZRDNHCDRORDOSN"

# Function to get a substring from the predefined sequences
def get_sequence(line, length=5):
    # Choose the sequence based on the line number
    sequence = chart1 if line % 3 == 0 else chart2 if line % 3 == 1 else chartR
    start_index = (line % (len(sequence) // length)) * length
    return sequence[start_index:start_index + length]

# ETDRS chart configuration
glyphs = [5] * 14  # 14 lines is standard for ETDRS

# LogMAR to M-size mapping based on provided equivalences
logMAR_to_Msize = {
    -0.3: 0.2, -0.2: 0.25, -0.1: 0.32, 0.0: 0.4,
    0.1: 0.5, 0.2: 0.6, 0.3: 0.8, 0.4: 1.0,
    0.5: 1.3, 0.6: 1.6, 0.7: 2.0, 0.8: 2.5,
    0.9: 3.2, 1.0: 4.0
}

# TeX code templates for layout adjustments
t1 = Template(r"\deflen{$name}{$length$unit} % $dist m")
t2 = Template(r"\noalign{\vskip $vspace pt} $feet / $meters & \optotype{\factor\$name}{$string} & $logMAR & $Msize \\")

output = []

output.append("\n% Length definitions")
optotype_sizes = []
for line in range(len(glyphs)):
    logMAR_value = -0.1 * (line - 10)
    scaling_factor = 10 ** logMAR_value
    optotype_size = round(base_optotype_size * scaling_factor, 6)
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
output.append(r"\begin{longtable}{cccc}")
output.append(r"\textbf{20/  6/} & \textbf{Optotypes (Latin Alphabet Chart)} & \textbf{LogMAR} & \textbf{M-Size} \\ \hline")
for line, g in enumerate(glyphs):
    logMAR_value = -0.1 * (line - 10)
    visual_acuity_20 = round(20 * 10 ** logMAR_value)
    visual_acuity_6 = round(6 * 10 ** logMAR_value)
    sequence = get_sequence(line)  # Get the sequence for this line
    
    # Use the mapping to get the correct M-size for the LogMAR value
    M_size = logMAR_to_Msize.get(round(logMAR_value, 1), "N/A")  # Default to "N/A" if not found

    # Calculate spacing based on the next line's optotype size, if available
    vspace = optotype_sizes[line + 1] if line + 1 < len(optotype_sizes) else 0
    
    output.append(
        t2.substitute(
            vspace=round(vspace, 2),
            feet=visual_acuity_20,
            meters=visual_acuity_6,
            logMAR=round(logMAR_value, 2),
            name="Set" + ascii_uppercase[line],
            string=sequence,
            Msize=M_size
        )
    )
output.append(r"\end{longtable}")

output_joined = "\n".join(output)
print(output_joined)
