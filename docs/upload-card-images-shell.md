Shell Instructions for Uploading Card Images
============================================

## Fork the [`holotable`](https://github.com/swccgpc/holotable) git repo

## Clone the fork locally

```bash

git clone git@github.com:DevoKun/holotable.git
cd holotable

```

## Add the images.
* Sets go in the `Images-HT/starwars` subdirectory.
* Create two new directories for the Virtual set, one per side.
* The _new_ png images will go in the `hires` subdirectory of the set.
```bash
mkdir -p Virtual16-Light/hires
mkdir -p Virtual16-Dark/hires
```

## Commit the new images

```bash
git add -A Virtual16-Light Virtual16-Dark
git commit -m 'Added new Virtual Set 16'
```

## Push the images

```bash
git push
```

## On the **GitHub** website, create a pull request




