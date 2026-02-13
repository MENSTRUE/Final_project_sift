import cv2
import numpy as np
import os
import pandas as pd
import time

# Setup
os.makedirs("outputs", exist_ok=True)

img1 = cv2.imread("images/img1.jpeg")
img2 = cv2.imread("images/img2.jpeg")

gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Matching Function
def compare_method(name, detector):

    start = time.time()

    kp1, des1 = detector.detectAndCompute(gray1, None)
    kp2, des2 = detector.detectAndCompute(gray2, None)

    if name == "ORB":
        bf = cv2.BFMatcher(cv2.NORM_HAMMING)
    else:
        bf = cv2.BFMatcher()

    matches = bf.knnMatch(des1, des2, k=2)

    good = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good.append(m)

    inlier_ratio = 0
    mask = None

    if len(good) > 4:
        src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1,1,2)
        dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1,1,2)
        H, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)

        if mask is not None:
            inlier_ratio = sum(mask.ravel()) / len(good)

    end = time.time()

    # Save Keypoints Visualization
    img1_kp = cv2.drawKeypoints(img1, kp1, None)
    img2_kp = cv2.drawKeypoints(img2, kp2, None)

    cv2.imwrite(f"outputs/{name}_keypoints_img1.png", img1_kp)
    cv2.imwrite(f"outputs/{name}_keypoints_img2.png", img2_kp)

    # Save Matching Image
    draw_params = dict(
        matchColor=(0,255,0),
        matchesMask=mask.ravel().tolist() if mask is not None else None,
        flags=2
    )

    match_img = cv2.drawMatches(img1, kp1, img2, kp2, good, None, **draw_params)
    cv2.imwrite(f"outputs/{name}_matching.png", match_img)

    return {
        "Method": name,
        "Keypoints Img1": len(kp1),
        "Keypoints Img2": len(kp2),
        "Good Matches": len(good),
        "Inlier Ratio": round(inlier_ratio,3),
        "Time (s)": round(end-start,3)
    }

# Initialize Detectors
sift = cv2.SIFT_create()
orb = cv2.ORB_create(nfeatures=1000)

# Run Comparison
results = []
results.append(compare_method("SIFT", sift))
results.append(compare_method("ORB", orb))

df = pd.DataFrame(results)
df.to_csv("outputs/comparison_results.csv", index=False)

print("\nFINAL COMPARISON")
print(df)
