_Holotable_ - Source of truth for all SWCCG Card Images and `holotable.exe` Card Data
==============================



## Options

* [Instructions for **`holotable.exe`** **users** looking to **update the local holotable card data**](docs/update-holotable.md)
* [Instructions for **`CDF`** file **developers**](docs/cdf-development.md)
* [Instructions for **`Graphics team members`** who want to **upload new cards**](docs/upload-card-images.md)

### Specs

* [`CDF` file format](docs/cdf-development.md)
* [Card Images](docs/card-images.md)
* [Serving `version.dat` for `holotable.exe`](docs/serving_versiondat_for_holotable.md)




## FAQ

### What is `holotable.exe`?
* `Holotable` is a Windows application for playing SWCCG.
* If you do not already have `holotable.exe` installed, then you do not need [these instructions.](docs/update-holotable.md)
* If you are interested in installing `holotable.exe`, then find installation instructions at [holotable.starwarsccg.org](https://holotable.starwarsccg.org/)

### What are `CDF` files?
* `CDF` stands for Card Data Files.
* `CDF` files are used to provide `holotable.exe` with information about all the cards in the SWCCG card game.
* If you want to contribute to CDF development, [read more about the unique requirements needed in the file formats](docs/cdf-development.md).

### What are the card images stored in _this_ git repo?
* **The Holotable Git repo** is the source of truth for all card images used in SWCCG.
* Card images use by Scomp, gemp, holotable, websites, et al., originate from here.
* If you are a part of the graphics team and want to upload a new card image, or a new virtual set, then [read more about how to upload the image files.](docs/upload-card-images.md)



### Shouldn't the branch name be changed from `master` to something more modern?

* Changing the branch name from `master` to something more modern will break the `holoetable.exe` client.
* Unfortunately, the default branch needs to remain `master` until an update to `www.holotable.com/version.dat` can be released.
* `www.holotable.com/version.dat` has a reference to the `listmd5` file stored on GitHub in the `master` branch.
* `www.holotable.com/version.dat` requires that `listmd5.bz2` can be downloaded from:<br />`https://raw.githubusercontent.com/swccgpc/holotable/master/Images-HT/listmd5.bz2`

