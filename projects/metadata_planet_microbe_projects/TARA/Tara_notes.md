This is the master PANGAEA Tara folder: [Tara Oceans Consortium, Coordinators; Tara Oceans Expedition, Participants (2017): Registry of all samples from the Tara Oceans Expedition](https://doi.pangaea.de/10.1594/PANGAEA.875582)

This has 10 datasets:

# 1)

[Alberti, A; Pesant, S; Tara Oceans Consortium, C et al. (2017): Methodology used in the lab for molecular analyses and links to the Sequence Read Archive of selected samples from the Tara Oceans Expedition (2009-2013)](https://doi.pangaea.de/10.1594/PANGAEA.875581)

Sequencing methodology and access to sequence read files from the Tara Oceans Expedition (2009-2013)

Doesn't have the essential metadata, but does have the ENVO environmental feature terms as well as links to the ENA accession numbers.

# 2)

[Ardyna, M; Tara Oceans Consortium, C; Tara Oceans Expedition, P (2017): Environmental context of all station from the Tara Oceans Expedition (2009-2013), about the annual cycle of key parameters estimated daily from remote sensing products at a spatial resolution of 9km. ](https://doi.pangaea.de/10.1594/PANGAEA.883613)

metadata in docx file, and it's about the remote sensing data at a (9-km resolution)

Doesn't have the essential metadata, probably safe to skip for now.

# 3)

[Ardyna, M; Tara Oceans Consortium, C; Tara Oceans Expedition, P (2017): Environmental context of all stations from the Tara Oceans Expedition (2009-2013), about the annual cycle of key parameters estimated daily from remote sensing products at a spatial resolution of 100km.](https://doi.pangaea.de/10.1594/PANGAEA.883614)

metadata in docx file, and it's about the remote sensing data at a (100-km resolution) spacial scale

Doesn't have the essential metadata, probably safe to skip for now.


# 4)

[Ardyna, M; d'Ovidio, F; Speich, S et al. (2017): Environmental context of all samples from the Tara Oceans Expedition (2009-2013), about mesoscale features at the sampling location. ](https://doi.pangaea.de/10.1594/PANGAEA.875577)

This has the metadata listed on PANGAEA, and it has 71 fields including ENA links lat long and expected chem parameters so this may be the "correct full dataset" which we'd need to include. I'll have to check the others to see if this isn't it.

I don't think this is the 'final' TARA data we want. Many of the fields are calculated from models such as Darwin for iron and ammonium, or AMODIS for PAR. So this may be a cool and complete dataset from some modeling paper but the data seem to all be calculated from Darwin and AMODIS models, not true measurements.

# 5)

[Guidi, L; Gattuso, J-P; Pesant, S et al. (2017): Environmental context of all samples from the Tara Oceans Expedition (2009-2013), about carbonate chemistry in the targeted environmental feature. ](https://doi.pangaea.de/10.1594/PANGAEA.875567)

carbonate chemistry project specific metadata, what genomic samples were collected near what carbonate chemistry events. The data is pretty specific to carbonate chemistry, and not as standard metadata which would more likely overlap with the other stuff. So I say we either don't do this, or add this later if Bonnie wants it. Or take specific metadata from this that overlap in the general set of standard oceanographic terms.

# 6)

[Guidi, L; Morin, P; Coppola, L et al. (2017): Environmental context of all samples from the Tara Oceans Expedition (2009-2013), about nutrients in the targeted environmental feature. ](https://doi.pangaea.de/10.1594/PANGAEA.875575)

This has the po4 no3 no2 nox sio4 with the 4 quartiles for (what I understand) is all tara samples. May want to grab this stuff in addition to #7

Include in spreadsheet as TARA_nutr

# 7)

[Guidi, L; Picheral, M; Pesant, S et al. (2017): Environmental context of all samples from the Tara Oceans Expedition (2009-2013), about sensor data in the targeted environmental feature.](https://doi.pangaea.de/10.1594/PANGAEA.875576)

This is the first TARA pangaea page I had been looking at. I had originally presumed this to be everything Tara related. I titled this in the Planet_Microbe_Metadata sheet as TARA_Env_context, but when I noticed that this doesn't have phosphate or other expected fields I looked into the rest of the tara stuff.

This may be the equivalent of TARA_CTD or sensor data. The Chl a and no3 etc data are calculated from in-situ sensors.

Included in spreadsheet as TARA_Env_context

# 8)

[Guidi, L; Ras, J; Claustre, H et al. (2017): Environmental context of all samples from the Tara Oceans Expedition (2009-2013), about pigment concentrations (HPLC) in the targeted environmental feature.](https://doi.pangaea.de/10.1594/PANGAEA.875569)

This one is about about HPLC pigment concentrations. I'm sure this overlaps with HOT_niskin and BATS_pigments. We should decide if this is going to be added later. This stuff doesn't need to be in the first round. Or just some of it.

Include in spreadsheet as: TARA_HPLC

# 9)

[Pesant, S; Tara Oceans Consortium, C; Tara Oceans Expedition, P (2017): Methodology used on board to prepare samples from the Tara Oceans Expedition (2009-2013).](https://doi.pangaea.de/10.1594/PANGAEA.875580)

Metadata about what sampling techniques were used where the samples when. I don't think we need to include this.

# 10)

[Speich, S; Chaffron, S; Ardyna, M et al. (2017): Environmental context of all samples from the Tara Oceans Expedition (2009-2013), about the water column features at the sampling location.](https://doi.pangaea.de/10.1594/PANGAEA.875579)

Data which is associated  with [this paper:](https://www.nature.com/articles/sdata201523)

My understanding is that these were samples taken which correspond to a variety of mesoscale marine features such as surface water layer, deep chlorophyll maximum layer,  mesopelagic zone ... etc.

I'm not sure to what extent these correspond with the other TARA genomic data but this data for many parameters o2 no2 no3 chl for each of the marine features. This is a neat collection as it is highly semantically annotated/ enriched with ENVO terms. But I don't think this data needs to be included in round 1 to make the general overlapping cyberinfrustructure work out. They also mention in the paper something about "the development of on line discovery tools and collaborative annotation tools for sequences and images." Not sure if there is a live portal for this yet or what the deal is if this is something we should be aware of. There are pangaea links in the paper to access TARA metadata but the links don't work for me.

I don't think this is necessary to add now. There would be a lot of terms to come from this but I'm not sure if that's worth doing as of now. We'd need to see if there's scope/if we've pledged to do this.
