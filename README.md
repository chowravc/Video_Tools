# Video_Tools

Video tools in python (mostly with cv2). Input your files in `/input/`. Run main.py with arguments to use the script.

## Utilities:

1. Video to frames
    
    Input the video inside directory `/input/`.
    
    ```
    python main.py --v2f --vDir input/example.avi
    ```
    
    Frames will be outputted to `/output/<your-video-name>/`.

2. Frames to video
    
    Input the frames inside a directory `/input/<your-directory-name>`.
    
    ```
    python main.py --f2v --fDir input/example/*.tif --fps 25
    ```
    
    Video will be outputted to `/output/<your-directory-name>.avi`.

3. Select frames at equal intervals
    
    Input the frames inside a directory `/input/<your-directory-name>`.
    
    ```
    python main.py --fSel --fDir input/example/*.tif --nSel 100
    ```
    
    Images will be outputted to `/output/<your-directory-name>/`.
