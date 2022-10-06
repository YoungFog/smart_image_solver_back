# Smart Image Solver BackEnd

Introduction: A image watermark demo.

### Get Start

Firstly, prepare for you python environment.
- ensure you are using ```python3.7``` currently
- install the dependent packages by trying ```pip install -r requirements.txt```

Secondly, download the pre-trained model which is given by StegaStamp's author. Try,

```bash
wget http://people.eecs.berkeley.edu/~tancik/stegastamp/saved_models.tar.xz
tar -xJf saved_models.tar.xz
rm saved_models.tar.xz
```

Flask

```bash
interface.py
```

### TO-DO

add argparse for ```main.py```

### Related

We implemented this algorithm to Android application, which is available in the release page of [app](https://github.com/litun5315/apps).

### Cite
This repo is a minimized demo of [StegaStamp](https://github.com/tancik/StegaStamp), which is for stydying. For commercial, please contact as the author.