# OpenFace Command-Line Arguments Reference (Windows)

> Reference guide for commonly used OpenFace command-line flags.

## Input Flags

  -----------------------------------------------------------------------------------------------
  Flag               Description               Windows Example
  ------------------ ------------------------- --------------------------------------------------
  `-f <file>`        Process a single video or `FeatureExtraction.exe -f "D:\Videos\video.mp4"`
                     image.                    

  `-fdir <folder>`   Process all supported     `FeatureExtraction.exe -fdir "D:\Dataset"`
                     files in a folder.        

  `-device <id>`     Capture from webcam.      `FeatureExtraction.exe -device 0`
  -----------------------------------------------------------------------------------------------

## Output Flags

  ---------------------------------------------------------------------------------
  Flag                  Description               Windows Example
  --------------------- ------------------------- ---------------------------------
  `-out_dir <folder>`   Output directory.         `-out_dir "D:\Output"`

  `-of <file>`          Output CSV filename       `-of result.csv`
                        (where supported).        

  `-q` / `-quiet`       Reduce console output.    `-q`
  ---------------------------------------------------------------------------------

## Action Unit (AU) Flags

  --------------------------------------------------------------------------
  Flag           Description               Windows Example
  -------------- ------------------------- ---------------------------------
  `-aus`         Estimate Action Units (AU `-aus`
                 presence & intensity).    

  `-au_static`   Use the static AU model   `-au_static`
                 (recommended for          
                 independent images).      
  --------------------------------------------------------------------------

## Gaze Flags

  Flag      Description                Windows Example
  --------- -------------------------- -----------------
  `-gaze`   Estimate gaze direction.   `-gaze`

## Face Alignment Flags

  Flag          Description                            Windows Example
  ------------- -------------------------------------- -----------------
  `-simalign`   Save similarity-aligned face images.   `-simalign`
  `-hogalign`   Save aligned faces and HOG features.   `-hogalign`

## Visualization Flags

  Flag           Description                         Windows Example
  -------------- ----------------------------------- -----------------
  `-tracked`     Save tracked output video/images.   `-tracked`
  `-vis-track`   Display tracking window.            `-vis-track`
  `-vis-aus`     Overlay Action Units.               `-vis-aus`
  `-vis-gaze`    Overlay gaze vectors.               `-vis-gaze`

## Model Selection / Advanced Flags

  ----------------------------------------------------------------------------------------
  Flag                         Description               Windows Example
  ---------------------------- ------------------------- ---------------------------------
  `-mloc <folder>`             Load models from a custom `-mloc "D:\OpenFace\models"`
                               model directory.          

  `-clm_sigma <value>`         Advanced landmark fitting `-clm_sigma 1.5`
                               parameter.                

  `-clm_window_size <value>`   Landmark search window    `-clm_window_size 11`
                               size.                     
  ----------------------------------------------------------------------------------------

## Common Windows Commands

### Single video

``` powershell
FeatureExtraction.exe ^
-f "D:\Videos\video.mp4" ^
-out_dir "D:\Output" ^
-aus ^
-gaze
```

### Folder of images (single CSV + static AU)

``` powershell
FeatureExtraction.exe ^
-fdir "D:\Dataset\Happy" ^
-out_dir "D:\Output" ^
-aus ^
-au_static ^
-q
```

### Webcam

``` powershell
FeatureExtraction.exe ^
-device 0 ^
-aus ^
-gaze
```

### Save tracked output

``` powershell
FeatureExtraction.exe ^
-f "D:\Videos\video.mp4" ^
-tracked ^
-vis-track
```

### Extract aligned faces

``` powershell
FeatureExtraction.exe ^
-f "D:\Videos\video.mp4" ^
-simalign
```

### Extract HOG features

``` powershell
FeatureExtraction.exe ^
-f "D:\Videos\video.mp4" ^
-hogalign
```

## Notes

-   `FeatureExtraction.exe` is recommended for most AU extraction tasks.
-   Use `-au_static` for unrelated images or image datasets.
-   Use the default (dynamic) AU model for continuous videos.
-   `-mloc` is only needed if your OpenFace models are stored in a
    non-default location.


