SIMPDR - A (relatively SIMple) PDR/XDR code by SIMon Bruderer (2011,2012).
================================================================================

The model is based on my previous work on outflow walls in YSOs (Bruderer et al.
2009a,b, 2010), however implements several improvements, which are reported in 
Bruderer et al. 2012 (accepted, http://arxiv.org/abs/1201.4860). For this 
study, I have rewritten and further improved several modules of the code, e.g.

- Since the benchmark-problems are in 1d, I can use a much simpler way to calculate 
  the thermal balance, which cuts down the calculation time to 2-4 minutes for a 
  reasonably fine grid (~ 500 points in Av).

- A more stable globally convergent Newton-Raphson solver is used for the chemistry.

- Since there are still several different H2 formation rates in use, I can now easily
  switch between the formulation by Cazaux/Tielens, Cuppen, Hollenbach&McKee or Sternberg
  
- Cooling through the metastable OI and CI lines are now treated a bit more realistic 
  and also more fine structure coolants (Fe, Si, Si+, S) are included by default.

- X-ray heating through H2 recombination is now also included in addition coulomb 
  heating.
  
- I have an updated branch of the code that can run the Ršllig et al. Benchmark 
  study, if we want to do a more "normalized" testing a some point.
  
- The heating or cooling by H2 is refined and now calculated from a toy-model for 
  the collisional excitation, UV fluorescence, line emission and formation in an 
  excited state. It only includes the 14 vibrationally excited levels, averaging 
  over the rotational levels. For low temperature (few 1000 K), the agreement 
  with the Ršllig et al. 2006 rates that have been used before is very good 
  (for the benchmark models usually < 10%). For higher temperatures, however, the 
  toy-model cools more efficiently than the two-level one, since it also includes 
  higher levels that can then be (collisionally) populated. This just what I would 
  expect...
  
- I have changed a few minor things in the chemical network:

  - The collider reaction H+H2 + 52000 K --> 3H, which gets important at the edge 
  of XDRs with high irradiation has been much higher in the UMIST network, compared
  to the high-temperature network of OSU (Harada et al. 2010). This resulted in a
  (unrealistically) steep H/H2 transition. Since the UMIST H+H2 rate is also much 
  higher than other collider reactions, I've decided to use the OSU rates  

  - I've switched off the hydrogenated PAH reactions from the disk model.

  - The photodissociation rates are calculated from the fits (C*exp(-gamma*Av)) instead 
  of the detailed cross-section, since I the UV-radiative transfer works only in 2d so far...

  - For most models, I've switched off freeze-out
  
    
Models run:
-----------

- For the PDR models, I've run the models between Av=1e-7 and Av=10. Certain assumptions 
  (e.g. CR ionization rate 5e-17 s**-1, turbulent line width 1 km/s, Av=6.289e-22*N_Htot), 
  are taken in agreement with the PDR comparison study by Roellig et al. (see document 
  benchmark_request.txt on http://www.astro.uni-koeln.de/site/pdr-comparison/benchmark.htm).
  
- Since there is not much information available about the parameters I should use for 
  the XDR models, I've been taking some assumptions from Rowin Meijerinks thesis:
  X-ray spektra emitted between 1 and 10 keV with a spectra exp(-E/10 keV) (Section 6.3).
  The models are run between Av=2e-5 to 2000 (~ 3e16-3e24 cm**-2).

- The elemental abundance in the gas is assumed to be

   H               1.0e+00
   He              1.0e-01
   C               1.0e-04
   N               5.0e-05
   O               3.0e-04
   Mg              3.0e-07
   Si              2.0e-06
   S               7.0e-06
   Fe              2.0e-07

PDRBench - Network from PDR comparison study by Ršllig et al. Also some atomic data has been 
           exchanged to older rates, that have presumably been used during the benchmark runs.

PDR_A    - Larger chemical network, PAHs at ISM abundance, no freeze-out considered

PDR_B    - Larger chemical network, PAHs at ISM abundance, including freeze-out
           Model PDR5 did only run up to Av ~ 4, due to the high density in combination
           with the relatively low UV flux. Since everything is frozen out there, the 
           CO ladder shouldn't be affected. Model PDR2 doesn't differ much from PDR2 without 
           freeze-out due to photoevaporation. PDR4 shows only little freeze-out at the very edge 
           for the same reason.
           
PDR_C    - Larger chemical network, no PAHs in the network (but as small grains for heating), 
           no freeze-out considered.

XDR_A    - XDR models.

  
  
  
  

