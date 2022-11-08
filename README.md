# Smart Image Solver BackEnd

Introduction: A image watermark demo.

<br>
## Preview
<img src="https://user-images.githubusercontent.com/74957969/200536311-7ceb38f9-1d56-4f03-99cd-fb7e022f088e.png" width="350px" align='left'><img src="https://user-images.githubusercontent.com/74957969/200536316-03f88650-ed57-46b1-89b8-1f37fea3c8d6.jpg" width="350px" align='right'>
<img src="https://user-images.githubusercontent.com/74957969/200536326-670fa708-354b-4e84-95e3-45cf6843394c.jpg" width="350px" align='left'><img src="https://user-images.githubusercontent.com/74957969/200536336-4f984aec-7b0f-4b5c-aa58-e65a325dca25.jpg" width="350px" align='right'>
<img src="https://user-images.githubusercontent.com/74957969/200536346-930e22f0-1d1e-4c26-8c82-8a6f89922d25.jpg" width="350px" align='left'><img src="https://user-images.githubusercontent.com/74957969/200536355-48359a2d-f89d-4465-a177-bc02e3014261.jpg" width="350px" align='right'>
<img src="https://user-images.githubusercontent.com/74957969/200536363-aaf86b3d-0a9c-446d-aa57-90016dcd84f3.jpg" width="350px" align='left'><img src="https://user-images.githubusercontent.com/74957969/200536382-ef3fcf06-d481-4832-a1e9-447c76f4a00e.jpg" width="350px" align='right'>
<img src="https://user-images.githubusercontent.com/74957969/200536383-9eb59cb6-7bda-4378-be92-720867ac721f.jpg" width="350px" align='left'><img src="https://user-images.githubusercontent.com/74957969/200536384-9169de4f-49d3-40a5-ad13-b09bb675437d.jpg" width="350px" align='right'>
<img src="https://user-images.githubusercontent.com/74957969/200536388-ca4f6d9d-1065-46b5-8078-a633641687f8.jpg" width="350px">

## Download Release
<br>
u can download apk in Release or click the link:
https://github.com/YoungFog/smart_image_solver_front_app/releases/download/android/Smart_Image_Solver_version_1.0.4.apk


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
