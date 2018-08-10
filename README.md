# FDR_Corrected_P-value
Code to Run FDR correction of P-values

This is an example code of how to run FDR correction of p-values based
on the Benjamini-Hochberg Correction (1995).

Example dataset used in the code comes directly from their paper on
the topic. 

Becauses the values are corrected, a user can then determine the threshold
for significance of the P-values. 

There are two versions of code found and they treat duplicate values slightly different. One version is less stringent and returns the lowest corrected p-value for both duplicates, whereas another version of the code is more stringent and returns the highest corrected p-value for both duplicates (penalizing all the p-values). 
