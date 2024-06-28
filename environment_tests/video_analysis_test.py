import numpy as np
from scipy import ndimage
import imageio
import os


def ensure_dtype_uint8(arr):
    return arr.astype(np.uint8)


def test_video_analysis():
    """check that all image loading and analysis stuff works"""
    file_path = os.path.realpath(__file__)
    file_dir, _ = os.path.split(file_path)

    fname = os.path.join(file_dir, "short-movie20170810_182130.mp4")
    reader = imageio.get_reader(fname)
    for frame in reader:
        frame0 = frame[:, :, 1]  # take only green channel
        break
    (height, width) = frame0.shape
    all_frames = []
    reader.set_image_index(0)  # return to start of file
    for frame in reader:
        all_frames.append(frame[:, :, 1])
    all_frames = np.array(all_frames)
    n_frames = len(all_frames)

    mean_frame = np.mean(all_frames, axis=0)
    median_frame = np.median(all_frames, axis=0)

    frame0_absdiff = abs(frame0 - median_frame)

    threshold = 100

    assert threshold + 0 == threshold

    binarized = ensure_dtype_uint8(frame0_absdiff > threshold)

    labels, num_labels = ndimage.label(binarized)

    frames = []
    xs = []
    ys = []
    for i in range(n_frames):
        frame = all_frames[i, :, :]
        frame_absdiff = abs(frame - median_frame)
        binarized = ensure_dtype_uint8(frame_absdiff > threshold)
        labels, num_labels = ndimage.label(binarized)
        if num_labels != 1:
            print("WARNING: num_labels %d on frame %d, skipping" % (num_labels, i))
            continue
        y, x = np.mean(np.nonzero(labels == 1), axis=1)
        frames.append(i)
        xs.append(x)
        ys.append(y)
