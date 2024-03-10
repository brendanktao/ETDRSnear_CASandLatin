# Code to Generate ETDRS visual acuity charts in Latin and Canadian Aboriginal Syllabics (CAS)
*Adapted from https://github.com/manu-mannattil/vachart AND https://github.com/shaanbhambra/CAS_Snellen_VA_Chart*

This repository contains a LaTeX file and a Python script for making random ETDRS *near* charts.  PDFs with Latin and CAS ETDRS *near* charts, used at the standard 40cm viewing distance, can be produced with this respository. 

Steps for CAS: 
1. Run "ETDRS_CAS.py" to generate the TeX output (this will create a random sequence of CAS letters to use in the ETDRS *near* chart). Set aside this output so that you can refer to it in steps 2/3.
2. Open "CAS.TeX" and identify the code section "Length definitions". Copy the corresponding TeX output from step 1 and use it to replace the "Length definitions" section in LaTeX file.
3. In "CAS.TeX", identify the code section that begins with "\begin{longtable}{ccc}" and ends with "\end{longtable}". Copy the corresponding TeX output from step 1 and use it to replace this section in LaTeX file.
4. If viewing from a non-standard distance (other than 40cm), be sure to adjust the "\factor" argument in the .TeX file to adjust accordingly.
8. We recommend using [Overleaf](https://overleaf.com) for compiling the .TeX file to generate the corresponding PDF eye chart. You will need to alter the settings to use the XeLaTeX compiler.

Steps for Latin: 
1. Run "ETDRS_Latin.py" to generate the TeX output. Unlike for CAS, there are 3 standard sequences of optotypes (Chart1/Chart2/ChartR). Choose one of these sequences where indicated in the code and then set aside the output so that you can refer to it in steps 2/3.
2. Open "Latin.TeX" and identify the code section "Length definitions". Copy the corresponding TeX output from step 1 and use it to replace the "Length definitions" section in LaTeX file.
3. In "Latin.TeX", identify the code section that begins with "\begin{longtable}{ccc}" and ends with "\end{longtable}". Copy the corresponding TeX output from step 1 and use it to replace this section in LaTeX file.
4. If viewing from a non-standard distance (other than 40cm), be sure to adjust the "\factor" argument in the .TeX file to adjust accordingly.
8. We recommend using [Overleaf](https://overleaf.com) for compiling the .TeX file to generate the corresponding PDF eye chart. You will need to alter the settings to use the XeLaTeX compiler.

## Background:

The ETDRS *near* chart was developed to be a standardized alternative to the Snellen chart, and therefore more accurate (especially for research). The following are standards in the standard ETDRS *near* chart: 
1. Letter Size and Scaling: The ETDRS *near* chart uses a logarithmic scale for letter sizes, specifically the logMAR scale. The chart is designed so that each line represents a 0.1 logMAR change in visual acuity, equivalent to the optotype height changing by a factor of 10^0.1 or approximately 1.2589 per line. There are five letters per line. 
2. Distance for Testing: The standardized testing distance for the ETDRS *near* chart is 40cm (approximately 13 feet). This distance allows for a more accurate measurement across a range of visual acuities.
3. Optotype: The ETDRS *near* chart uses the Sloan letters (C, D, H, K, N, O, R, S, V, Z) for its optotypes. These letters were chosen because of their uniformity and recognizability. Each letter is designed to subtend a visual angle of 5 minutes of arc at a specified distance, with each element of the letter (e.g., the width of the lines) subtending 1 minute of arc. The ETDRS *near* chart has 3 standard charts with pre-defined sequences: Chart 1 (often for testing the right eye), Chart 2 (often for testing the left eye), and Chart R (often for re-testing or testing both eyes simultaneously).
4. Layout: The ETDRS *near* chart consists of 14 rows, with each row containing five letters of the same size. The letters are arranged in a specific way to minimize memorization and ensure each visual acuity level is represented by a balanced set of optotypes. The spacing between the rows should be equal to the size of the optotype directly below. The spacing between optotypes should be equal to one letter width.
5. Visual Acuity Notation: Visual acuity on the ETDRS *near* chart is recorded in logMAR values. This system allows for a more precise and standardized measurement of visual acuity than the Snellen fraction. A logMAR value of 0 corresponds to "20/20" vision in the Snellen system, with positive values indicating worse visual acuity and negative values indicating better visual acuity.

This repository should produce a Latin alphabet ETDRS *near* chart that follows the above standardized parameters. This repository also produces a CAS-equivalent ETDRS *near* chart, using the optotypes of ᐱ, ᑎ, ᑭ, ᒧ, ᒋ, ᒥ, ᑯ, ᒧ, and ᔨ, which are relatively preserved across Inuktitut, Cree, and Ojibwe. Note that, currently, there is no specific optotype set recommended for CAS, as is the case with Sloan letters for Latin characters. 


## Further reading

R. J. Kolker, [Subjective Refraction and Prescribing Glasses][sub] (American Academy of Opthalmology, San Francisco, CA, 2014).

A. R. Elkington, H. J. Frank, M. J. Greaney, Clinical Optics, 3rd ed. (Blackwell Science, Oxford, 1999).

## Disclaimer and License

This repository is for informational purposes only and do not constitute medical advice. It is not intended to replace the advice of a qualified health provider or a licensed optometrist.

[snellen]: https://en.wikipedia.org/wiki/Snellen_chart
[sil]: http://scripts.sil.org/OFL
[sub]: http://web.archive.org/web/20220309081507/https://www.aao.org/Assets/563fc40b-1466-477e-bc12-4e62f8b2d324/635476894936870000/subjective-refraction-prescribing-glasses-pdf
