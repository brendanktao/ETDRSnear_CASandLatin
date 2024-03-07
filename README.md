# Code to Generate ETDRS visual acuity charts in Latin and Canadian Aboriginal Syllabics (CAS)
*Adapted from https://github.com/manu-mannattil/vachart AND https://github.com/shaanbhambra/CAS_Snellen_VA_Chart*

This repository contains a LaTeX file and a Python script for making random ETDRS charts.  PDFs with Latin and CAS ETDRS charts, used at the standard 4m viewing distance, can be produced with this respository. Steps: 
1. Run "VA_Chart.py" to generate the TeX output. Comment in/out whether you want the output to reflect Latin or CAS characters.
2. Open "CAS.TeX". Identify the code output (using CAS characters) from "VA_Chart.py" that resembles what is found in CAS.text and replace the latter with the former. This should involve separately replacing the details under "Length definitions" and "\begin{document}". Repeat this for the "Latin.TeX".
3. If viewing from a non-standard distance (other than 4m), be sure to adjust the "\factor" argument in the .TeX files to adjust accordingly.
4. We recommend using [Overleaf](https://overleaf.com) for compiling each .TeX file to generate the corresponding PDF eye chart. You will need to alter the settings to use the XeLaTeX compiler.


## Background:

The ETDRS chart was developed to be a standardized alternative to the Snellen chart, and therefore more accurate (especially for research). The following are standards in the standard ETDRS chart: 
1. Letter Size and Scaling: The ETDRS chart uses a logarithmic scale for letter sizes, specifically the logMAR scale. The chart is designed so that each line represents a 0.1 logMAR change in visual acuity, with five letters per line. The size of the letters is precisely calculated to follow this scale.
2. Distance for Testing: The standardized testing distance for the ETDRS chart is 4 meters (approximately 13 feet). This distance allows for a more accurate measurement across a range of visual acuities.
3. Optotype: The ETDRS chart uses the Sloan letters (C, D, H, K, N, O, R, S, V, Z) for its optotypes. These letters were chosen because of their uniformity and recognizability. Each letter is designed to subtend a visual angle of 5 minutes of arc at a specified distance, with each element of the letter (e.g., the width of the lines) subtending 1 minute of arc.
4. Layout: The ETDRS chart consists of 14 rows, with each row containing five letters of the same size. The letters are arranged in a specific way to minimize memorization and ensure each visual acuity level is represented by a balanced set of optotypes.
5. Visual Acuity Notation: Visual acuity on the ETDRS chart is recorded in logMAR values. This system allows for a more precise and standardized measurement of visual acuity than the Snellen fraction. A logMAR value of 0 corresponds to "20/20" vision in the Snellen system, with positive values indicating worse visual acuity and negative values indicating better visual acuity.

This repository should produce a Latin alphabet ETDRS chart that follows the above standardized parameters. This repository also produces a CAS-equivalent ETDRS chart, using the optotypes of ᐱ, ᑎ, ᑭ, ᒧ, ᒋ, ᒥ, ᑯ, ᒧ, and ᔨ, which are relatively preserved across Inuktitut, Cree, and Ojibwe. Note that, currently, there is no specific optotype set recommended for CAS, as is the case with Sloan letters for Latin characters.


## Further reading

R. J. Kolker, [Subjective Refraction and Prescribing Glasses][sub] (American Academy of Opthalmology, San Francisco, CA, 2014).

A. R. Elkington, H. J. Frank, M. J. Greaney, Clinical Optics, 3rd ed. (Blackwell Science, Oxford, 1999).

## Disclaimer and License

This repository is for informational purposes only and do not constitute medical advice. It is not intended to replace the advice of a qualified health provider or a licensed optometrist.

[snellen]: https://en.wikipedia.org/wiki/Snellen_chart
[sil]: http://scripts.sil.org/OFL
[sub]: http://web.archive.org/web/20220309081507/https://www.aao.org/Assets/563fc40b-1466-477e-bc12-4e62f8b2d324/635476894936870000/subjective-refraction-prescribing-glasses-pdf
