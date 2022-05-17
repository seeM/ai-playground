# ai-playground/object-detection

## Usage

Install dependencies:

```sh
pip install -r requirements.txt
```

Install MMDetection if required by the notebook.
The [latest installation instructions](https://mmdetection.readthedocs.io/en/latest/get_started.html#installation) as of writing are:

```sh
pip install openmim
mim install mmdet
```

Launch a Jupyter Lab server:

```sh
jupyter-lab
```

## Docker

You can also launch Jupyter Lab within a docker environment.

Build the image:

```sh
./scripts/build-image.sh
```

Run a container:

```sh
./scripts/run.sh
```
