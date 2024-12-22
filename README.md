# DeepRacer Custom Track

This repository contains custom tracks for AWS DeepRacer. It's purpose is to be an extension to the default tracks in the [DeepRacer Simapp](https://github.com/aws-deepracer-community/deepracer-simapp), which contains the tracks that are also available in the AWS DeepRacer Console. See the [Race Data Repository's Track List](https://github.com/aws-deepracer-community/deepracer-race-data/blob/main/raw_data/tracks/README.md) for all details about the official tracks.

Tracks can be:
* A remix of the official tracks by adding/removing features like buildings, lights etc. - whilst still keeping the original track shape.
* A 'cut-out' of an offical track to reduce the size.
* A completely new track.

Motivation for creating a new track can be:
* Increased variability to reduce risk of overfitting for physical racing.
* Creating a smaller foot-print track to allow for physical racing at home.

See the [full track list](tracks/README.md) for details of the tracks.

## Using the repository

The repository works by adding its files 'on top' of an existing Robomaker/Simapp Docker Image.

To use the repository run the following commands:
1. `make build` to collect the relevant files into the `build/` directory.
1. `make image TAG=<your_simapp_tag>` to extend the `awsdeepracercommunity/deepracer-simapp:<your_simapp_tag>` image. 

Once built the image can be used by altering DRfC's `system.env` by using the new tag `<your_simapp_tag>-ext`.

## Other commands

Two other commands are available:

* `make copy-src TARGET=<your_simapp_path>` - this will copy the files into the *source* of the Simapp, i.e from `build/` to `$TARGET/bundle`.
* `make copy-install TARGET=<your_simapp_path>` - this will copy the files into the *built* bundle in Simapp, i.e from `build/` to `$TARGET/install/deepracer_simulation_environment/share/deepracer_simulation_environment/`.

## Altering the environment

It is possible to alter the environment during runtime. Some tracks, e.g. `2024_reinvent_champ_custom` have different parts of the world that can be made invisible.

To try this out:
* Copy from `scripts` folder `alter_environment_0.sh`, `alter_environment_iterator.sh` and `alter_environment_random.py` into the `data/scripts` folder of DRfC.
* Uncomment the `system.env` line `DR_ROBOMAKER_MOUNT_SCRIPTS_DIR=${DR_DIR}/data/scripts` (or add, if you don't have it).
* Set the DR_WORLD to `2024_reinvent_champ_custom`
* Start training

This code will randomize the world when the Robomaker starts (`alter_environment_0.sh`), and if you want to change things over time then put `alter_environment_iterator.sh` into a crontab (or execute manually), it will then run `alter_environment_random.py` in each running Robomaker container.

## Contributing

The repository is open for contributors' tracks. See [CONTRIBUTING](CONTRIBUTING.md) for details.
