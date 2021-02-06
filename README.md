Holotable Card Data Files
=========================

Up to date card data for use with **Holotable**.

After installing Holotable on Windows or Linux, use the Card Data Files _(CDF)_ on this site to update Holotable to the latest SWCCG release.

## Card Images

* Images are in the `Images-HT/starwars/` subdirectory.
* Card images are used by: **Holotable**, **GEMP**, and **SCOMP**.
* Card images are served from `res.starwarsccg.org/cards`.
* Card images are automatically uploaded to `res.starwarsccg.org/cards` when merging to the `main` branch.

## Image Sizes

Images used by **Holotable** are small and large. There are two sizes of large images. The newer large size is to accomodate larger screens and a desire to actually be able to read the text on a card.

* **Small Images**: 67x87 RGB 72dpi gif
* **_Old_ Large Images**: 350x490 RGB 72dpi gif
* **current Large Images**: 745x1039 RGB 72dpi gif

### Creating t_gif files using `ImageMagick`

```bash
convert -quality 72 -resize 67x87 large/FILENAME.gif t_FILENAME.gif
```



