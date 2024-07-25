# research-with-roy

*Forced_Phot_All*
RIGHT NOW THE NET_FLUX IS NOT THE RAW FLUX. IT IS THE FLUX DENSITY. SO THE COLUMN THAT SAYS FLUX DENSITY IS NOT USABLE. ASSUME THAT FLUX DENSITY IS THE "NET_FLUX" COLUMN

- This is the code for doing forced aperture photometry on all of the WISE images. Make sure it is printing nothing but the dataframe and the names of the galaxies and it will only take 1 minute to run through. 
- It has color-color and color-luminosity diagrams as well.
- breif overview of what it does:
    - imports dataframes, one that can be found under the  "Finding where all of Anthony's x-ray sources are" section inside of "attempt 1 for forced phot.ipynb" and it should be the first cell. if you can't find it command f 'inWISE' and it should take you right to it. The second data frame is mentioned below.
    - these dataframes then are manipulated through pd.merge to group x-ray sources based on name, which are then subgrouped to determine the longest exposure ObsID.
    - the code then runs over every source from the inWISE csv aforementioned, and pulls their ra and dec to retreive the fits files from an online service website url that WISE provides.
    - for each galaxy, the ra and dec positions of all of the sources associated with it are pulled.
    - then for each image url found in that service link for that singular galaxy out of the 74 galaxies, it creates a cutout to be later used for images and the positions are converted into WCS world to pixel values.
    - these new ra and dec values are then processed through KDTree as spatial recognition of any completely overlapping sources (meaning a source that has been detected multiple times) to within 5 pixels of the ra and dec of each source.
    - any sources within 5 pixels of each other aggregated into a group, their average position determined, and compiled under one unique point source.
    - THEN, the code runs over every single source 'i', comparing it to every single source that is not itself 'j', and determines the distance between i and j. If the distance is less than their radii added together (which is 9 (pixels?) for both of them) then they must be overlapping. if this overlap is more than 50%, it is an unusable source; you cannot derive any reasonable flux from such a small region. 
    - However, if the overlap is an acceptable amount photometry is conducted and the counts scaled by the area of the region of overlapping. These counts are then subtracted from the original source, taking into account that if there are multiple sources overlapping with this one source (but all with an acceptable amount of overlap) then all of these overlapping counts are also subtracted from the target source's counts.
    - after subtraction of these counts, if they are greater than zero, aperture photometry is conducted. otherwise they will be Nan. (anything that is not acceptable is likely converted to Nan or tagged with some sort of invalid statement. All sources that are valid are thoroughly filtered and at the end of the code are dataframes that can be printed showing these sources exclusively.)
    - of course, if there is no overlap at all, the aperture photometry is run like normal
    - after the aperture photometry, there are many additional add-ons that loop over the galaxy, such as printing its images or calculating the flux density with the newly derived values of flux from the preceding for loop over all the sources in the galaxy.


*Forced_Phot_One* 
- the code needed for doing forced photometry on just one 
- the SED plots are also in here.
attempt1 for forced phot.ipynb has some useful stuff in there, it is the spinoff of HowManyInWISE and starts to do the photometry. it is very well organized. some stufff for merging pandas.

*Step 2*
- a mess, mainly stuff on trying to query the WISE databse.

Files Needed:
- make sure you have "Source_Flux_All_Modified_5.csv", as this is the datatable that I used for organizing the correct queries and galaxies.

