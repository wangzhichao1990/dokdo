# Changelog

## 1.5.0

* Starting this version, Dokdo is packaged with `setuptools`.
* There have been major changes to the Dokdo CLI.
* Added a new plotting method called `regplot()`.
* Added a new command called `prepare-lefse`.
* The `merge_metadata` command has been deprecated.
* Updated the following methods:
    * `_artist()`
    * `alpha_diversity_plot()`
    * `beta_3d_plot()`
    * `beta_parallel_plot()`
    * `barplot()`
    * `ordinate()`
    * `taxa_abundance_bar_plot()`
    * `taxa_abundance_box_plot()`
    * `heatmap()`
* Updated the `make_manifest` command.
* See [#6](https://github.com/sbslee/dokdo/issues/6) for more details.

## 1.4.0

* Added a new command called `summarize`.
* Added a new plotting method called `heatmap()`.
* Updated the following commands:
    * `make_manifest`
    * `add_metadata`
    * `collapse`
* Updated the following methods:
    * `_artist()`
    * `alpha_rarefaction_plot()`
    * `taxa_abundance_bar_plot()`
    * `taxa_abundance_box_plot()`
* See [#4](https://github.com/sbslee/dokdo/issues/4) for more details.

## 1.3.0

* Updated the `ordinate()` method so that the user can now choose to:
    * skip rarefying,
    * provide custom sampling depth for rarefying,
    * provide `qiime2.Artifact` as input instead of file path, and
    * output `PCoAResults % Properties('biplot')` as well as `PCoAResults`.
* Added new plotting methods:
    * `beta_scree_plot()`
    * `beta_parallel_plot()`
    * `addbiplot()`
    * `barplot()`
* See [#2](https://github.com/sbslee/dokdo/issues/2) for more details.

## 1.2.0

* The `tax2seq` command has been deprecated.
* Updated the `_artist()` method to set the font size of title, labels, etc.
* Added the `s` argument to the `ancom_volcano_plot()` method for setting marker size.
* Updated the docstring.
* See [#1](https://github.com/sbslee/dokdo/issues/1) for more details.

## 1.1.0

* Introduced the `addpairs()` method.
* The `beta_2d_plot_gallery()` method has been deprecated.
* Made some changes to the following methods:
    * `ordinate()`
    * `taxa_abundance_bar_plot()`
    * `taxa_abundance_box_plot()`
    * `_artist()`
* Fixed some bugs.
* Made keyword arguments for the `_artist()` method more explicit with `artist_kwargs`.
* Temporary files will be deleted automatically from now on.
* Updated the docstring.
* Plotting methods now accept Artifact and Visualization objects as input.

## 1.0.0

* Initial release.
