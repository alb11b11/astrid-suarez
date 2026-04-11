import os
import shutil
from PIL import Image
import imagehash

# === CONFIG ===
gallery_path = "/Users/alejandrooyarbide/Desktop/Astrid/gallery/paintings"
new_photos_path = "/Users/alejandrooyarbide/Desktop/Astrid/Places_jpg"
output_path = "/Users/alejandrooyarbide/Desktop/Astrid/gallery_2/paintings"

DRY_RUN = False   # 🔒 Set to True to simulate without copying
THRESHOLD = 25   # similarity threshold

VALID_EXTENSIONS = (".jpg", ".jpeg", ".png", ".webp")

os.makedirs(output_path, exist_ok=True)


def is_image(filename):
    return filename.lower().endswith(VALID_EXTENSIONS)


def get_hash(image_path):
    try:
        img = Image.open(image_path)
        return imagehash.phash(img)
    except Exception as e:
        print(f"⚠️ Error reading {image_path}: {e}")
        return None


print("📸 Building gallery hash database...")

gallery_hashes = {}

for file in os.listdir(gallery_path):
    if not is_image(file):
        continue

    full_path = os.path.join(gallery_path, file)
    h = get_hash(full_path)

    if h:
        gallery_hashes[file] = h

print(f"✅ Loaded {len(gallery_hashes)} gallery images")


print("\n🔍 Processing new photos...")

for new_file in os.listdir(new_photos_path):
    if not is_image(new_file):
        continue

    new_path = os.path.join(new_photos_path, new_file)
    new_hash = get_hash(new_path)

    if not new_hash:
        continue

    best_match = None
    best_diff = 999

    for gallery_file, gallery_hash in gallery_hashes.items():
        diff = new_hash - gallery_hash

        if diff < best_diff:
            best_diff = diff
            best_match = gallery_file

    if best_match and best_diff < THRESHOLD:
        dest_path = os.path.join(output_path, best_match)

        if os.path.exists(dest_path):
            print(f"⚠️ Skipping (already exists): {best_match}")
            continue

        print(f"✅ Match: {new_file} → {best_match} (diff={best_diff})")

        if not DRY_RUN:
            shutil.copy2(new_path, dest_path)
        else:
            print(f"🧪 DRY RUN: would copy to {dest_path}")

    else:
        print(f"❌ No good match for: {new_file}")


print("\n🎉 Done.")
