# gelquant — SDS-PAGE ladder calibration and lane densitometry  *(port in progress)*

**Source:** the same pipeline typed three times, in
`code/0915_gel_annotation.ipynb` (271 L), `code/0929_gel_annotation.ipynb` and
`code/1010_gel_annotation.ipynb` (335 L). That triplication is the argument for packaging it.

**What it does.** Takes a gel photograph plus a ladder specification and lane labels, then:
detects lanes, builds a background model, converts pixel intensity to optical density, fits the
ladder's migration curve, reports each band's apparent mass and each lane's total density, and
writes an annotated overlay image.

**Why it is worth packaging.** Every wet-lab iGEM team runs gels, almost all of them read band
sizes by eye, and the lightweight open alternatives are poor. Dependencies are only
Pillow / numpy / scipy.

## What must change before release

1. **Per-gel constants are inline** in each notebook — lane x-positions, ladder rungs, crop box,
   background window. They must become arguments: a ladder preset
   (Thermo PageRuler Prestained 170–10 kDa is the one we use), a lane spec, and a background
   method.
2. **Two different background models exist** across the three notebooks and the right one depends
   on the photograph: a 70 px Gaussian flat-field for the 0915 images, an 80th-percentile 400 px
   background with optical-density conversion for stained gels on a light box (0929, 1010). Ship
   both, named, and document when each applies — do not silently pick one.
3. **The noise floor must be measured, not assumed.** 0929 used 0.055 (set by paper texture under
   the tray); 1010 measured 0.020 from genuinely unloaded wells. The tool should estimate it from
   empty lanes when they exist and require it explicitly when they do not.
4. **Report both calibrations.** Rung-to-rung interpolation and a cubic fit differ by 2–3 kDa
   between the 55 and 40 kDa rungs; the notebooks report both and so should the tool.
5. **OD totals are not comparable between gels.** Keep that caveat in the output, not just in the
   docs.
6. Add tests on a synthetic gel image with known band positions, where the right answer is known
   by construction.
