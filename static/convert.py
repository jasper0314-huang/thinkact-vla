import os

files = [
    ("manipulation_1.mp4", 1200),
    ("manipulation_2.mp4", 1200),
    ("manipulation_3.mp4", 1200),

    ("reflection_1.mp4", 1200),
    ("reflection_2.mp4", 1200),
    ("reflection_3.mp4", 1200),

    ("comparison_1.mp4", 450),
    ("comparison_2.mp4", 450),
    ("comparison_3.mp4", 450),
    ("comparison_4.mp4", 450),
    ("comparison_5.mp4", 450),
    ("comparison_6.mp4", 450),

    ("qa_1.mp4", 400),
    ("qa_2.mp4", 400),
    ("qa_3.mp4", 400),
]

src_dir = "videos_original"
dst_dir = "videos_crf_18"

cmd_template = "ffmpeg -i {SRC_VIDEO} -vf \"scale='min({RES},iw)':-2\" -crf 18 {DST_VIDEO}"

for name, res in files:
    cmd = cmd_template.format(SRC_VIDEO=os.path.join(src_dir, name), DST_VIDEO=os.path.join(dst_dir, name), RES=res)
    print('=' * 50, '\n', cmd, '\n', '=' * 50)
    os.system(cmd)
