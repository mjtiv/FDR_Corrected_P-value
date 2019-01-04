# FDR_Corrected_P-value

Code to Run FDR Adjustment of P-values for Multiple Testing

This is an example code of how to run FDR Adjustment of p-values for multiple testing based
on the Benjamini-Hochberg Paper (1995).

Example dataset used in the code comes directly from their paper on the topic. 

Becauses the values are corrected, a user can then determine the threshold
for significance of the p-values. 

There are three versions of code found here:

FDR_Code_Matches_R - Implements p-value adjustment that matches the R output exactly (BEST VERSION OF CODE TO USE)

FDR_Code_Less_Stringent - Adjusted p-values, but takes the lowest adjusted p-value (more significant value) for all duplicate values, but has no correction being implemented if during the sorting/p-value adjustment a following ranked p-value has a better resulting q-value.

FDR_Code_Stringent - Adjusted p-values, but takes the highest adjusted p-value (less significant value) for all duplicate values, but has no correction being implemented if during the sorting/p-value adjustment a following ranked p-value has a better resulting q-value.
